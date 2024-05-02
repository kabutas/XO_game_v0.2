import tkinter as tk
from game_bord import Bord
import player

zaidimas = Bord
player = player.Player
my_font = ("Helvetica", 80)


def rename_button(button, position):
    button.config(text=player.get_active_player(), state='disabled')
    # change_player(active_player)
    zaidimas.add_guess(position, player.get_active_player())
    zaidimas.test_winner()
    player.change_player()


def start_game():
    root.withdraw()
    game_loop()


root = tk.Tk()

root.title("MANO GERIAUSIAS ZAIDIMAS")
root.geometry("800x600")
button_sp = tk.Button(root, text="Vienas žaidėjas prieš AI", width=20, command=start_game, font=("Helvetica", 30))
button_mp = tk.Button(root, text="Du žaidėjai prie vieno PC", width=20, command=start_game, font=("Helvetica", 30))
button_quit = tk.Button(root, text="Išjungti žaidimą", width=20, command=quit, font=("Helvetica", 30))
button_sp.pack()
button_mp.pack()
button_quit.pack()


def game_loop():
    game = tk.Tk()
    game.title("MANO GERIAUSIAS ZAIDIMAS")
    game.geometry('800x600')

    button_a1 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_a1, "a1"), font=my_font)
    button_a2 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_a2, "a2"), font=my_font)
    button_a3 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_a3, "a3"), font=my_font)
    button_b1 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_b1, "b1"), font=my_font)
    button_b2 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_b2, "b2"), font=my_font)
    button_b3 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_b3, "b3"), font=my_font)
    button_c1 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_c1, "c1"), font=my_font)
    button_c2 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_c2, "c2"), font=my_font)
    button_c3 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_c3, "c3"), font=my_font)

    button_a1.grid(row=0, column=0)
    button_a2.grid(row=0, column=1)
    button_a3.grid(row=0, column=2)
    button_b1.grid(row=1, column=0)
    button_b2.grid(row=1, column=1)
    button_b3.grid(row=1, column=2)
    button_c1.grid(row=2, column=0)
    button_c2.grid(row=2, column=1)
    button_c3.grid(row=2, column=2)
    game.mainloop()


root.mainloop()

# game.print_intro()


# def guess():
#     return input(f"Spėja žaidėjas {player.get_active_player()}: ")

#
# def gamestart():
#     game.reset_bord()
#     while 1:
#         game.print_game_bord()
#         guess = input(f"Spėja žaidėjas {player.get_active_player()}: ")
#         if guess in game.bord and game.bord[guess] == '-':
#
#             game.add_guess(guess, player.get_active_player())
#         else:
#             print("neteisingas spejimas, arba uzimtas langelis.")
#
#         if game.test_winner():
#             print(f"Laimejo žaidėjas {player.get_active_player()}: ")
#             # game.player_x_wins += 1
#             break
#         player.change_player()
#
#
# gamestart()
#
# replay = input("Ar žaisime dar kartą? Y/N")
#
# if replay.lower() == 'y':
#     gamestart()
