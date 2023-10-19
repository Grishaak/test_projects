class Closed_critter(object):
    """Закрытый криттер с закрытыми аттрибутами"""

    def __init__(self, name, mood):
        print("Новый зверь появился!")
        self.__name = name
        self.__mood = mood

    def talk(self):
        print(f"Меня зовут {self.__name}")
        print(f"Мое настроение: {self.__mood}\n")

    def __private_method(self):
        print("Это закрытый метод")

    def public_method(self):
        print("Это публичный метод через него"
              " можно вызывать скрытые методы")
        self.__private_method()


crit = Closed_critter("Вася", "Хорошо")
# print(crit._Closed_critter__mood)
crit.talk()
crit.public_method()