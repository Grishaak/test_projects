class Property_critter(object):
    """Зверь со свойстовм"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя не может быть пустой строкой.")
        else:
            self.__name = new_name
            print('Имя изменено.')

    def talk(self):
        print("Привет, я", self.name)


crit = Property_critter("Иван")

print(crit.name)
crit.talk()
crit.name = input("Новое имя: ")
crit.talk()
