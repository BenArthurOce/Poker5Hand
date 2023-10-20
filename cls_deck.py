import random
from cls_card import Card

class Deck():

    def __init__(self):
        self.card_list = []


    def build(self) -> None:
        """Creates the Deck() list, contains 52 Card() objects with information about their rank, value, display, suit"""
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        displays = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ["♥", "♦", "♣", "♠"]
        suitNums = [1, 2, 3, 4]
        self.card_list = [Card(rank, value, display, suit, suitNum) for rank, value, display in zip(ranks,values,displays) for suit, suitNum in zip(suits,suitNums)]


    def locate_certain_card(self, card_disp:str, card_suit:str) -> int:
        """Using the Card() Display and Card() suit icon, locates where that card is in the deck"""
        current_deck = [(str(each_card.display)+str(each_card.suit)) for each_card in self.card_list]
        return current_deck.index(card_disp + card_suit)


    def remove_card_based_on_index(self, index:int) -> Card:
        """Removes a Card() Object from the deck list, based on its index position. Returns the Card() object that was removed"""
        return self.card_list.pop(index)


    def remove_top_card(self) -> Card:
        """Removes the first Card() object from Deck(). Returns the card drawn."""
        return self.card_list.pop(0)


    def add_card(self, card_added:Card) -> None:
        """Adds a nominated card to the deck"""
        self.card_list.append(card_added)


    def shuffle(self) -> None:
        "Randomise/Shuffle the Card() objects in Deck()"
        self.shuffled_cards = random.shuffle(self.card_list)


    def print_contents_to_terminal(self) -> None:
        """Displays remaining Card() objects left in Deck() to terminal"""

        # produce a standard deck of cards
        hrts = ['A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥']
        dmds = ['A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
        clbs = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
        spds = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
        standard_deck = [hrts,dmds,clbs,spds]

        # produce the current deck of cards
        current_deck = [(str(each_card.display)+str(each_card.suit)) for each_card in self.card_list]

        # create a iter list of all cards, and remove cards not in the current game deck        
        for x in range(4):
            for y in range(13):
                if not standard_deck[x][y] in current_deck:
                    standard_deck[x][y] = "-"

        # print a table of current cards in deck
        table_of_current_cards = (
            '\n'
            'Remaining Cards in Deck:                                                                              \n'
            '                                                                                                      \n'
            '          │  A   │  2   │  3   │  4   │  5   │  6   │  7   │  8   │  9   │ 10   │  J   │  Q   │  K   │\n'
            '──────────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│\n'
            ' Hearts   │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            ' Diamonds │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            ' Clubs    │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            ' Spades   │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            '\n'
        ).format(*hrts, *dmds, *clbs, *spds)
        print(table_of_current_cards)