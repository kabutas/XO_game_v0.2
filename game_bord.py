class Bord:
    bord = {'a1': '-', 'a2': '-', 'a3': '-', 'b1': '-', 'b2': '-', 'b3': '-', 'c1': '-', 'c2': '-', 'c3': '-', }

    def __init__(self):
        pass

    def reset_bord(self):
        self.bord = {'a1': '-', 'a2': '-', 'a3': '-', 'b1': '-', 'b2': '-', 'b3': '-', 'c1': '-', 'c2': '-',
                     'c3': '-', }


    def add_guess(self, guess, player):
        if self.bord[guess] == '-':
            self.bord[guess] = player

    def test_winner(self):
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
            if self.bord[i[0]] == self.bord[i[1]] == self.bord[i[2]] != '-':
                return self.bord[i[0]]

    def print_game_bord(self):
        print("\tŽaidimo lenta.")
        print("Rezultatas: X = 0\t0 = 0")
        print(f'\t\t{self.bord['a1']} {self.bord['a2']} {self.bord['a3']}\n'
              f'\t\t{self.bord['b1']} {self.bord['b2']} {self.bord['b3']}\n'
              f'\t\t{self.bord['c1']} {self.bord['c2']} {self.bord['c3']}')

    def print_intro(self):
        print("Žaidimas Iksiukai - Nuliukai\n"
              "žaidimo lenta sudaryta tokiu būdu:\n"
              "\t\ta1 a2 a3\n"
              "\t\tb1 b2 b3\n"
              "\t\tc1 c2 c3\n"
              "Spėjimas vyksta įvedant langelio koordinates.")
        input("Spauskite Enter kad pradėti: ")

#
