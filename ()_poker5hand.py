import random
from collections import Counter


#========================================================
#=====================  Class  ==========================
#=====================  Card   ==========================
#========================================================


class Card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)

    def _getCard(self):
        return self.value, self.suit

    def _show_card(self,value, suit):

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


#========================================================
#=====================  Class  ==========================
#=====================  Deck   ==========================
#========================================================

class Deck():

    def __init__(self, name):
        self.name = name
        self.card_list = []

    # make a 52 list of all Card() objects
    #=================================================
    def _build(self):
        for s in ["♡", "♢", "♣", "♠"]:
            for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.card_list.append(Card(v, s))

    # obtain a tuple or list of current cards in deck
    #=================================================
    def _getContents(self,isTuple=True) -> list:
        list = []
        for card in self.card_list:
            if isTuple == True:
                list.append(Card._getCard(card))
            elif isTuple == False:
                card = Card._getCard(card)
                list.append(card[0]+card[1])
        return list
    
    # removes the first card in the deck. Returns details of the card drawn
    #=================================================
    def _removeTopCard(self):
        card_drawn = self.card_list[0]
        self.card_list.pop(0)
        return card_drawn

    # randomise deck
    #=================================================
    def _shuffle(self):
        self.shuffled_cards = random.shuffle(self.card_list)

    # will be used for discard deck
    #=================================================
    def _addCard(self, card_added):
        self.card_list.append(card_added)

    # print a table of all current cards in deck
    #=================================================
    def _printContents(self):
        # produce a standard deck of cards
        hrts = ['A♡', '2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡']
        dmds = ['A♢', '2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢']
        clbs = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
        spds = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']

        # produce the current deck of cards
        current_deck = self._getContents(False)

        # create a iter list of all cards, and remove cards not in the current game deck 
        standard_deck = [hrts,dmds,clbs,spds]
        for x in range(4):
            for y in range(13):
                if not standard_deck[x][y] in current_deck:
                    standard_deck[x][y] = "-"

        # print a table of current cards in deck
        table_of_current_cards = (
            '\n'
            '          │  A   │  2   │  3   │  4   │  5   │  6   │  7   │  8   │  9   │ 10   │  J   │  Q   │  K   │\n'
            '──────────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│──────│\n'
            ' Hearts   │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            ' Diamonds │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            ' Clubs    │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            ' Spades   │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │ {:4} │\n'
            '\n'
        ).format(*hrts, *dmds, *clbs, *spds)
        print(table_of_current_cards)


#========================================================
#=====================  Player  =========================
#=====================  Class ===========================
#========================================================

class Player():

    def __init__(self):
        self._players_hand = []


    # player picks up n amount of cards
    #=================================================
    def _picksUpCard(self,deck,number_drawn):
        for n in range(number_drawn):
            card_drawn = deck._removeTopCard()
            self._players_hand.append(card_drawn)


    # gets the tuple details of a single card in hand
    #=================================================
    def _returnSingleCardInHand(self, hand_pos):
        cards_in_hand = self._returnHandContents()
        return cards_in_hand[int(hand_pos-1)]


    # gets the tuple details of all cards in a players hand
    #=================================================
    def _returnHandContents(self):
        return [Card._getCard(card) for card in self._players_hand]


    # prints the current player hand in card format in the terminal
    #=================================================
    def _showHand(self):
        value_list = [x[0] for x in self._returnHandContents()]
        suit_list  = [y[1] for y in self._returnHandContents()]

        for card in self._players_hand:
            new_map = map(card._show_card, value_list, suit_list)
            for lines in zip(*new_map):
                print(*lines)
            break #we only want to loop once


    # player selects what cards to replace  ---  this is not a callable method. It should be called from _replaceCards (see below)
    #=================================================
    def _chooseWhatCardsToReplace(self):
        allowed_inputs = ["1","2","3","4","5"]
        selected_inputs = []
        n = int(fRestrict_User_Input(["0","1","2","3","4","5"],"Select number of cards to replace"))

        # loop for the number of cards user wants replaced
        for r in range(n):

            # user types 1-5 position of card to replace
            pos = fRestrict_User_Input(allowed_inputs,"Select Card to Replace")

            # after selecting the card position, remove it as an allowable option for future loops
            allowed_inputs.remove(pos)

            # add the position to a new list, which will pick out the cards to be removed
            selected_inputs.append(pos)

        return selected_inputs


    # player obtains new cards in the same positions of the old cards. Old cards discarded.
    #=================================================
    def _replaceCards(self):
        #user determines what cards to be removed
        selected_cards = self._chooseWhatCardsToReplace()

        for eachref in range(len(selected_cards)):
            card_pos = int(selected_cards[eachref])-1   #converts list entry to [list position] with base 0
            card_obj = self._players_hand[card_pos-0]   #obtains the card in players hand, based on above [position]

            # add its value to the discard deck
            discard_deck._addCard(card_obj)

            #draw new card, store it to the side
            self._picksUpCard(game_deck,1)          #adds a 6th card to position [5] in the players hand

            # add new card to hand by replacing the list position of the old card
            self._players_hand[int(card_pos)-0] = self._players_hand[5] 

            # remove the 6th card from position 5
            del self._players_hand[5]              


#========================================================
#=====================  Evaluating  =====================
#=====================  Single Card =====================
#========================================================

class EvalCard():
    def __init__(self, value, suit):
        # adjust card value and card suit value to become a numeric string that represents how strong the card is
        dictValue = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        dictSuit = {'♡':4, '♢':3, '♣':2, '♠':1}
        self.value = dictValue[value]
        self.suit = dictSuit[suit]

    # return a tuple of the cards adjusted value, and cards adjusted suit
    def _getCard(self):
        return self.value, self.suit


#========================================================
#=====================  Evaluating  =====================
#=====================     Hand     =====================
#========================================================

class EvalHand():
    def __init__(self, hand):

        # create and fill a list of EvalCard Class items
        self.evalHand = [EvalCard(value, suit) for value, suit in hand]

        # check and return if the hand has a straight
        self.is_there_straight = self._checkStraight()

        # check and return if the hand has a flush
        self.is_there_flush = self._checkFlush()

        # check for royal flush and straight flush
        self.is_there_royal_or_straight_flush = self._checkForRoyalStraightFlush()

        # check if there are any non straight/flush combinatons
        self.is_there_other = self._checkOtherCombinations()


    # transform the EvalHand() class list into a list containing multiple tupples
    #===================================================================================
    def _getTuple(self):
        return [a._getCard() for a in self.evalHand]


    # sort every tupple by the cards adjust value (from EvalCard()), numbers are increasing order
    #===================================================================================
    def _arrange(self):
        a = sorted(self._getTuple())
        return a


    # check if the hand has a STRAIGHT
    #===================================================================================
    def _checkStraight(self):

        # get the tuple of the hand, which is already sorted based on card values
        hand = self._arrange()

        # get a list of values
        list_of_values = [a[0] for a in hand]

        # cycle first 4 cards. Does the value plusOne equal the next list element? If not, return false
        for a in range(len(hand)-1):
            if list_of_values[a] +1 == list_of_values[a+1]:
                continue
            else:
                return ""
        return "Straight"


    # check if the hand has a FLUSH
    #===================================================================================
    def _checkFlush(self):

        # get the tuple of the hand, sorted for value of card values
        hand = self._arrange()

        # obtain the tupple of the first card in hand, and get its suit and value
        first_card_in_hand = hand[0]
        first_value, first_suit = first_card_in_hand

        # get a list of suits
        list_of_suits = [a[1] for a in hand]

        # check the value of the suit in the first card, if there are 5 of those suits, there is a flush
        if list_of_suits.count(first_suit) == 5:
            return "Flush"
        else:
            return ""


    # check for Royal Flush, Check for Straight Flush (Royal Flush needs to be done)
    #===================================================================================
    def _checkForRoyalStraightFlush(self):
        
        # royal flush still needs to be completed


        # if the hand contains a straight and a flush, return StraightFlush
        if self.is_there_straight == "Straight" and self.is_there_flush == "Flush":
            return "Straight Flush"
        else:
            return ""


    # check for other combinations (Non Straight, Non Flush)
    #===================================================================================
    def _checkOtherCombinations(self):

        # get the tuple of the hand, which is already sorted based on card values
        hand = self._arrange()

        # get a list of values
        list_of_values = [a[0] for a in hand]

        # run counter function 
        counted_cards = Counter(list_of_values)
        two_most_common, count = zip(*counted_cards.most_common(2))

        dict = {
            (2, 1): "One Pair",
            (3, 1): "Three of a Kind",
            (4, 1): "Four of a Kind",
            (2, 2): "Two Pairs",
            (3, 2): "Full House",
        }

        result = dict.get(count,"No")
        return result


    # check for highest value card
    #===================================================================================
    def _getHighestCard(self):

        # get the tuple of the hand, which is already sorted based on card values
        hand = self._arrange()

        # get a list of values
        list_of_values = [a[0] for a in hand]

        # get the last element of list
        last_element = list_of_values[-1]

        # reverse back to card values (14=A, 13=K, 12=Q etc)
        dictValue = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13:'King', 14:'Ace'}
        stringValue = dictValue[last_element]

        return "High Card: " + str(stringValue)


    # Evaluate Hand
    #===================================================================================
    def _evaluateHand(self):
        if self.is_there_royal_or_straight_flush == "Straight Flush":
            return "Straight Flush"
        elif self.is_there_other == "Four of a Kind":
            return "Four of a Kind"
        elif self.is_there_other == "Full House":
            return "Full House"
        elif self.is_there_flush == "Flush":
            return "Flush"
        elif self.is_there_straight == "Straight":
            return "Straight"
        elif self.is_there_other == "Three of a Kind":
            return "Three of a Kind"
        elif self.is_there_other == "Two Pairs":
            return "Two Pairs"
        elif self.is_there_other == "One Pair":
            return "One Pair"
        else:
            return self._getHighestCard()


# function that restrics the user inupt (is used for the card replacement function)
#===================================================================================
def fRestrict_User_Input(user_can_only_type:list, input_message:str):
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



#========================================================
#=====================  Game   ==========================
#=====================  Start  ==========================
#========================================================


# create game deck and discard deck
game_deck = Deck("Game")
discard_deck = Deck("Discard")
game_deck._build()
game_deck._shuffle()


# Establish Players.
Player1 = Player()
Player2 = Player()

# draw starting hand
Player1._picksUpCard(game_deck,5)
Player2._picksUpCard(game_deck,0)

# Player One to replace cards
Player1._showHand()
Player1._replaceCards()


# display ending hand tuple, display player hand and display result
print()

print(Player1._returnHandContents())
Player1._showHand()

print()

eval_hand = EvalHand(Player1._returnHandContents())
print(eval_hand._evaluateHand())


# option for user to display what cards remain the game game deck
user_input = fRestrict_User_Input(['y','n'],"display ending deck contents? y/n")
if user_input == "y":
    game_deck._printContents()
elif user_input == "n":
    pass



# discard_deck._printContents()


# testing custom cards
flush_test = [('9', '♠'), ('7', '♠'), ('10', '♠'), ('4', '♠'), ('2', '♠')]
straight_test = [('10', '♣'), ('9', '♠'), ('J', '♠'), ('K', '♢'), ('Q', '♣')]
straightflush_test = [('10', '♠'), ('9', '♠'), ('J', '♠'), ('8', '♠'), ('7', '♠')]
fullhouse_test = [('10', '♠'), ('10', '♡'), ('J', '♠'), ('J', '♡'), ('J', '♢')]
fourkind_test = [('2', '♣'), ('3', '♠'), ('2', '♠'), ('2', '♡'), ('2', '♢')]
threekind_test = [('2', '♣'), ('3', '♠'), ('2', '♠'), ('2', '♡'), ('A', '♢')]


player_hand = [x for x in Player1._returnHandContents()]

