from exercises_book.black_jack_and_whores.Cards.Card import Card
from exercises_book.black_jack_and_whores.Cards.Hand import Hand


class Deck(Hand):
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        from random import shuffle
        shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Карт больше нет.")


deck1 = Deck()
print(deck1)
deck1.populate()
print(deck1)
deck1.shuffle()
print(len(deck1.cards))

my_hand = Hand()
other_hand = Hand()
hands = [my_hand, other_hand]
deck1.deal(hands, 5)

print(my_hand)
print(other_hand)

print(len(deck1.cards))
print(deck1)
deck1.clear()