import random


# You would never really run this. Just save an apply
# The Coin class simulates a coin that can
# be flipped.
# use upper case for naming class variable
class Insect:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.
    # ensures that instance calling it is the only thing interacting with it
    def __init__(self):
        self.wings = "2"
        self.legs = "4"
        self.flight = "0"

    def get_number(self):
        if self.wings == "Two" and self.legs == "Four":
            self.flight = random.randint(0, 10)
        else:
            print("No flight!")

    # The get_sideup method returns the value
    # referenced by sideup.
    # Logic is used this way for checking. Compartmenatlize as much as possible
    # Accessor methods or get methods are used for retunring a varibale

    def get_flight(self):
        return self.flight
