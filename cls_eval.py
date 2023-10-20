from collections import Counter
import itertools
from cls_card import Card

class EvalHand:
    def __init__(self, player_cards, community_cards):
        self.all_card_combinations = itertools.combinations(player_cards + community_cards, 5)
        self.dict_each_hand_score = self.calculate_each_score()
        self.best_hand_contents, self.best_hand_title, self.best_hand_score = self.get_best_hand_information()

    def calculate_each_score(self) -> dict:
        """ Creates all possible 5 card hands from the 7 cards provided
            Each hand is given a score and a title (ie: Full house) and stored in a dictionary."""
        dict_all_scores = {}

        for each_five_card_combination in self.all_card_combinations:
            hand_tuple = sorted([(card.value, card.suitNum) for card in each_five_card_combination], reverse=True)
            each_hand_title, each_hand_score = self.evaluate_hand(hand_tuple)
            dict_all_scores[each_hand_score] = {'name': each_hand_title, 'cards': each_five_card_combination}

        return dict_all_scores


    def get_best_hand_information(self) -> tuple:
        """ Reads the dictionary of all scores, returns the highest score.
            Then reads into the score (dictionary key) to find information about the hand that generated that score/title"""
        best_score = max(self.dict_each_hand_score)
        return self.dict_each_hand_score[best_score]['cards'], self.dict_each_hand_score[best_score]['name'],  best_score


    def evaluate_hand(self, evaluated_hand):
        """Using Counter Library, return the score and title of a 5 card poker hand"""

        list_of_values = [a[0] for a in evaluated_hand]
        list_of_suits = [a[1] for a in evaluated_hand]
        counted_cards = Counter(list_of_values)
        two_most_common, countV = zip(*counted_cards.most_common(2))


        dict_count_multiple = {
            (2, 1): "One Pair",
            (3, 1): "Three of a Kind",
            (4, 1): "Four of a Kind",
            (2, 2): "Two Pairs",
            (3, 2): "Full House",
            (1, 1): "High Card"
        }
        other_hand_result = dict_count_multiple.get(countV,"ERROR")
       
        # if there are no pairs, trips etc, check for straights/flushes.
        is_straight_found = False if other_hand_result == "High Card" else (max(counted_cards.keys()) - min(counted_cards.keys()) + 1) == 5 and len(counted_cards.keys()) == 5

        # this code needs to be fixed for locating a flush
        is_flush_found = False if other_hand_result == "High Card" else max(counted_cards.values()) == 5 and len(list_of_suits) == 5

        # adjust straight if low card Ace
        if is_straight_found and list_of_values == [2, 3, 4, 5, 14]:
            list_of_values = [1, 2, 3, 4, 5]

        # generates a list of most important cards in hand, the front of list being most important
        most_common_cards = counted_cards.most_common()
        high_card = most_common_cards[0][0]

        #Using the Straight/Flush checks and the pair count dictionary, determine the type of hand and calculate its score
        match (is_straight_found, is_flush_found, other_hand_result):
            case (True, True, "High Card"):
                hand_name, hand_score = "(A) - Royal Flush", 90000000000 if high_card == 14 else "", 0
                     
            case (True, True, "High Card"):
                hand_name = "(B) - Straight Flush"
                hand_score = 80000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = highest value in flush
                hand_score += most_common_cards[1][0] * 1000000     #second element = second highest value in flush
                hand_score += most_common_cards[2][0] * 10000       #third element = middle value in flush
                hand_score += most_common_cards[3][0] * 100         #fourth element = second lowest value in flush
                hand_score += most_common_cards[4][0] * 1           #fifth element = lowest value in flush 
                

            case (False, False, "Four of a Kind"):
                hand_name = "(C) - Four of a Kind"
                hand_score = 70000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = value of quad
                hand_score += most_common_cards[1][0] * 1000000     #second element = value of kicker
                
            
            case (False, False, "Full House"):
                hand_name = "(D) - Full House"
                hand_score = 60000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element - value of the trio
                hand_score += most_common_cards[1][0] * 1000000     #second element - value of the duo
                

            case (False, True, "High Card"):
                hand_name = "(E) - Flush"
                hand_score = 50000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = highest value in flush
                hand_score += most_common_cards[1][0] * 1000000     #second element = second highest value in flush
                hand_score += most_common_cards[2][0] * 10000       #third element = middle value in flush
                hand_score += most_common_cards[3][0] * 100         #fourth element = second lowest value in flush
                hand_score += most_common_cards[4][0] * 1           #fifth element = lowest value in flush
                
            
            case (True, False, "High Card"):
                hand_name = "(F) - Straight"
                hand_score = 40000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = highest value in straight
                hand_score += most_common_cards[1][0] * 1000000     #second element = second highest value in straight
                hand_score += most_common_cards[2][0] * 10000       #third element = middle value in straight
                hand_score += most_common_cards[3][0] * 100         #fourth element = second lowest value in straight
                hand_score += most_common_cards[4][0] * 1           #fifth element = lowest value in straight
                
            
            case (False, False, "Three of a Kind"):
                hand_name = "(G) - Three of a Kind"
                hand_score = 30000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = value of trio
                hand_score += most_common_cards[2][0] * 1000000     #second element = highest single card
                hand_score += most_common_cards[1][0] * 10000       #third element = second highest single card
                

            case (False, False, "Two Pairs"):
                hand_name = "(H) - Two Pairs"
                hand_score = 20000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = value of higher pair
                hand_score += most_common_cards[1][0] * 1000000     #second element = value of lower pair
                hand_score += most_common_cards[2][0] * 10000       #third element = value of kicker
                

            case (False, False, "One Pair"):
                hand_name = "(I) - One Pair"
                hand_score = 10000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = value of pair
                hand_score += most_common_cards[1][0] * 1000000     #second element = kicker (highest)
                hand_score += most_common_cards[2][0] * 10000       #third element = kicker (second highest)
                hand_score += most_common_cards[3][0] * 100         #fourth element = kicker (third highest)
                

            case (False, False, "High Card"):
                hand_name = "(J) - High Card: " + str(high_card)
                hand_score = 00000000000
                hand_score += most_common_cards[0][0] * 100000000   #first element = high card
                hand_score += most_common_cards[1][0] * 1000000
                hand_score += most_common_cards[2][0] * 10000
                hand_score += most_common_cards[3][0] * 100
                hand_score += most_common_cards[4][0] * 1
                
            
            case _:
                print("You shoudn't have gotten here, I'm exiting this code")
                exit()

        return hand_name, hand_score



