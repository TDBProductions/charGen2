import time
from test.ImporterTest import ImporterTest
from data.GameData import GameData
from utilities.CharacterGenerator import CharacterGenerator

class Bootstrap(object):
    """Used to bootstrap the application and maintain program flow."""
 
    gameData = None

    def __init__(self):
        self.printOpeningMessage()
        self.importGameData()        
        characters = CharacterGenerator(self.gameData)
        
    def printOpeningMessage(self):
        print("Welcome to the Die in a Dungeon Standalone Character Generator!\n")
        print("The output of this generator will be a number of randomly defined characters as per the rules set in config.xml.")
        print("For more information on the use of this program, please see the readme.txt file in the directory.")
        print("The generator will now begin.\n")
        print("...\n")

    def importGameData(self):
        self.gameData = GameData()

    def generateCharacters(self):
        pass