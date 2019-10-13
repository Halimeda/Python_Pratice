import world


def main():
    dungeon_size = (17, 17)
    game = world.Game(dungeon_size)
    hero = game.hero
    world.GAME_UPDATE_FUNCTION = game_update

    game.run()


def game_update(hero):



    if not (hero.is_at_goal()):
        hero.move()
        hero.turn_left()
        while not (hero.is_tile_free()):
            hero.turn_right()

if __name__ == '__main__':
    main()
