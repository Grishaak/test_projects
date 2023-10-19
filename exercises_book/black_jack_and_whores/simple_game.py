class Player(object):
    """Игрок"""

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Игрок: {self.name}," \
               f" Очки: {self.score}"


def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Введите число из заданного диапозона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == '__main__':
    print("Да начнётся игра! Но сперва импортируй")
