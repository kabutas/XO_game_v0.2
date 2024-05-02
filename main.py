from game_bord import Bord
import player

game = Bord
player = player.Player
game.print_intro()


# def guess():
#     return input(f"Spėja žaidėjas {player.get_active_player()}: ")


def gamestart():
    game.reset_bord()
    while 1:
        game.print_game_bord()
        guess = input(f"Spėja žaidėjas {player.get_active_player()}: ")
        if guess in game.bord and game.bord[guess] == '-':

            game.add_guess(guess, player.get_active_player())
        else:
            print("neteisingas spejimas, arba uzimtas langelis.")

        if game.test_winner():
            print(f"Laiejo žaidėjas {player.get_active_player()}: ")
            # game.player_x_wins += 1
            break
        player.change_player()


gamestart()

replay = input("Ar žaisime dar kartą? Y/N")

if replay.lower() == 'y':
    gamestart()
