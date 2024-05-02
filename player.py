class Player:
    def __init__(self):
        self.active_player = "X"

    def change_player(self):
        if self.active_player == "X":
            self.active_player = "0"
        else:
            self.active_player = "X"

    def get_active_player(self):
        return self.active_player

