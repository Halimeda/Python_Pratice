import world
from pyglet.window import key
from random import randint

MONSTER_IMAGE_PATH = r'assets/monster.png'
PICKUP_IMAGE_PATH = r'assets/pickup.png'

def manhattan_distance(pos1, pos2):
    return (abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1]))

def main():
    dungeon_size = (10, 10)
    game = world.Game(dungeon_size)

    monster1 = world.Monster(MONSTER_IMAGE_PATH)
    monster2 = world.Monster(MONSTER_IMAGE_PATH)
    game.add_monster(monster1, (1, 2))
    game.add_monster(monster2, (3, 4))

    # pickup = world.Pickup(PICKUP_IMAGE_PATH)
    # game.add_pickup(pickup, (3, 5))

    hero = game.hero

    game.run()

def game_update(hero, monsters):

    print("Update")

    for monster in monsters:
        distance = manhattan_distance(hero.get_pos(), monster.dungeon_position)
        if distance <= 6 and distance >= 3:
            move = randint(0,1)
            print(move)
            if move == 0:
                if (hero.get_pos()[0] - monster.dungeon_position[0]) < 0:
                    monster.down()
                    #if not monster.is_tile_free(down):
                        #monster.left()
                elif (hero.get_pos()[0] - monster.dungeon_position)[0] > 0:
                    monster.up()
                    #if not monster.is_tile_free(up):
                        #monster.right()
        #elif distance < 3:
         #       if (hero.get_pos() - monster.dungeon_position) < 0:
          #          monster.down()
           #         if not monster.is_tile_free(down):
            #            monster.left()
             #   elif (hero.get_pos() - monster.dungeon_position) > 0:
              #      monster.up()
                #    if not monster.is_tile_free(up):
                 #       monster.right()


def on_key_press(key_pressed, modifiers, hero):
    if key_pressed == key.UP:
        hero.move()
    elif key_pressed == key.LEFT:
        hero.turn_left()
    elif key_pressed == key.RIGHT:
        hero.turn_right()

def on_pickup_grabbed(pickup, hero, monsters):
    pass

if __name__ == '__main__':
    main()
