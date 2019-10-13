from game_engine import init, Game, Layer
from game import Base
from game import Bullet


init((800, 600), "Jeu des canons")
game = Game()
layer = Layer()
game.add(layer)
player_1 = Base(1, (64,0))
player_2 = Base(2, (736,0))

layer.add(player_1)
layer.add(player_2)


# insérez le code ici.

game.run()