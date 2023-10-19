from exercises_book.black_jack_and_whores.Cards_3.Card import Card
from exercises_book.black_jack_and_whores.Cards_3.Positionable_Card import PositionableCard
from exercises_book.black_jack_and_whores.Cards_3.Unprintable_Card import UnprintableCard


def main():
    card1 = Card("A", "d")
    card2 = UnprintableCard("A", "c")
    card3 = PositionableCard("A", "h")
    print(card1)
    print(card2)
    print(card3)
    card3.flip()
    print(card3)


if __name__ == '__main__':
    main()
