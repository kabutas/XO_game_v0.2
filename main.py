import tkinter as tk
import random
import time
from game_bord import Bord
import player

zaidimas = Bord
player = player.Player
my_font = ("Helvetica", 60)
test_list = zaidimas.win_con


def start_game():
    root.withdraw()
    game_loop(root)


def start_multiplayer():
    root.withdraw()
    game_loop_multi(root)


root = tk.Tk()

root.title("MANO GERIAUSIAS ZAIDIMAS")

button_sp = tk.Button(root, text="One Player", width=20, command=start_game, font=("Helvetica", 30))
button_mp = tk.Button(root, text="Two Players", width=20, command=start_multiplayer, font=("Helvetica", 30))
button_quit = tk.Button(root, text="Quit Game", width=20, command=quit, font=("Helvetica", 30))
button_sp.grid(row=1, column=0, columnspan=3)
button_mp.grid(row=2, column=0, columnspan=3)
button_quit.grid(row=3, column=0, columnspan=3)


def game_loop(root):
    game = tk.Tk()
    game.title("MANO GERIAUSIAS ZAIDIMAS")
    w = tk.Label(game, text=zaidimas.get_score(), font="120")
    w.grid(row=0, column=0, columnspan=3)

    button_dict = {}

    for row in range(3):
        for col in range(3):
            position = str(row) + str(col)
            button = tk.Button(game, text='-', width=3, command=lambda pos=position: rename_button(pos), font=my_font)
            button.grid(row=row + 1, column=col)
            button_dict[position] = button

    def rename_button(position):
        button_dict[position].config(text=player.get_active_player(), state='disabled')
        zaidimas.add_guess(position, player.get_active_player())
        if zaidimas.test_winner():
            game.destroy()
            root.deiconify()
            zaidimas.reset_bord()
        else:
            player.change_player()
            if player.active_player == '0':
                ai_move()

    def ai_move():
        for win_combo in zaidimas.win_con:
            ai_in_pos = [key for key, value in zaidimas.bord.items() if value == "O" and key in win_combo]
            if len(ai_in_pos) == 2:
                empty_cell = [key for key in win_combo if key not in ai_in_pos and zaidimas.bord[key] == "-"]
                if empty_cell:
                    position = empty_cell[0]
                    rename_button(position)
                    return

        for win_combo in zaidimas.win_con:
            opponent_in_pos = [key for key, value in zaidimas.bord.items() if value == "X" and key in win_combo]
            if len(opponent_in_pos) == 2:
                empty_cell = [key for key in win_combo if key not in opponent_in_pos and zaidimas.bord[key] == "-"]
                if empty_cell:
                    position = empty_cell[0]
                    rename_button(position)
                    return

        empty_cells = [key for key, value in zaidimas.bord.items() if value == '-']
        if empty_cells:
            position = random.choice(empty_cells)
            rename_button(position)

    game.mainloop()


def game_loop_multi(root):
    game_multi = tk.Tk()
    game_multi.title("MANO GERIAUSIAS ZAIDIMAS")
    w = tk.Label(game_multi, text=zaidimas.get_score(), font="120")
    w.grid(row=0, column=0, columnspan=3)

    button_dict = {}

    for row in range(3):
        for col in range(3):
            position = str(row) + str(col)
            button = tk.Button(game_multi, text='-', width=3, command=lambda pos=position: rename_button(pos),
                               font=my_font)
            button.grid(row=row + 1, column=col)
            button_dict[position] = button

    def rename_button(position):
        button_dict[position].config(text=player.get_active_player(), state='disabled')
        zaidimas.add_guess(position, player.get_active_player())
        if zaidimas.test_winner():
            game_multi.destroy()
            root.deiconify()
            zaidimas.reset_bord()
        else:
            player.change_player()


    game_multi.mainloop()


root.mainloop()
