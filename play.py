"""Classes and functions to handle the gameplay of Wiezen."""


class Card:
    """A card in a game of Wiezen."""

    suits = [
        "\u2666",
        "\u2665",
        "\u2663",
        "\u2660",
    ]  # ["Diamonds", "Hearts","Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(
        self,
        suit: int,
        rank: int,
        suit_fc: int = None,
        suit_trump: int = None,
    ):
        """Initialize a card.

        Args:
            suit (int): index of the suit of the card
            rank (int): index of the rank of the card
            suit_fc (int, optional): index of the suit of the first card played
            in the current round. Defaults to None.
            suit_trump (int, optional): index of the trump card in the current
            round. Defaults to None.
        """
        self.suit = suit
        self.rank = rank
        self.suit_fc = suit_fc  # Suit of first card played in current round
        self.suit_trump = suit_trump  # Suit of trump card in current round

    def __str__(self):
        """Return a human-readable string representation."""
        return f"{Card.suits[self.suit]} {Card.ranks[self.rank]}"

    def __lt__(self, other):
        """Override < operator."""
        # One of the two cards is a trump
        if self.suit == self.suit_trump and other.suit != self.suit_trump:
            return False
        if self.suit != self.suit_trump and other.suit == self.suit_trump:
            return True
        # Both cards are trump
        if self.suit == self.suit_trump and other.suit == self.suit_trump:
            return self.rank < other.rank
        # Neither card is trump, so depends on the first card that's played
        if self.suit == self.suit_fc and other.suit != self.suit_fc:
            return False
        if self.suit != self.suit_fc and other.suit == self.suit_fc:
            return True
        return self.rank < other.rank


def play_game():
    """Play a game of Wiezen."""
    # Test the Card class
    suit_trump = None
    suit_fc = 2
    card1 = Card(0, 1, suit_fc, suit_trump)
    card2 = Card(3, 0, suit_fc, suit_trump)
    print(card1 < card2)
    print(card1)
    print(card2)


if __name__ == "__main__":
    print("This is a module, not a script...")
    play_game()
    # exit(1)
