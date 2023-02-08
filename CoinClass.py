import random

#You would never really run this. Just save an apply
# The Coin class simulates a coin that can
# be flipped.
# use upper case for naming class variable
class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.
    #ensures that instance calling it is the only thing interacting with it
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.
    #Logic is used this way for checking. Compartmenatlize as much as possible
    #Accessor methods or get methods are used for retunring a varibale

    def get_sideup(self):
            return self.sideup
