from game_engine import init, Game, Layer
from game import Base, Bullet


init((800, 600), "Jeu des canons")
game = Game()
layer = Layer()
game.add(layer)

# insérez le code ici.

player1 = Base(1, (64, 0))
player2 = Base(2, (736, 0))
bullet = Bullet(1, (200,200), (10, 10))
layer.add(player1)
layer.add(player2)
layer.add(bullet)

game.run()