import random
from utilities.CharacterRoller import CharacterRoller

class CharacterGenerator(object):
    """Object used to generate characters."""

    gameData = None
    characterList = []

    def __init__(self, gameData):
        self.gameData = gameData
        self.characterList = []
        
        # Determines the program mode, classic or enhanced
        generatorMode = gameData.gameOptions['generatorMode']
        # Determines the char gen mode, weightedRandom, forced, or random
        charGenMode = gameData.gameOptions['charGenMode']
        # Determines how many characters to generate
        charactersGenerated = gameData.gameOptions['charactersGenerated']
        # Determines how many basic class chars to generate
        basicClassCount = gameData.gameOptions['basicClassCount']
        prestigeClassCount = gameData.gameOptions['prestigeClassCount']
        # Character roller object
        characterRoller = CharacterRoller(gameData)
        
        # Break down by char gen mode
        # Weighted Random generation mode
        if (charGenMode == "weightedRandom"):
            # Returns a complete list of rolled characters
            for i in range(0, int(charactersGenerated)):
                self.characterList.append(characterRoller.weightedClassSelection())
                # TODO verify number of basic / prestiges rolled

        # Forced count generation mode
        if (charGenMode == "forced"):
            for i in range(0, int(basicClassCount)):
                self.characterList.append(characterRoller.forcedClassSelection("Basic"))
            for i in range(0, int(prestigeClassCount)):
                self.characterList.append(characterRoller.forcedClassSelection("Prestige"))
            # Randomize the list
            random.shuffle(self.characterList)


        # True random generation mode 
        if (charGenMode == "random"):
            pass