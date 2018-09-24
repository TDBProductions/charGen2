import unittest
from data.Armor import Armor
from data.PlayerClass import PlayerClass


class ImporterTest(unittest.TestCase):
    """Used for testing the importer classes"""

    def __init__(self):
        pass
      
    ### Armor testing
    def armorTest(self, armor):
        self.assertIsInstance(armor, Armor)

    # Armor Class (Heavy, medium, etc.) (string)
    def armorTestArmorClass(self, armorClass):
        self.assertIsInstance(armorClass, str)

    # Armor Name (string)
    def armorTestArmorName(self, armorName):
        self.assertIsInstance(armorName, str)

    # Armor AC (integer)
    def armorTestAC(self, ac):
        self.assertIsInstance(ac, int)

    # Armor Characteristics (list of strings
    def armorTestCharacteristics(self, characteristics):
        self.assertIsNotNone(characteristics)

    ### (Char) Class testing
    def classTest(self, charClass):
        self.assertIsInstance(charClass, PlayerClass)
    # Class Name
    def classTestClassName(self, className):
        self.assertIsInstance(className, str)

    # Class Type

    def classTestClassType(self, classType):
        self.assertIsInstance(classType, str)

    # Ability Requirements
    def classTestClassAbilityRequirements(self, abilityRequirements):
        self.assertIsInstance(abilityRequirements, dict)

    # Initial Hit Dice
    def classTestInitialHitDice(self, initialHitDice):
        self.assertIsInstance(initialHitDice, str)

    # Level Hit Dice
    def classTestLevelHitDice(self, levelHitDice):
        self.assertIsInstance(levelHitDice, str)

    # Races
    def classTestRaces(self, races):
        self.assertIsInstance(races, list)
        for race in races:
            self.assertIsInstance(race, str)
    
    # Armors
    def classTestArmors(self, armors):
        self.assertIsInstance(armors, list)
        for armor in armors:
            self.assertIsInstance(armor, str)

    # Features list
    def classTestFeatures(self, features):
        self.assertIsInstance(features, dict)

    # Alignments
    def classTestAlignments(self, alignments):
        self.assertIsInstance(alignments, list)
        for alignment in alignments:
            self.assertIsInstance(alignment, str)

    # Poison Save
    def classTestPoisonSave(self, poisonSave):
        self.assertIsInstance(poisonSave, int)

    # Petrification Save
    def classTestPetrificationSave(self, petrificationSave):
        self.assertIsInstance(petrificationSave, int)

    # Wand Save
    def classTestWandSave(self, wandSave):
        self.assertIsInstance(wandSave, int)

    # Breath Save
    def classTestBreathSave(self, breathSave):
        self.assertIsInstance(breathSave, int)

    # Spell Save
    def classTestSpellSave(self, spellSave):
        self.assertIsInstance(spellSave, int)

    # Starting Gold
    def classTestStartingGold(self, startingGold):
        self.assertIsInstance(startingGold, str)

    # Spell Class
    def classTestSpellClass(self, spellClass):
        self.assertIsInstance(spellClass, str)

    # Spells Level 1
    def classTestSpellsLevel1(self, spellsLevel1):
        self.assertIsInstance(spellsLevel1, int)

    # Spells Level 2
    def classTestSpellsLevel2(self, spellsLevel2):
        self.assertIsInstance(spellsLevel2, int)

    # Weapons
    def classTestWeapons(self, weapons):
        self.assertIsInstance(weapons, list)
        for weapon in weapons:
            for weaponAttribute in weapon:
                self.assertIsInstance(weaponAttribute, str)
    
    ### Game Options testing
    def optionsTestGeneratorMode(self, generatorMode):
        self.assertIsInstance(generatorMode, str)

    def optionsTestEnforceSexAbilities(self, enforceSexAbilities):
        self.assertIsInstance(enforceSexAbilities, str)

    def optionsTestEnforceRacialAbilities(self, enforceRacialAbilities):
        self.assertIsInstance(enforceRacialAbilities, str)

    def optionsTestIgnoreRaceRestrictions(self, ignoreRaceRestrictions):
        self.assertIsInstance(ignoreRaceRestrictions, str)

    def optionsTestMinimumReroll(self, minimumReroll):
        self.assertIsInstance(minimumReroll, str)

    def optionsTestEnforceFloorValues(self, enforceFloorValues):
        self.assertIsInstance(enforceFloorValues, str)

    def optionsTestRollMethod(self, rollMethod):
        self.assertIsInstance(rollMethod, str)

    def optionsTestEnforceAbilityScores(self, enforceAbilityScores):
        self.assertIsInstance(enforceAbilityScores, str)

    def optionsTestCharGenMode(self, charGenMode):
        self.assertIsInstance(charGenMode, str)

    def optionsTestCharactersGenerated(self, charactersGenerated):
        self.assertIsInstance(charactersGenerated, str)

    def optionsTestBasicClassWeight(self, basicClassWeight):
        self.assertIsInstance(basicClassWeight, str)

    def optionsTestPrestigeClassWeight(self, prestigeClassWeight):
        self.assertIsInstance(prestigeClassWeight, str)

    def optionsTestBasicClassMin(self, basicClassMin):
        self.assertIsInstance(basicClassMin, str)

    def optionsTestPrestigeClassMin(self, prestigeClassMin):
        self.assertIsInstance(prestigeClassMin, str)

    def optionsTestBasicClassCount(self, basicClassCount):
        self.assertIsInstance(basicClassCount, str)

    def optionsTestPrestigeClassCount(self, prestigeClassCount):
        self.assertIsInstance(prestigeClassCount, str)


    # Item testing

    # Race testing

    # Spell testing

    # Stat Adjustment testing

    # Thief skill testing

    # Weapon testing


