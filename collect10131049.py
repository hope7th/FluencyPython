# coding=utf-8
import collections
from random import choice


Card = collections.namedtuple('Card',['rank','suit'])
suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDenk.ranks.index(card.rank)
    print rank_value
    return rank_value * len(suit_values) + suit_values[card.suit]

class FrenchDenk(object):
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    print ranks
    suits = 'spades diamonds clubs hearts'.split()
    print suits

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
        print self._cards

    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    deck = FrenchDenk()
    print len(deck)
    print deck[0]
    print deck[-1]
    print choice(deck)
    print choice(deck)
    print "slicing"
    print deck[:3]
    print deck[12:: 13]
    for card in deck:
        print card
    for card in reversed(deck):
        print card
    print Card('Q','hearts') in deck
    print 'sorted to here'
    for card in sorted(deck,key=spades_high):
        print card
    pass