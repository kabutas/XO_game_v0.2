from tkinter import messagebox


class Bord:
    bord = {'00': '-', '01': '-', '02': '-', '10': '-', '11': '-', '12': '-', '20': '-', '21': '-', '22': '-'}
    win_con = [
        ['00', '01', '02'],
        ['10', '11', '12'],
        ['20', '21', '22'],
        ['00', '10', '20'],
        ['01', '11', '21'],
        ['02', '12', '22'],
        ['00', '11', '22'],
        ['02', '11', '20']]
    player_x_wins = 0
    player_0_wins = 0

    def __init__(self):
        pass

    @classmethod
    def get_score(cls):
        return f"Player X has {cls.player_x_wins} wins. Player 0 has {cls.player_0_wins} wins"

    @classmethod
    def reset_bord(cls):
        cls.bord = {'00': '-', '01': '-', '02': '-', '10': '-', '11': '-', '12': '-', '20': '-', '21': '-', '22': '-'}

    @classmethod
    def add_guess(cls, guess, player):
        if cls.bord[guess] == '-':
            cls.bord[guess] = player

    @classmethod
    def test_winner(cls):
        lines = cls.win_con
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