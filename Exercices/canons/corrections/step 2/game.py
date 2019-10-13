from game_engine import Sprite

BASE_1 = r'assets/base_1.png'
BASE_2 = r'assets/base_2.png'
BULLET_1 = r'assets/bullet_1.png'
BULLET_2 = r'assets/bullet_2.png'
KEY_A = 97
KEY_P = 112


class Base(Sprite):

    def __init__(self, player_number, position):

        self.player_number = player_number

        if player_number == 1:
            base_player_path = BASE_1
        else:
            base_player_path = BASE_2

        super().__init__(base_player_path, position, anchor=(64, 0))

    def on_key_press(self, key, modifiers):

        if self.player_number == 1 and key == KEY_A:
            print("player 1 shoot.")
        elif self.player_number == 2 and key == KEY_P:
            print("player 2 shoot.")





