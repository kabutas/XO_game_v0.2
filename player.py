class Player:
    active_player = 'X'

    @classmethod
    def change_player(cls):
        if cls.active_player == "X":
            cls.active_player = "0"
        else:
            cls.active_player = "X"

    @classmethod
    def get_active_player(cls) -> str:
        return cls.active_player
