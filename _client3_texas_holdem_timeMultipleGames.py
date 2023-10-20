# Client 3. Assumes texas holdem
# Efficiency speed test. Runs the same poker game as Client2, but determines how fast the code ran
# Standard kept at 10 runs with 300 calls per run (3,000 games in total)
# More detailed comments about this code can be found in Client2
# Historical notes kept at bottom of code

import sys
sys.stdout.reconfigure(encoding='utf-8')

from cls_deck import Deck
from cls_player import Player
from cls_eval import EvalHand
from cls_scenario import ScenarioBuilder


def run_game():

    # Establish and build deck
    PickupDeck = Deck()
    PickupDeck.build()
    PickupDeck.shuffle()

    # Draw starting hand - Player 1
    Player1 = Player()
    Player1.pick_up_cards_from_deck(PickupDeck, 2)  

    # Draw starting hand - Player 2
    Player2 = Player()
    Player2.pick_up_cards_from_deck(PickupDeck, 2) 

    # Draw the 5 community cards
    CommunityCards = Player()
    CommunityCards.pick_up_cards_from_deck(PickupDeck, 5)  

    # Evaluate the Game
    EvalPlayer1 = EvalHand(Player1.players_hand, CommunityCards.players_hand)
    EvalPlayer2 = EvalHand(Player2.players_hand, CommunityCards.players_hand)

    # Determine the winner
    if EvalPlayer1.best_hand_score > EvalPlayer2.best_hand_score:
        return str("Player 1 Won")
    elif EvalPlayer2.best_hand_score > EvalPlayer1.best_hand_score:
        return str("Player 2 Won")
    else:
        return str("Neither Won")


if __name__ == '__main__':  
    import timeit

    t = timeit.Timer("run_game()", setup="from __main__ import run_game",)
    runs = 10
    calls_p_run = 300  
    results=t.repeat(runs, calls_p_run)

    maxV = max(results) * 1000
    minV = min(results) * 1000
    avgV = sum(results) / len(results) * 1000

    print(
        '\n \t =================================================================='
        '\n \t =============== SPEED TEST- RUN MULTIPLE SCENARIOS ==============='
        '\n \t =================================================================='
        '\n \t Total run time: {0:0.4} \t \t Total times ran: {1:0}'
        .format(sum(results), runs*calls_p_run)
    )

    print(
        '\n \t ====================================EXECUTION TIMES====================================='
        '\n \t  Cycles   | Calls    | First    | Last     | Fastest  | Slowest  | Spread   | Average   '
        '\n \t  {a:<8.5} | {b:<8.5} | {c:<8.5} | {d:<8.5} | {e:<8.5} | {f:<8.5} | {g:<8.5} | {h:<8.5}  '
        '\n                                                   '
        .format( a = format(runs, ' <2')
                ,b = format(calls_p_run, ' <2')
                ,c = format(results[0]*1000, ' <2')
                ,d = format(results[runs-1]*1000, ' <2')
                ,e = format(minV, ' <2')
                ,f = format(maxV, ' <2')
                ,g = format(maxV - minV, ' <2')
                ,h = format(avgV, ' <2')))

input("Press any key to exit")

# Note 03/03/2023
# current fastest speed times (three runs): 440.6 / 453.8 / 442.7
# then counted_cards.most_common() removed off every line
# times after removing the method (three runs) 379.6 / 387.8 / 376.1

# Note 17/10/2023
# Fastest: 457.0, Average: 463.0

