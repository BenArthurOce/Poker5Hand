from cls_card import Card
from cls_deck import Deck

class Player():
    def __init__(self):
        self.players_hand = []


    def pick_up_cards_from_deck(self, deck:Deck, number_drawn:int) -> None:
        """Removes n Card() objects from the top of nominated Deck(). The Card() objects are played in the player hand."""
        for n in range(number_drawn):
            # card_drawn = deck.remove_top_card()
            # self.players_hand.append(card_drawn)
            self.players_hand.append(deck.remove_top_card())


    def extract_card_from_deck(self, deck:Deck, card_rank:str, card_suit:str) -> None:
        """Removes a Card() object from nominated Deck() and put into Player() hand. The Card() is based on the details of the Card() object provided."""
        card_index = deck.locate_certain_card(card_rank, card_suit)
        card_drawn = deck.remove_card_based_on_index(card_index)
        self.players_hand.append(card_drawn)


    def put_down_card_onto_deck(self, deck:Deck, card_to_put_down:Card) -> None:
        """Removes a single nominated Card() object from Player() hand and puts it into a nominated Deck()."""
        deck.add_card(card_to_put_down)
        card_pos = self.return_index_pos_in_hand(card_to_put_down)
        del self.players_hand[card_pos] 


    def return_single_card_object(self, n:int) -> Card:
        """Returns the Card() object that is in 'n' position of Player() hand. This is Base 1. Not Base 0"""
        return self.players_hand[int(n)-1]


    def return_index_pos_in_hand(self, card:Card) -> int:
        """Returns the index position of a Card() object in the Player() hand."""
        return self.players_hand.index(card)


    def print_hand_to_terminal(self) -> None:
        """Prints contents of players hand to terminal. The display is in card format. See Card() for design."""
        hand_contents_list = [Card.return_tuple(card) for card in self.players_hand]
        rank_list = [x[0] for x in hand_contents_list]
        suit_list  = [y[1] for y in hand_contents_list]

        for card in self.players_hand:
            new_map = map(card.print_for_terminal, rank_list, suit_list)
            for lines in zip(*new_map):
                print(*lines)
            break #we only want to loop once


    def choose_what_cards_to_replace(self) -> list:
        """Method for letting the user nominate the number of Card() objects to replace, and then picks which Card() objects to replace. BASE 1"""

        # constructs a list of numbers that the user is restricted to input
        count_of_hand_cards = len(self.players_hand)
        card_input_range = [*range(count_of_hand_cards+1)]

        # user types in how many cards they want to replace. User is restricted on what to input based from "card_input_range"
        num_to_replace = int(self.restrict_user_input(
                                        user_can_only_type = card_input_range,
                                        input_message = "Select Number of Cards to Replace: "
                                        ))

        # this is a list of the card positions the user is allowed to choose from. 
        # This will be reduced each time a card position is chosen, so the user cannot remove the same cards
        allowed_inputs = [*range(1, count_of_hand_cards+1)]
        selected_inputs = []

        # internet code for ordinal numbers (StackoverFlow 9647202)
        ordinal_function = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        ordinal_list = [ordinal_function(n) for n in range(1,32)]

        # loop for the number of cards user wants replaced
        for r in range(num_to_replace):

            # user inputs a card position. The card in this position will be replaced. Only allowed to type in values from the "allowed_inputs" list
            pos = int(self.restrict_user_input(
                                        user_can_only_type = allowed_inputs,
                                        input_message = "Select {0} Card to Replace: ".format(ordinal_list[r])
                                        ))

            # after selecting the card position, remove it as an allowable option for future loops
            allowed_inputs.remove(pos)

            # add the user input to a new list, which will pick out the cards to be removed for the replace_cards() method
            selected_inputs.append(pos)

        return selected_inputs


    def restrict_user_input(self, user_can_only_type:list, input_message:str) -> None:
        """Method that stops the code going forward if the user does not input a value from the provided list"""
        while True:
            try:
                user_input = input(input_message + ": ")
                if int(user_input) in user_can_only_type:
                    return user_input
                raise ValueError()
            except ValueError:
                print("\t Error: You are required to enter one of the following: {}".format(user_can_only_type))
                print("\t Please try again\n")



    def replace_cards(self, list_of_cards_selected:list, game_deck:Deck, discard_deck:Deck) -> None:
        """Removes Card() objects from Player() hand based on index position and put into nominated Deck(). Player then draws from nominated Deck()"""

        # code is structured like this so the new card thats the position of the old card and is not just added to the back of the hand.
        for each_pos_num in list_of_cards_selected:
            new_card = game_deck.remove_top_card()
            old_card = self.return_single_card_object(int(each_pos_num)-0)

            self.put_down_card_onto_deck(discard_deck, old_card)
            self.players_hand.insert(int(each_pos_num)-1, new_card)