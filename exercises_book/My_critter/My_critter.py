class Critter(object):
    """Виртуальный питомец"""

    def talk(self):
        print("ПРив, я экземпляр класса Critter.")

crit = Critter()
crit.talk()