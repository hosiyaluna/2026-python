from solution.chibi_battle import ChibiBattle, General


def main():
	game = ChibiBattle()
	game.load_generals("generals.txt")
	game.load_battle_config("battles.txt")
	game.run_full_battle()


if __name__ == "__main__":
	main()
