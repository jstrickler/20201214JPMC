from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Fred")  # CardDeck.__init__(...)
print(d1)

# accessors & mutators (getters & setters)
print(d1.get_dealer())

# properties
print(d1.dealer)
d1.dealer = "Naomi"

print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
print()

d1.shuffle()
print(d1.cards)
print()
for i in range(5):
    print(d1.draw())
print()

print(str(d1))  # print calls str()
print(d1)
print(len(d1))
print(repr(d1))

d2 = CardDeck("Roderick")

x = d1 + d2

print(x, '\n')

j1 = JokerDeck('James')
j1.shuffle()
print(j1)
print(j1.cards, '\n')
print(j1.game_id())

print(JokerDeck.mro())
