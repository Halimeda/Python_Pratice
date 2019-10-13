import world


def main():

    length = int(input("What's Dungeon length ? "))
    width = int(input("What's Dungeon width ? "))

    length = max(7, length)
    width = max(7, width)

    if (length > 25):
        length = 25
    if (width > 20):
        width = 20

    dungeon_size = (length, width)
    game = world.Game(dungeon_size)
    hero = game.hero

    print("Dungeon : Level 1")
    print("The Dungeon have " + str(length) + " squares length and " + str(width) + " squares width.")

    # >>> action du hero

    # Trois actions possibles:
    # move (avance), turn_right (tourne à droite), turn left (tourne à gauche)

    hero.move(2)
    hero.turn_left()
    hero.move(2)
    hero.turn_right()
    hero.move(2)
    hero.turn_left()
    hero.move(2)
   


    game.run()

if __name__ == '__main__':
    main()
