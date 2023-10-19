from exercises_book.black_jack_and_whores.Cards_3.Card import Card


class UnprintableCard(Card):
    def __str__(self):
        return "<нельзя напечатать>"
