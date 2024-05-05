import tkinter as tk
import random
from game_bord import Bord
import player

zaidimas = Bord
player = player.Player
my_font = ("Helvetica", 60)


def start_game():
    root.withdraw()
    game_loop(root)


root = tk.Tk()

root.title("MANO GERIAUSIAS ZAIDIMAS")

# root.geometry("800x600")
button_sp = tk.Button(root, text="One Player", width=20, command=start_game, state='disabled', font=("Helvetica", 30))
button_mp = tk.Button(root, text="Two Players", width=20, command=start_game, font=("Helvetica", 30))
button_quit = tk.Button(root, text="Quit Game", width=20, command=quit, font=("Helvetica", 30))
button_sp.grid(row=1, column=0, columnspan=3)
button_mp.grid(row=2, column=0, columnspan=3)
button_quit.grid(row=3, column=0, columnspan=3)


def game_loop(root):
    game = tk.Tk()
    game.title("MANO GERIAUSIAS ZAIDIMAS")
    w = tk.Label(game, text=zaidimas.get_score(), font="120")
    w.grid(row=0, column=0, columnspan=3)
    # game.geometry('800x600')

    button_a1 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_a1, "a1"), font=my_font)
    button_a2 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_a2, "a2"), font=my_font)
    button_a3 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_a3, "a3"), font=my_font)
    button_b1 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_b1, "b1"), font=my_font)
    button_b2 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_b2, "b2"), font=my_font)
    button_b3 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_b3, "b3"), font=my_font)
    button_c1 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_c1, "c1"), font=my_font)
    button_c2 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_c2, "c2"), font=my_font)
    button_c3 = tk.Button(game, text="-", width=3, command=lambda: rename_button(button_c3, "c3"), font=my_font)

    button_a1.grid(row=1, column=0)
    button_a2.grid(row=1, column=1)
    button_a3.grid(row=1, column=2)
    button_b1.grid(row=2, column=0)
    button_b2.grid(row=2, column=1)
    button_b3.grid(row=2, column=2)
    button_c1.grid(row=3, column=0)
    button_c2.grid(row=3, column=1)
    button_c3.grid(row=3, column=2)

    def rename_button(button, position):
        button.config(text=player.get_active_player(), state='disabled')
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
        empty_cells = [pos for pos, value in zaidimas.bord.items() if value == '-']
        if empty_cells:
            position = random.choice(empty_cells)

    game.mainloop()


root.mainloop()
