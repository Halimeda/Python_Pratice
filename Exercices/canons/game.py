from game_engine import Sprite

BASE_1 = r'assets/base_1.png'
BASE_2 = r'assets/base_2.png'
BULLET_1 = r'assets/bullet_1.png'
BULLET_2 = r'assets/bullet_2.png'
KEY_A = 97
KEY_P = 112
GRAVITY = (0, -50)


class Base(Sprite):
    def __init__(self, player_number, position):
        self.player_number = player_number
        self.power = 0.0
        self.hold = False
        if self.player_number == 1:
            player_base_path = BASE_1
        else:
            player_base_path = BASE_2
        super().__init__(player_base_path, position, anchor=(64,0))

    def on_key_press(self, key, modifiers):
        if key == KEY_A and self.player_number == 1:
            self.hold = True
        elif key == KEY_P and self.player_number == 2:
            self.hold = True

    def on_key_release(self, key, modifiers):
        if key == KEY_A and self.player_number == 1:
            self.add_bullet()
            self.hold = False
        elif key == KEY_P and self.player_number == 2:
            self.add_bullet()
            self.hold = False

    def add_bullet(self):
        initial_position = (self.position[0], self.position[1] + 64)
        initial_speed = (100 * self.power, 100 * self.power)
        if self.player_number == 2:
            initial_speed = ((initial_speed[0] * -1), initial_speed[1])
        bullet = Bullet(self.player_number, initial_position, initial_speed)
        self.layer.add(bullet)
        self.power = 0.0
    
    def update(self, dt):
        super().update(dt)
        if self.hold == True:
            self.power += 0.5 * dt

class Bullet(Sprite):

    def __init__(self, player_number, position, speed):
        self.player_number = player_number
        self.speed = speed
        if player_number == 1:
            bullet_player_path = BULLET_1
        else:
            bullet_player_path = BULLET_2
        super().__init__(bullet_player_path, position, anchor=(8, 8))
    
    def update(self, dt):
        if (self.position[0] < 0) or (self.position[0] > 800) or (self.position[1] < 0) or (self.position[1] > 400) :
            self.destroy
        super().update(dt)

        dvx = GRAVITY[0] * dt
        dvy = GRAVITY[1] * dt
        self.speed = ((self.speed[0] + dvx), (self.speed[1] + dvy))
        dx = self.position[0] + (self.speed[0] * dt)
        dy = self.position[1] + (self.speed[1] * dt)
        self.position = (dx, dy)

    def on_collision(self, other):
        if isinstance(other, Base):
            if other.player_number != self.player_number:
                other.destroy()
        if isinstance(other, Bullet):
            other.destroy()