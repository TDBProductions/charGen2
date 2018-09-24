import random

class DiceRoller:
    """Object used to roll dice."""

    rollHistory = None

    def __init__(self):
        self.rollHistory = [0,0,0,0,0] # Contains the last 5 rolls

    def rollDice(roll):
        """Accepts input as xdy, where x is the number of dice to roll, and y is the value of the dice to roll"""

        # TODO Validate the input first
        sum = 0
        diceSplit = roll.split('d')
        numberOfDice = int(diceSplit[0])
        valueOfDice = int(diceSplit[1])
        
        for i in range(1, numberOfDice+1):
            sum = sum + random.randint(1,valueOfDice)

        return sum