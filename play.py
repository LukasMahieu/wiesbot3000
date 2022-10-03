"""Classes and functions to handle the gameplay of Wiezen."""
import random

# Add to Round class
# # One of the two cards is a trump
# if self.suit == self.suit_trump and other.suit != self.suit_trump:
#     return False
# if self.suit != self.suit_trump and other.suit == self.suit_trump:
#     return True
# # Both cards are trump
# if self.suit == self.suit_trump and other.suit == self.suit_trump:
#     return self.rank < other.rank
# # Neither card is trump, so depends on the first card that's played
# if self.suit == self.suit_fc and other.suit != self.suit_fc:
#     return False
# if self.suit != self.suit_fc and other.suit == self.suit_fc:
#     return True
# return self.rank < other.rank


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
    ):
        """Initialize a card.

        Args:
            suit (int): index of the suit of the card
            rank (int): index of the rank of the card
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return a human-readable string representation."""
        return f"{Card.suits[self.suit]} {Card.ranks[self.rank]}"

    def __lt__(self, other):
        """Override < operator."""
        return self.rank < other.rank

    def __gt__(self, other):
        """Override > operator."""
        return self.rank > other.rank

    def __eq__(self, other):
        """Override == operator."""
        return self.rank == other.rank


class Deck:
    """A deck of cards in a game of Wiezen."""

    def __init__(self):
        """Initialize a new deck and shuffle it."""
        self.cards = []
        self.reset()
        self.random_shuffle()

    def __len__(self):
        """Return the number of cards in the deck."""
        return len(self.cards)

    def __str__(self):
        """Return a human-readable string representation."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ", ".join(res)

    def random_shuffle(self):
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def cut(self):
        """Cut the deck in two."""
        cutpoint = random.randint(0, len(self.cards))
        self.cards = self.cards[cutpoint:] + self.cards[:cutpoint]

    def reset(self):
        """Reset the deck to a full deck of cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card(suit, rank))

    def deal(self, n_cards):
        """Deal n_cards from the deck."""
        cards = []
        for _ in range(n_cards):
            cards.append(self.cards.pop())
        return cards

    def deal_all(self):
        """Deal all cards from the deck."""
        return self.deal(len(self.cards))


class Player:  # pylint: disable=too-few-public-methods
    """A player in a game of Wiezen."""

    def __init__(self, name):
        """Create a player with a name."""
        self.name = name
        self.hand = []

    def __str__(self):
        """Return the name of the player."""
        return self.name


def play_game():
    """Play a game of Wiezen."""
    # Test the Player class
    player = Player("Player 1")
    print(player)


if __name__ == "__main__":
    print("This is a module, not a script...")
    play_game()
    # exit(1)
