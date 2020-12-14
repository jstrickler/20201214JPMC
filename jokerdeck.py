from carddeck import CardDeck, Card


class Game:
    def game_id(self):
        return "I am a game"


class JokerDeck(CardDeck, Game):

    def _make_deck(self):
        super()._make_deck()  # call in parent class
        for i in 1, 2:
            joker = Card(i, 'Joker')
            self._cards.append(joker)
