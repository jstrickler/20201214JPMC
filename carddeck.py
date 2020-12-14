import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):  #  __str__()
        return f"Card({self.rank},{self.suit})"

    def __str__(self):
        return f"{self.rank}-{self.suit}"

class CardDeck:   #  inherits from 'object
    # class variables
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer  # copy to private attribute
        self._make_deck()

    def get_dealer(self):  # public getter method
        return self._dealer

    def _make_deck(self):
        self._cards = []   # empty list
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer): # SETTER property
        if isinstance(dealer, str):
            self._dealer =dealer
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        my_class = type(self)
        class_name = my_class.__name__  # name of class
        return f"{class_name}({self.dealer}, {len(self)})"

    def __repr__(self):
        my_class = type(self)
        my_name = my_class.__name__  # name of class
        return f"""{my_name}("{self.dealer}")"""

    def __len__(self):
        return len(self._cards)

    def __add__(self, other):
        my_type = type(self)
        new_deck = my_type(self.dealer)
        new_deck._cards = self.cards + other.cards
        return new_deck
