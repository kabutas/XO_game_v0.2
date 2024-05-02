from game_bord import Bord
import player

game = Bord
player = player.Player

game.print_intro(Bord)

while 1:
    game.print_game_bord(Bord)
    guess = input(f"Spėja žaidėjas {player.get_active_player()}")
    game.add_guess(Bord, guess, player.get_active_player())
    game.test_winner(Bord)

replay = input("Ar žaisime dar kartą? Y/N")

if replay.lower() == 'y':
    game.start()

