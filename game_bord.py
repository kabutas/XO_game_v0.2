from tkinter import messagebox
class Bord:
    bord = {'a1': '-', 'a2': '-', 'a3': '-', 'b1': '-', 'b2': '-', 'b3': '-', 'c1': '-', 'c2': '-', 'c3': '-'}
    player_x_wins = 0
    player_0_wins = 0

    def __init__(self):
        pass


    @classmethod
    def get_score(cls):
        return f"Player X has {cls.player_x_wins} wins. Player 0 has {cls.player_0_wins} wins"


    @classmethod
    def reset_bord(cls):
        cls.bord = {'a1': '-', 'a2': '-', 'a3': '-', 'b1': '-', 'b2': '-', 'b3': '-', 'c1': '-', 'c2': '-',
                    'c3': '-', }

    @classmethod
    def add_guess(cls, guess, player):
        if cls.bord[guess] == '-':
            cls.bord[guess] = player

    @classmethod
    def test_winner(cls):
        lines = [
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1']]
        for i in lines:
            if cls.bord[i[0]] == cls.bord[i[1]] == cls.bord[i[2]] != '-':
                if cls.bord[i[0]] == 'X':
                    cls.player_x_wins += 1
                if cls.bord[i[0]] == '0':
                    cls.player_0_wins += 1
                messagebox.showinfo("Congratulation", f"{cls.bord[i[0]]} is the winner!")
                return cls.bord[i[0]]
            if '-' not in cls.bord.values():
                messagebox.showinfo("Tie", "Its A Tie!")
                return "Tie"
        return None

    @classmethod
    def print_game_bord(cls):
        print("\tŽaidimo lenta.")
        print(f"Rezultatas: X = {cls.player_x_wins}\t0 = {cls.player_0_wins}")
        print(f'\t\t{cls.bord['a1']} {cls.bord['a2']} {cls.bord['a3']}\n'
              f'\t\t{cls.bord['b1']} {cls.bord['b2']} {cls.bord['b3']}\n'
              f'\t\t{cls.bord['c1']} {cls.bord['c2']} {cls.bord['c3']}')

    @classmethod
    def print_intro(cls):
        print("Žaidimas Iksiukai - Nuliukai\n"
              "žaidimo lenta sudaryta tokiu būdu:\n"
              "\t\ta1 a2 a3\n"
              "\t\tb1 b2 b3\n"
              "\t\tc1 c2 c3\n"
              "Spėjimas vyksta įvedant langelio koordinates.")
        input("Spauskite Enter kad pradėti: ")

#
