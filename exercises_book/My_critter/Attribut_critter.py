class Atribut_critter(object):
    """Зверёк в аттрибутами"""

    def __init__(self, name):
        print("На свет появилась новая зверушка.")
        self.name = name

    def __str__(self):
        rep = "Обьект класса Attribute_critter "
        rep += "имя: " + self.name
        return rep

    def talk(self):
        print(f"Привет меня зовут {self.name} \n")


crit1 = Atribut_critter("Момик")
crit2 = Atribut_critter("Эвенк")
crit1.talk()
crit2.talk()
print(crit1)
print(crit1.name)
print(crit2.name)
