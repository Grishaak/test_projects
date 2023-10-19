class Hero(object):
    """Класс Игрок"""

    def blast(self, enemy):
        print("Игрок стреляет по пришельцу\n")
        enemy.die()


class Alien(object):
    """Класс пришельца-врага"""

    def die(self):
        print("Пришелец умирает.")


# Очень простая схема взаимоотношейни обьектов между собой
hero = Hero()
alien = Alien()
hero.blast(alien)
