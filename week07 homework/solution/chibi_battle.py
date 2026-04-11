from __future__ import annotations

from collections import Counter, defaultdict, namedtuple
from pathlib import Path


General = namedtuple(
    "General",
    ["faction", "name", "hp", "atk", "def_", "spd", "is_leader"],
)


class ChibiBattle:
    """赤壁戰役的簡化回合制模擬器。"""

    def __init__(self):
        self.generals = {}
        self.battle_name = "赤壁"
        self.max_waves = 3
        self.allied_factions = {"蜀", "吳"}
        self.enemy_factions = {"魏"}
        self.reset_battle_state()

    def reset_battle_state(self):
        self.current_hp = {}
        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }
        self.wave_logs = []

    def _resolve_path(self, filename):
        candidate = Path(filename)
        if candidate.is_absolute():
            return candidate

        direct = Path.cwd() / candidate
        if direct.exists():
            return direct

        workspace_relative = Path(__file__).resolve().parent.parent / candidate
        return workspace_relative

    def load_generals(self, filename):
        self.generals = {}
        path = self._resolve_path(filename)

        with path.open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                parts = line.split()
                if len(parts) != 7:
                    raise ValueError(f"Invalid general record: {line}")

                faction, name, hp, atk, def_, spd, is_leader = parts
                self.generals[name] = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == "True"),
                )

        self.reset_battle_state()
        self.current_hp = {name: general.hp for name, general in self.generals.items()}

    def load_battle_config(self, filename):
        path = self._resolve_path(filename)

        with path.open("r", encoding="utf-8") as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line:
                    continue
                if line == "EOF":
                    break

                parts = line.split()
                if len(parts) < 5:
                    raise ValueError(f"Invalid battle record: {line}")

                battle_name = parts[-2]
                waves = parts[-1]
                self.battle_name = battle_name
                self.max_waves = int(waves)
                return

    def get_battle_order(self):
        return sorted(
            self.generals.values(),
            key=lambda general: (-general.spd, general.faction, general.name),
        )

    def is_defeated(self, name):
        return self.current_hp.get(name, 0) <= 0

    def get_active_generals(self, factions=None):
        if factions is None:
            factions = set()
        return [
            general
            for general in self.get_battle_order()
            if (not factions or general.faction in factions) and not self.is_defeated(general.name)
        ]

    def pick_target(self, attacker_name):
        attacker = self.generals[attacker_name]
        enemy_factions = self.enemy_factions if attacker.faction in self.allied_factions else self.allied_factions
        candidates = self.get_active_generals(enemy_factions)
        if not candidates:
            return None

        return min(
            candidates,
            key=lambda general: (
                self.current_hp[general.name],
                general.def_,
                -general.atk,
                general.name,
            ),
        ).name

    def calculate_damage(self, attacker_name, defender_name):
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)

        self.stats["damage"][attacker_name] += damage
        self.stats["losses"][defender_name] += damage
        self.current_hp[defender_name] = max(0, self.current_hp[defender_name] - damage)

        return damage

    def simulate_wave(self, wave_num):
        actions = []
        for attacker in self.get_battle_order():
            if self.is_defeated(attacker.name):
                continue

            target_name = self.pick_target(attacker.name)
            if target_name is None:
                break

            damage = self.calculate_damage(attacker.name, target_name)
            actions.append((attacker.name, target_name, damage))

        self.wave_logs.append({"wave": wave_num, "actions": actions})
        return actions

    def simulate_battle(self):
        self.reset_battle_state()
        self.current_hp = {name: general.hp for name, general in self.generals.items()}

        for wave in range(1, self.max_waves + 1):
            if not self.get_active_generals(self.allied_factions):
                break
            if not self.get_active_generals(self.enemy_factions):
                break
            self.simulate_wave(wave)

    def get_damage_ranking(self, top_n=5):
        return self.stats["damage"].most_common(top_n)

    def get_faction_stats(self):
        faction_damage = defaultdict(int)
        for name, damage in self.stats["damage"].items():
            faction_damage[self.generals[name].faction] += damage
        return dict(faction_damage)

    def get_defeated_generals(self):
        return [
            name
            for name, general in self.generals.items()
            if self.stats["losses"][name] >= general.hp
        ]

    def _health_bar(self, hp, max_hp, width=10):
        ratio = 0 if max_hp == 0 else hp / max_hp
        filled = int(round(ratio * width))
        filled = max(0, min(width, filled))
        return "#" * filled + "." * (width - filled)

    def print_battle_start(self):
        print("=" * 55)
        print(f"赤壁戰役 | {self.battle_name} | 蜀吳聯軍 vs 魏軍")
        print("=" * 55)
        for faction in ["蜀", "吳", "魏"]:
            print(f"[{faction}軍]")
            for general in [item for item in self.get_battle_order() if item.faction == faction]:
                leader = " 軍師" if general.is_leader else ""
                print(
                    f"  {general.name:<4} HP {self._health_bar(general.hp, general.hp)} "
                    f"攻{general.atk:>2} 防{general.def_:>2} 速{general.spd:>2}{leader}"
                )
            print()

    def print_damage_report(self):
        print("傷害排名 Top 5")
        for index, (name, damage) in enumerate(self.get_damage_ranking(), start=1):
            print(f"{index:>2}. {name:<4} {damage:>3} HP")

        print("\n勢力總傷害")
        for faction, damage in sorted(self.get_faction_stats().items()):
            print(f"{faction}: {damage}")

        print("\n戰敗名單")
        defeated = self.get_defeated_generals()
        if not defeated:
            print("無")
        else:
            for name in defeated:
                print(name)

    def run_full_battle(self):
        self.print_battle_start()
        self.simulate_battle()
        self.print_damage_report()


if __name__ == "__main__":
    game = ChibiBattle()
    game.load_generals("generals.txt")
    game.load_battle_config("battles.txt")
    game.run_full_battle()