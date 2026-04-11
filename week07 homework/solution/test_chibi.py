import unittest
from collections import Counter

try:
    from .chibi_battle import ChibiBattle, General
except ImportError:
    from chibi_battle import ChibiBattle, General


def make_game():
    game = ChibiBattle()
    game.load_generals("generals.txt")
    game.load_battle_config("battles.txt")
    return game


class TestChibiBattle(unittest.TestCase):
    def test_load_generals_from_file(self):
        game = make_game()
        self.assertEqual(len(game.generals), 9)
        self.assertIn("劉備", game.generals)
        self.assertIn("曹操", game.generals)

    def test_parse_general_attributes(self):
        game = make_game()
        general = game.generals["關羽"]
        self.assertIsInstance(general, General)
        self.assertEqual(general.name, "關羽")
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, "蜀")

    def test_faction_distribution(self):
        game = make_game()
        factions = Counter(general.faction for general in game.generals.values())
        self.assertEqual(factions["蜀"], 3)
        self.assertEqual(factions["吳"], 3)
        self.assertEqual(factions["魏"], 3)

    def test_eof_parsing(self):
        game = make_game()
        self.assertEqual(len(game.generals), 9)

    def test_load_battle_config(self):
        game = make_game()
        self.assertEqual(game.battle_name, "赤壁")
        self.assertEqual(game.max_waves, 3)

    def test_battle_order_by_speed(self):
        game = make_game()
        battle_order = game.get_battle_order()
        speeds = [general.spd for general in battle_order]
        self.assertEqual(speeds, sorted(speeds, reverse=True))
        self.assertEqual(battle_order[0].spd, 85)
        self.assertEqual(battle_order[-1].spd, 60)

    def test_calculate_damage(self):
        game = make_game()
        damage = game.calculate_damage("關羽", "夏侯惇")
        self.assertEqual(damage, 14)

    def test_damage_counter_accumulation(self):
        game = make_game()
        game.calculate_damage("關羽", "夏侯惇")
        game.calculate_damage("關羽", "曹操")
        self.assertEqual(game.stats["damage"]["關羽"], 26)

    def test_simulate_one_wave_produces_actions(self):
        game = make_game()
        actions = game.simulate_wave(1)
        self.assertTrue(actions)
        self.assertGreater(sum(game.stats["damage"].values()), 0)

    def test_simulate_three_waves_allies_do_more_damage(self):
        game = make_game()
        game.simulate_battle()
        faction_stats = game.get_faction_stats()
        self.assertGreater(faction_stats["蜀"] + faction_stats["吳"], faction_stats["魏"])

    def test_troop_loss_tracking(self):
        game = make_game()
        game.simulate_battle()
        self.assertGreater(game.stats["losses"]["郭嘉"], 0)

    def test_damage_ranking_most_common(self):
        game = make_game()
        game.simulate_battle()
        ranking = game.get_damage_ranking()
        damages = [damage for _, damage in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))

    def test_faction_damage_stats(self):
        game = make_game()
        game.simulate_battle()
        faction_stats = game.get_faction_stats()
        self.assertGreater(faction_stats["蜀"], 0)
        self.assertGreater(faction_stats["吳"], 0)
        self.assertGreater(faction_stats["魏"], 0)

    def test_defeated_generals_exist_after_battle(self):
        game = make_game()
        game.simulate_battle()
        defeated = game.get_defeated_generals()
        self.assertTrue(defeated)
        self.assertIn("郭嘉", defeated)


if __name__ == "__main__":
    unittest.main()