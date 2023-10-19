from exercises_book.black_jack_and_whores.Cards.Card import Card


class Hand(object):
    """Набор игральных карт у игрока"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        other_hand.add(card)
        self.cards.remove(card)


# card1 = Card(rank="A", suit="c")
# card2 = Card(rank="2", suit="c")
# card3 = Card(rank="3", suit="c")
# card4 = Card(rank="4", suit="c")
# print("Вывожу на экран обьек-карту:")
# print(card1)
# print(card2)
# print(card3)
# print(card4)
# hand = Hand()
# other_hand = Hand()
# hand.add(card1)
# hand.add(card2)
# hand.add(card3)
# hand.add(card4)
# print(hand)
# hand.give(card3, other_hand)
# print(hand)
# print(other_hand)
# hand.clear()
# other_hand.clear()
# print(hand)
# print(other_hand)
