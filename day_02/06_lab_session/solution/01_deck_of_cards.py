import random


def create_deck() -> list[str]:
    """Return a list of 52 strings containing a standard deck"""
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [f'{rank}{suit}' for suit in suits for rank in ranks]


def draw_top(deck: list[str], count: int = 1) -> list[str]:
    """Remove and return count cards from the start of the deck"""
    drawn = deck[:count]
    del deck[:count]
    return drawn


def draw_bottom(deck: list[str], count: int = 1) -> list[str]:
    """Remove and return count cards from the end of the deck"""
    drawn = deck[-count:]
    del deck[-count:]
    return drawn


def draw_random(deck: list[str], count: int = 1) -> list[str]:
    """Remove and return count random cards from the deck"""
    drawn = random.sample(deck, min(count, len(deck)))
    for card in drawn:
        deck.remove(card)
    return drawn


def show(deck):
    """Print all cards in deck"""
    print('Deck:', ', '.join(deck))


def add_top(deck: list[str], other: list[str]):
    """Add cards in other to the first parts of deck"""
    deck[:0] = other


def add_bottom(deck: list[str], other: list[str]):
    """Add cards in other to the last parts of deck"""
    deck.extend(other)


def add_random(deck: list[str], other: list[str]):
    """Add cards in other randomly to deck"""
    for card in other:
        idx = random.randint(0, len(deck))
        deck.insert(idx, card)


def load(filename: str) -> list[str]:
    """Returns a list of cards loaded from a file"""
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def save(deck: list[str], filename: str):
    """Saves a list of cards into a file (retrievable with load)"""
    with open(filename, 'w') as f:
        for card in deck:
            f.write(card + '\n')
