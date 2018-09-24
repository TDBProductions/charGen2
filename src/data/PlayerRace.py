from data.Feature import Feature

class PlayerRace:
    """Holds the data model for a (player) race"""

    raceName = None # String
    abilityCapsMinMale = None # Dictionary objects { "Ability" : "Val" }
    abilityCapsMinFemale = None # Dictionary objects { "Ability" : "Val" }
    abilityCapsMaxMale = None # Dictionary objects { "Ability" : "Val" }
    abilityCapsMaxFemale = None # Dictionary objects { "Ability" : "Val" }
    abilityBonus = None # List of dictionary objects { "Ability" : "Val" }
    raceFeatures = None # Complex object.  Use the Feature class.
    languages = None # List of strings
    mWeight = None # List of ints / strings
    mHeight = None # List of ints / strings
    fWeight = None # List of ints / strings
    fHeight = None # List of ints / strings
    saveBonuses = None # Dictionary of { "Ability": ["val", "val"..."val"] } (save bonuses are affected by ability, so we must list all affects from 3-18)
    thiefBonuses = None # Dictionary of { "Ability" : "Val"}
    

    def __init__(self):
        pass