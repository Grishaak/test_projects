class Critter_constructor(object):
    """Конструктор для зверька"""

    def __init__(self):
        print("на свет появлаь зверушка")

    def talk(self):
        print("Я новая зверушка с конструктором")


crit = Critter_constructor()
crit.talk()
crit1 = Critter_constructor()
crit1.talk()
