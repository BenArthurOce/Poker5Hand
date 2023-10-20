# Client 1:
# Simulates a single person replacing cards from a 5 card hand
# Then returns the type of hand (ie: one pair) and then a grid of all the remaining cards in deck

import sys
sys.stdout.reconfigure(encoding='utf-8')

from cls_deck import Deck
from cls_player import Player
from cls_eval import EvalHand

# Create the Deck() of 52 Card() objects
PickupDeck = Deck()
PickupDeck.build()
PickupDeck.shuffle()

# Create an empty Deck() object that discarded Card()s can go into
DiscardDeck = Deck()

# Create a Player() and have them draw 5 Card()s
Player1 = Player()
Player1.pick_up_cards_from_deck(PickupDeck, 5)

# Player() selects what Card()s to discard and draws new Card()s from the Deck()
Player1.print_hand_to_terminal()
cards_to_replace = Player1.choose_what_cards_to_replace()
Player1.replace_cards(cards_to_replace, PickupDeck, DiscardDeck)

# Reprint the new hand to the terminal
Player1.print_hand_to_terminal()

# Create a EvalHand() object which contains only the contents of Player() hand.
# EvalHand() automatically calculates Player()s hand and determines result
Player1Eval = EvalHand(Player1.players_hand,[])

# Print the calculated result to terminal
print(Player1Eval.best_hand_title)

# Print the remaining Card() objects that remain in the Deck() object
PickupDeck.print_contents_to_terminal()

input("Game complete - press any key to exit")