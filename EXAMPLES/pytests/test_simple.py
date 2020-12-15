#!/usr/bin/env python
# from carddeck import CardDeck
import pytest

@pytest.mark.xfail
def test_two_plus_two_equals_four():  # <1>
    assert 2 + 2 == 5   #  <2>

def test_hello():
    assert True

# def test_card_deck_has_52_cards():
#     d = CardDeck("Test User")
#     assert len(d) == 52
#
