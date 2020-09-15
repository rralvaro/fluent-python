import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__=='__main__':
    deck = FrenchDeck()
    print (deck[0])

    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    print(deck[:3])
    print(deck[5:9])

    for card in reversed(deck[:5]):
        print (card)

    print(Card('Q','hearts') in deck)
    print(Card("O",'hearts') in deck)

    # Ordenamos lo que mas vale son los ases y dentro de etsto el de espadas
    suit_values= dict(spades=3,hearts=2,diamonds=1,clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value*len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)
        

