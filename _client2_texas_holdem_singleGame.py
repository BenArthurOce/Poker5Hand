# Client 2:
# Simulates a two player texas holdem poker game, where each player has 2 cards and are combined with 5 "community cards"
# Each player has their hand calculated with a score, and the better score wins

import sys
sys.stdout.reconfigure(encoding='utf-8')

from cls_deck import Deck
from cls_player import Player
from cls_eval import EvalHand

# Create the Deck() of 52 Card() objects
PickupDeck = Deck()
PickupDeck.build()
PickupDeck.shuffle()

# Creates a Player() object and removes two Card() objects from the Deck()
Player1 = Player()
Player1.pick_up_cards_from_deck(PickupDeck, 2)

# OR Replace the above code with the following code to draw certain Card() objects from the Deck()
# Player1.extract_card_from_deck(PickupDeck, 'A', '♥')
# Player1.extract_card_from_deck(PickupDeck, 'A', '♦')

# Creates a Player() object and removes two Card() objects from the Deck()
Player2 = Player()
Player2.pick_up_cards_from_deck(PickupDeck, 2)

# OR Replace the above code with the following code to draw certain Card() objects from the Deck()
# Player2.extract_card_from_deck(PickupDeck, '9', '♣')
# Player2.extract_card_from_deck(PickupDeck, '2', '♥')

#Create another Player() object which will represent the 5 "middle" community Card()s
CommunityCards = Player()
CommunityCards.pick_up_cards_from_deck(PickupDeck, 5)

# Print both Player() hands and the community cards to the terminal
Player1.print_hand_to_terminal()
CommunityCards.print_hand_to_terminal()
Player2.print_hand_to_terminal()

# Create a EvalHand() object which combines the Player() two Card()s against the five community Card()s and then determines the best hand
EvalPlayer1 = EvalHand(Player1.players_hand, CommunityCards.players_hand)
print("Score: {0:12}  Title: {1}".format(EvalPlayer1.best_hand_score, EvalPlayer1.best_hand_title))

# Create a EvalHand() object which combines the Player() two Card()s against the five community Card()s and then determines the best hand
EvalPlayer2 = EvalHand(Player2.players_hand, CommunityCards.players_hand)
print("Score: {0:12}  Title: {1}".format(EvalPlayer2.best_hand_score, EvalPlayer2.best_hand_title))

# Determine the winner
if EvalPlayer1.best_hand_score > EvalPlayer2.best_hand_score:
    print(str("Player 1 Won"))
elif EvalPlayer2.best_hand_score > EvalPlayer1.best_hand_score:
    print( str("Player 2 Won"))
else:
    print( str("Neither Won"))

# Print the remaining Card() objects that remain in the Deck() object
PickupDeck.print_contents_to_terminal()

input("Game complete - press any key to exit")
