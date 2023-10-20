# Client 4. Assumes texas holdem
# uses a ScenarioBuilder() class to run the same function on repeat
# in line 100~, input: "test_strength" or "run_game". This will run 3,000 games and tell you either: 
#   the chance of a certain hand coming up (test_strength)
#   the odds of player 1 or player 2 winning (run_game)

import sys
sys.stdout.reconfigure(encoding='utf-8')

from cls_deck import Deck
from cls_player import Player
from cls_eval import EvalHand
from cls_scenario import ScenarioBuilder

# How many times to run the code
times_to_run = 3000


# OPTION 1:
# Determine Outcome from a hand
def test_strength():

    # Establish and build deck
    PickupDeck = Deck()
    PickupDeck.build()
    PickupDeck.shuffle()  

    # Establish Player() and draw two particular Card() objects
    Player1 = Player()
    Player1.extract_card_from_deck(PickupDeck, '10', '♣')
    Player1.extract_card_from_deck(PickupDeck, '3', '♣')

    #Draw the 5 community Card() objects
    CommunityCards = Player()
    CommunityCards.pick_up_cards_from_deck(PickupDeck, 5)  

    #Evaluate the Game
    EvalPlayer1 = EvalHand(Player1.players_hand, CommunityCards.players_hand)

    return str(EvalPlayer1.best_hand_title)

# OPTION 2:
# Determine Player() more likely to win
def run_game():

    # Establish and build deck
    PickupDeck = Deck()
    PickupDeck.build()
    PickupDeck.shuffle()

    #Draw starting hand - Player 1
    Player1 = Player()
    Player1.extract_card_from_deck(PickupDeck, 'A', '♥')
    Player1.extract_card_from_deck(PickupDeck, 'A', '♦')

    #Draw starting hand - Player 2
    Player2 = Player()
    Player2.extract_card_from_deck(PickupDeck, '9', '♣')
    Player2.extract_card_from_deck(PickupDeck, '2', '♥')

    # Draw the 5 community cards
    CommunityCards = Player()
    CommunityCards.pick_up_cards_from_deck(PickupDeck, 5)  

    # Evaluate the Game
    EvalPlayer1 = EvalHand(Player1.players_hand, CommunityCards.players_hand)
    EvalPlayer2 = EvalHand(Player2.players_hand, CommunityCards.players_hand)

    # Determine Winner
    if EvalPlayer1.best_hand_score > EvalPlayer2.best_hand_score:
        return str("Player 1 Won")
    elif EvalPlayer2.best_hand_score > EvalPlayer1.best_hand_score:
        return str("Player 2 Won")
    else:
        return str("Neither Won")


# MAIN CODE
#===================
NewScenario = ScenarioBuilder(
                                 times_to_run_method = times_to_run
                                ,scenario_method = run_game     # Change this to run different functions
                             )

NewScenario.collect_scenario_data()
NewScenario.print_results_to_terminal_with_PANDAS()

input("Press any key to exit")