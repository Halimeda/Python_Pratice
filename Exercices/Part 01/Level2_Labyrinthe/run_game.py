import world


def main():
    dungeon_size = (15, 15)
    game = world.Game(dungeon_size)
    hero = game.hero
    world.GAME_UPDATE_FUNCTION = game_update

    game.run()


def game_update(hero):
    if not hero.is_at_goal():
        hero.turn_right()
        if hero.is_tile_free():
            hero.move()
        else:
            hero.turn_left()
            if hero.is_tile_free():
                hero.move()
            else:
                hero.turn_left()


if __name__ == '__main__':
    main()
