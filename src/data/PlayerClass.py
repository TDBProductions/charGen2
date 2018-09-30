from data.Feature import Feature

class PlayerClass:
    """Holds the data model for a (player) class"""
    
    className = None # String
    classType = None # String
    abilityRequirements = None # Dictionary mapping { Ability, Value }
    initialHitDice = None # String
    levelHitDice = None # String
    races = None # List of strings
    armors = None # List of strings
    features = None # Dictionary mapping
    alignments = None # List of strings
    poisonSave = None # Integer
    petrificationSave = None # Integer
    wandSave = None # Integer
    breathSave = None # Integer
    spellSave = None # Integer
    thac0 = None # Integer SUBJECT TO CHANGE
    startingGold = None # String
    spellClass = None # String
    spellsLevel1 = 0 # Int
    spellsLevel2 = 0 # Int
    weaponsList = [] # list of lists of strings

    def __init__(self):
        pass