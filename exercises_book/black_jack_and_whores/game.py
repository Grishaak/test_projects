import simple_game, random

print("Хало!")
flag = None
while flag != "n":
    players = []
    num = simple_game.ask_number(
        question="Сколько игроков участвует? (2 - 5):", low=2, high=5)
    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randrange(100) + 1
        player = simple_game.Player(name, score)
        players.append(player)
        print(f"Игрок {name} появился! \n")
    print("\nВот результаты игры!\n")
    for player in players:
        print(player)
    flag = simple_game.ask_yes_no("\nХотитие сыграть еще? (y/n): ")
