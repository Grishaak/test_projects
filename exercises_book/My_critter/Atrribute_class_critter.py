class Atribute_class_critter(object):
    """Зверь с атрибутом класса"""
    total = 0

    def __init__(self, name):
        print("На свет появилась зверушка")
        self.name = name
        Atribute_class_critter.total += 1

    @staticmethod
    def status():
        print(f"Сейчас зверей всего: {Atribute_class_critter.total}")


Atribute_class_critter.status()
crit1 = Atribute_class_critter("Ларионов")
crit2 = Atribute_class_critter("Снегов")
crit3 = Atribute_class_critter("Бромидов")
Atribute_class_critter.status()
# crit1.status()
