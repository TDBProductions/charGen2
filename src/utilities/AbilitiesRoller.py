from utilities.DiceRoller import DiceRoller

class AbilitiesRoller(object):
    def __init__(self):
        pass

    def rollAbilities(gameData):
        # Game option declarations
        rollMethod = gameData.gameOptions['rollMethod']
        minimumReroll = int(gameData.gameOptions['minimumReroll'])
        minimumRerollFlag = True

        # Roll until we hit the minimum reroll value
        while (minimumRerollFlag):
            # Declarations
            sum = 0
            abilitySum = 0
            diceArray = []
            abilityArray = []
            # If no method found, default to roll4drop1
            if rollMethod == None:
                rollMethod = "roll4drop1"

            # Roll 4 Drop 1 Method
            if rollMethod == "roll4drop1":
                # Roll for each ability (6 abilities, STR, DEX, CON, WIS, INT, CHA)
                for ability in range(0,6):
                    for i in range(0,4):
                        diceArray.append(DiceRoller.rollDice("1d6"))

                    # Drop the lowest value
                    diceArray.remove(min(diceArray))

                    # Sum the remainders
                    for i in diceArray:
                        sum = sum + i

                    # Append the sum to the abilityArray
                    abilityArray.append(sum)

                    # Reset the diceArray and sum
                    sum = 0
                    diceArray = []

            # Roll 3 method
            elif rollMethod == "roll3":
                # Roll for each ability (6 abilities, STR, DEX, CON, WIS, INT, CHA)
                for ability in range(0,6):
                    for i in range(0,3):
                        diceArray.append(DiceRoller.rollDice("1d6"))

                    # Sum the stats
                    for i in diceArray:
                        sum = sum + i

                    # Append the sum to the abilityArray
                    abilityArray.append(sum)

                    # Reset the diceArray and sum
                    sum = 0
                    diceArray = []
                
            
            # Sum the ability array to compare min reroll
            for i in abilityArray:
                abilitySum = abilitySum + i
        
            # Compare ability sum to minimum reroll value, end while loop if met
            if (abilitySum >= minimumReroll):
                minimumRerollFlag = False

        return abilityArray

    def verifyAbilities(gameData, attributeArray):
        # We have several checks we need to perform in order to ensure that the stats are capped where they should be.
        # Male to Female (if enabled)
        # Race
        enforcedGenderedAbilities = gameData.gameOptions['enforceGenderedAbilities']
        
        # First we check the race scores.
        


