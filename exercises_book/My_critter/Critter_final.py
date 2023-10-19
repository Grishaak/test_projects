class Critter(object):
    """Финальная версия зверька"""

    def __init__(self, name, boredom=0, hunger=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.boredom += 1
        self.hunger += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Отлично"
        elif 10 >= unhappiness >= 5:
            m = "Нормально"
        elif 17 >= unhappiness >= 11:
            m = "Не очень"
        else:
            m = "Плохо"
        return m

    def talk(self):
        print(f"Меня зовут {self.name} и сейчас я чуствую себя: {self.mood}")

    def eat(self, food=4):
        print("Спасибо за угощение!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Было весело!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


main_menu = """
Моя зверушка
0 - выход
1 - Узнать о самочувствии зверушки
2 - Покормить зверушку
3 - Поиграть со зверушкой"""
error_input = "Нет такого пункта меню"


def main():
    crit = Critter(input("Введите имя зверушки: "))
    choice = None
    while choice != 0:
        print(main_menu)
        choice = input()
        choice = test_choice(choice)
        if choice == "0":
            print_text("До свидания")
            return
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.talk()
        else:
            print_text(error_input)


def print_text(text: str):
    print(text)


def test_choice(choice: str):
    while True:
        if choice.isdigit():
            return choice
        else:
            print_text(main_menu)
            choice = input("Неверное значение, введите заново: ")


main()