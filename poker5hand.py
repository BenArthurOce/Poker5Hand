import random

class Card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)

    def _getCard(self):
        return self.value, self.suit

    def _show_card(self,value, suit):

        #suit = self.value
        #value = self.value
        suit = suit
        value = value
        return (
            '┌─────────┐\n'
            '│{}       │\n'
            '│         │\n'
            '│         │\n'
            '│    {}   │\n'
            '│         │\n'
            '│         │\n'
            '│       {}│\n'
            '└─────────┘'
        ).format(
            format(value, ' <2'),
            format(suit, ' <2'),
            format(value, ' >2')
        ).splitlines()


class Deck():

    def __init__(self, name):
        self.name = name
        self.card_list = []


    def _build(self):
        for s in ["♡", "♢", "♣", "♠"]:
            for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.card_list.append(Card(v, s))

    # prints a list of all current cards
    def _auditContents(self):
        for card in self.card_list:
            print(Card._getCard(card))
    
    def _returnFullList(self):
        list = []
        for card in self.card_list:
            list.append(Card._getCard(card))
            return list

    # prints the number of cards remaining in the deck
    def _count(self):
        print(len(self.card_list))

    # removes the first card in the deck. Returns details of the card drawn
    def _removeTopCard(self):
        card_drawn = self.card_list[0]
        self.card_list.pop(0)
        return card_drawn

    # randomise deck
    def _shuffle(self):
        self.shuffled_cards = random.shuffle(self.card_list)

    # pass - will be used for discard deck
    def _addCard(self, card_added):
        self.card_list.append(card_added)


class Player():

    def __init__(self, name):
        self.name = name
        self._players_hand = []

    # player picks up n amount of cards
    def _picksUpCard(self,deck,number_drawn):
        for n in range(number_drawn):
            card_drawn = deck._removeTopCard()
            self._players_hand.append(card_drawn)

    # prints number of cards in players hand
    def _countCards(self):
        print(len(self._players_hand))

    # gets the tupple details of a single card in hand
    def _returnSingleCardInHand(self, hand_pos):
        cards_in_hand = self._returnHandContents()
        return cards_in_hand[int(hand_pos-1)]

    # prints a single card to the terminal
    def _auditSingleCardInHand(self, hand_pos):
        cards_in_hand = [str(a) for a in self._players_hand]
        print(cards_in_hand[int(hand_pos-1)])

    # gets the tupple details of all cards in a players hand
    def _returnHandContents(self):
        return [Card._getCard(card) for card in self._players_hand]

    # prints each card to the terminal
    def _auditHandContents(self):
        list1 = [str(a) for a in self._players_hand]
        print(list1)

    # prints the current player hand
    def _showHand(self):
        value_list = [x[0] for x in self._returnHandContents()]
        suit_list  = [y[1] for y in self._returnHandContents()]

        for card in self._players_hand:
            new_map = map(card._show_card, value_list, suit_list)
            for lines in zip(*new_map):
                print(*lines)
            break #we only want to loop once



    # player selects what cards to replace
    # referenced from code below (_replaceCards)
    def _chooseWhatCardsToReplace(self):
        allowed_inputs = ["1","2","3","4","5"]
        selected_inputs = []
        n = int(fRestrict_User_Input(["1","2","3","4","5"],"Select number of cards to replace"))

        for r in range(n):

            val = fRestrict_User_Input(allowed_inputs,"Select Card to Replace")

            # after selecting that item, remove from list
            allowed_inputs.remove(val)

            # add card number to list of cards selected to be removed
            idx = ["1","2","3","4","5"].index(val) #get positional index
            selected_inputs.append(int(idx+1))

        return selected_inputs

    # player obtains new cards in the same positions of the old cards. Old cards discarded.
    def _replaceCards(self):
        #user determines what cards to be removed
        selected_cards = self._chooseWhatCardsToReplace()

        for eachref in range(len(selected_cards)):
            #get card details
            card_ref = selected_cards[eachref]
            card_got = self._players_hand[card_ref-1]

            # add its value to the discard deck
            discard_deck._addCard(card_got)

            #draw new card, store it to the side
            self._picksUpCard(game_deck,1)          #adds a 6th card to position 5

            # add new card to hand by replacing the list position of the old card
            self._players_hand[int(card_ref)-1] = self._players_hand[5] 

            #removes the 6th card from position 5
            del self._players_hand[5]              


def fRestrict_User_Input(user_can_only_type, input_message):
    list_upper_case = [each_string.upper() for each_string in user_can_only_type]
    while True:
        try:
            user_input = input(input_message + ": ")
            if str(user_input).upper() in list_upper_case:
                return user_input
            raise ValueError()
        except ValueError:
            print("    Error: You are required to enter one of the following: {}".format(user_can_only_type))
            print("    Please try again\n")



# create game deck and discard deck
game_deck = Deck("Game")
discard_deck = Deck("Discard")



game_deck._build()
game_deck._shuffle()


# Establish Players. Don't really need names
Player1 = Player(name="Ben")
Player2 = Player(name="Fred")

# draw starting hand
Player1._picksUpCard(game_deck,9)
Player2._picksUpCard(game_deck,10)

game_deck._count()

Player1._showHand()

print(game_deck.card_list)
print(Player1._auditHandContents())

#game_deck._auditContents()



# # check value of cards DEBUG
# Player1._countCards()
# Player2._countCards()
# game_deck._count()
# discard_deck._count()

# # show hand
# Player1._showHand()

# # replace hand
# Player1._replaceCards()
# Player1._showHand()

# # debug
# discard_deck._count()
# discard_deck._auditContents()















