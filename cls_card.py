class Card():
    def __init__(self, rank:str, value:int, display:str, suit:str, suitNum:int):
        self.rank = rank
        self.value = value
        self.display = display
        self.suit = suit
        self.suitNum = suitNum

    def __str__(self) -> str:
        return str(self.display) + " of " + str(self.suit)    #this isn't used anywhere

    def return_tuple(self) -> tuple:
        "Returns a tuple of a single card"
        #note. Need to review if actually used anymore
        return self.display, self.suit

    def print_for_terminal(self, display:int, suit:str) -> str:
        """Prints a single Card() object to terminal. Used with map() and zip() in the Player() class to print a series of cards"""
        suit = suit
        display = display
        return (
            '           \n'
            '┌─────────┐\n'
            '│{}       │\n'
            '│         │\n'
            '│         │\n'
            '│    {}   │\n'
            '│         │\n'
            '│         │\n'
            '│       {}│\n'
            '└─────────┘\n'
            '           \n'
        ).format(
            format(display, ' <2'),
            format(suit, ' <2'),
            format(display, ' >2')
        ).splitlines()