from importers.GameOptionsImporter import GameOptionsImporter
from importers.ClassImporter import ClassImporter
from importers.RaceImporter import RaceImporter
from importers.ArmorImporter import ArmorImporter
from importers.WeaponsImporter import WeaponsImporter
from importers.ItemImporter import ItemImporter
from importers.SpellImporter import SpellImporter
from importers.StatAdjustmentImporter import StatAdjustmentImporter
from importers.ThiefSkillImporter import ThiefSkillImporter
from data.PlayerClass import PlayerClass
from test.ImporterTest import ImporterTest

class GameData:
    """Used to access game data."""

    armor = []
    classes = []
    gameOptions = {}
    items = []
    races = []
    spells = []
    weapons = []
    statAdjustments = []

    def __init__(self):
        print("Beginning data import...\n")

        self.armor = ArmorImporter.importArmor()
        self.testArmor(self.armor)

        self.classes = ClassImporter.importClass()
        self.testClass(self.classes)

        self.gameOptions = GameOptionsImporter.importGameOptions()
        self.testGameOptions(self.gameOptions)
        self.items = ItemImporter.importItems()
        self.races = RaceImporter.importRaces()
        self.spells = SpellImporter.importSpells()
        self.weapons = WeaponsImporter.importWeapons()
        self.statAdjustments = StatAdjustmentImporter.importStatAdjustments()
        self.thiefSkills = ThiefSkillImporter.importThiefSkills()

        print("Data import successful!\n")

    def testArmor(self, armorList):
        # Declarations
        tester = ImporterTest()

        # Armor Test
        print("Verifying armor import...")
        for armor in armorList:
            tester.armorTest(armor)
            tester.armorTestArmorClass(armor.armorClass)
            tester.armorTestArmorName(armor.armorName)
            tester.armorTestAC(armor.ac)
            tester.armorTestCharacteristics(armor.characteristics)
        print("Armor import verified!\n\n")

    def testClass(self, classList):
        # Declarations 
        tester = ImporterTest()

        # Character class test
        print("Verifying class import...")
        for charClass in classList:
            tester.classTest(charClass)
            tester.classTestClassName(charClass.className)
            tester.classTestClassType(charClass.classType)
            tester.classTestClassAbilityRequirements(charClass.abilityRequirements)
            tester.classTestInitialHitDice(charClass.initialHitDice)
            tester.classTestLevelHitDice(charClass.levelHitDice)
            tester.classTestRaces(charClass.races)
            tester.classTestArmors(charClass.armors)
            tester.classTestFeatures(charClass.features)

            tester.classTestPoisonSave(charClass.poisonSave)
            tester.classTestPetrificationSave(charClass.petrificationSave)
            tester.classTestWandSave(charClass.wandSave)
            tester.classTestBreathSave(charClass.breathSave)
            tester.classTestSpellSave(charClass.spellSave)


            tester.classTestStartingGold(charClass.startingGold)
            tester.classTestSpellClass(charClass.spellClass)
            tester.classTestSpellsLevel1(charClass.spellsLevel1)
            tester.classTestSpellsLevel2(charClass.spellsLevel2)

            tester.classTestWeapons(charClass.weaponsList)

        print("Class import verified!\n\n")

    def testGameOptions(self, gameOptions):
        tester = ImporterTest()
        print("Verifying game configuration...")

        tester.optionsTestGeneratorMode(gameOptions['generatorMode'])
        tester.optionsTestEnforceSexAbilities(gameOptions['enforceSexAbilities'])
        tester.optionsTestEnforceRacialAbilities(gameOptions['enforceRacialAbilities'])
        tester.optionsTestIgnoreRaceRestrictions(gameOptions['ignoreRaceRestrictions'])
        tester.optionsTestMinimumReroll(gameOptions['minimumReroll'])
        tester.optionsTestEnforceFloorValues(gameOptions['enforceFloorValues'])
        tester.optionsTestRollMethod(gameOptions['rollMethod'])
        tester.optionsTestEnforceAbilityScores(gameOptions['enforceAbilityScores'])
        tester.optionsTestCharGenMode(gameOptions['charGenMode'])
        tester.optionsTestCharactersGenerated(gameOptions['charactersGenerated'])
        tester.optionsTestBasicClassWeight(gameOptions['basicClassWeight'])
        tester.optionsTestPrestigeClassWeight(gameOptions['prestigeClassWeight'])
        tester.optionsTestBasicClassMin(gameOptions['basicClassMin'])
        tester.optionsTestPrestigeClassMin(gameOptions['prestigeClassMin'])
        tester.optionsTestBasicClassCount(gameOptions['basicClassCount'])
        tester.optionsTestPrestigeClassCount(gameOptions['prestigeClassCount'])

        print("Game configuration verified!")


    def getClassByString(self, className):
        for charClass in self.classes:
            if (charClass.className == className):
                return charClass

    def getRaceByString(self, raceName):
        for charRace in self.races:
            if (charRace.raceName == raceName):
                return charRace


    def getArmorListByString(self, armorClass):
        armorList = []
        for armor in self.armor:
            if armor.armorClass == armorClass:
                armorList.append(armor)
        return armorList