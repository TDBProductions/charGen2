from utilities.DiceRoller import DiceRoller
from data.Character import Character
import random

class CharacterRoller(object):

    gameData = None

    def __init__(self, gameData):
        self.gameData = gameData
                
    # Returns a complete list of rolled characters
    def rollSelection(self, classString):
        # Create a new character
        print("Generating a character...")
        character = Character()

        # Determine sex
        charSexRoll = DiceRoller.rollDice("1d100")
        if charSexRoll >= 51:
            character.sex = "Male"
        else:
            character.sex = "Female"
        print("Sex: " + character.sex)

        # Determine class
        character.charClass = self.gameData.getClassByString(classString)
        print("Class: " + character.charClass.className)

        # Determine race
        character.charRace = self.raceSelection(character)
        print("Race: " + character.charRace.raceName)

        # Determine the abilitary array
        character.abilityArray = self.rollAbilities()
        character = self.verifyAbilities(character)

        print("Strength: " + str(character.abilityArray[0]))
        print("Wisdom: " + str(character.abilityArray[1]))
        print("Intelligence: " + str(character.abilityArray[2]))
        print("Dexterity: " + str(character.abilityArray[3]))
        print("Constitution: " + str(character.abilityArray[4]))
        print("Charisma: " + str(character.abilityArray[5]))

        # Determine height
        character.height = self.heightSelection(character)
        print("Height: " + character.height)

        # Determine weight
        character.weight = self.weightSelection(character)
        print("Weight: " + character.weight + " pounds")
 
        # Determine if we have exceptional strength
        character.exceptionalStrengthFlag, character.exceptionalStrengthVal = self.exceptionalStrength(character)
        print("Exceptional Strength: " + str(character.exceptionalStrengthFlag))
        print("Exceptional Strength Val: " + str(character.exceptionalStrengthVal))
        
        # Determine skills
        skillsArray = []
        skillsArray = self.skillSelection(character)

        if character.charClass.thiefFlag == True:
            character.thiefFlag = True

        character.toHitBonus = skillsArray[0]
        character.damageBonus = skillsArray[1]
        character.openDoors = skillsArray[2]
        character.bblg = skillsArray[3]
        character.acBonus = skillsArray[4]
        character.stealBonus = skillsArray[5]
        character.locksBonus = skillsArray[6]
        character.trapsBonus = skillsArray[7]
        character.sneakBonus = skillsArray[8]
        character.hideBonus = skillsArray[9]
        character.spellSaveBonus = skillsArray[10]
        character.hpBonus = skillsArray[11]
        print("To Hit Bonus " + str(character.toHitBonus))
        print("Damage Bonus " + str(character.damageBonus))
        print("Open Doors " + str(character.openDoors))
        print("BB/LG " + str(character.bblg))
        print("AC Bonus " + str(character.acBonus))
        print("Spell Save Bonus " + str(character.spellSaveBonus))
        print("HP Bonus " + str(character.hpBonus))
        if character.thiefFlag == True:
            print("Steal Bonus " + str(character.stealBonus))
            print("Locks Bonus " + str(character.locksBonus))
            print("Traps Bonus " + str(character.trapsBonus))
            print("Sneak Bonus " + str(character.sneakBonus))
            print("Hide Bonus " + str(character.hideBonus))

        # Determine saving throw adjustments
        character.saveArray = self.saveSelection(character)
        print("Saves:")
        print("\tPoison Save: " + str(character.saveArray[0]))
        print("\tPetrification Save: " + str(character.saveArray[1]))
        print("\tWand Save: " + str(character.saveArray[2]))
        print("\tBreath Save: " + str(character.saveArray[3]))
        print("\tSpell Save: " + str(character.saveArray[4]))

        # Determine thief skills if applicable
        if character.thiefFlag == True:
            thiefArray = []
            thiefArray = self.thiefSelection(character)
            character.steal = thiefArray[0]
            character.locks = thiefArray[1]
            character.traps = thiefArray[2]
            character.sneak = thiefArray[3]
            character.hide = thiefArray[4]
            character.listen = thiefArray[5]
            character.climb = thiefArray[6]
            character.read = thiefArray[7]
            print("Thief skills: ")
            print("\tSteal: " + str(character.steal))
            print("\tLocks: " + str(character.locks)) 
            print("\tTraps: " + str(character.traps)) 
            print("\tSneak: " + str(character.sneak)) 
            print("\tHide: " + str(character.hide)) 
            print("\tListen: " + str(character.listen)) 
            print("\tClimb: " + str(character.climb)) 
            print("\tRead: " + str(character.read))

        # Determine starting HP
        character.hp = self.hpSelection(character)
        print("Hp: " + str(character.hp))

        # Determine starting gold
        character.gold = self.goldSelection(character)
        print("Gold: " + str(character.gold))

        # Determine alignment
        character.alignment = self.alignmentSelection(character)
        print("Alignment: " + character.alignment)

        # Determine spells
        character.spells = self.spellSelection(character)
        print("Spells: ")
        for spell in character.spells:
            print("\t" + spell.spellName)

        # Determine weapons
        character.weapons = self.weaponSelection(character)
        print("Weapons:")
        for i in character.weapons:
            print("\t" + i.weaponName)
        #character.ammo = self.ammoSelection(character)
        #for i in characters.ammo:
        #    print("\t" + str(i[0]) + "( " + str(i[1]) + " )")

        # Determine armor
        character.armor = self.armorSelection(character)
        character.shield = self.shieldSelection(character)
        character.ac = int(character.armor.ac) + int(character.acBonus)
        print("Armor:")
        print("\t" + character.armor.armorName)
        if (character.shield is not None):
            print("\t" + character.shield.armorName)
            character.ac = int(character.ac) + int(character.shield.ac)
        print("Ac: " + str(character.ac))

        # Determine items
        character.items = self.itemSelection(character)
        print("Items:")
        for item in character.items:
            print("\t" + item.itemName)
        print("\n\n\n")

        return character

    def forcedClassSelection(self, classType):
        # Declarations
        classSelection = [] # Used to hold eligible class names
        character = None # Placeholder for the returned char type

        # If the class type being rolled is basic, add all basic classes into classSelection
        if (classType == "Basic"):
            for charClass in self.gameData.classes:
                if (charClass.classType == "Basic"):
                    classSelection.append(charClass.className)

        # If the class type being rolled is prestige, add all prestige classes into classSelection
        if (classType == "Prestige"):
            for charClass in self.gameData.classes:
                if (charClass.classType == "Prestige"):
                    classSelection.append(charClass.className)

        # Get a random class name out of the classSelection list
        classToRoll = random.choice(classSelection)
        # Pass to the character roller, return the rolled character
        character = self.rollSelection(classToRoll)
        return character

    def weightedClassSelection(self):
        # Declarations
        basicClassWeight = self.gameData.gameOptions['basicClassWeight']
        prestigeClassWeight = self.gameData.gameOptions['prestigeClassWeight']
        basicClassMin = self.gameData.gameOptions['basicClassMin']
        prestigeClassMin = self.gameData.gameOptions['prestigeClassMin']
        character = None        

        # Get all the classes, their type, and link with the class weight
        classWeights = []   
        sum = 0

        for charClass in self.gameData.classes:
            if (charClass.classType == "Basic"):
                sum = sum + int(basicClassWeight)
                classWeights.append([charClass.className, sum])
            elif (charClass.classType == "Prestige"):
                sum = sum + int(prestigeClassWeight)
                classWeights.append([charClass.className, sum])
        
        # We roll a dice from 1 to the maximum value of sum
        classRoll = DiceRoller.rollDice("1d"+str(sum))
        for i in classWeights:
            if (classRoll <= i[1]):
                charClass = i[0]
        
        chararacter = self.rollSelection(charClass)
        return character

    def randomClassSelection(self):
        pass

    def verifyClassRequirement(self, character):
        lookupArray = ["Strength", "Wisdom", "Intelligence", "Dexterity", "Constitution", "Charisma"]
        abilityArray = character.abilityArray
        print(abilityArray)
        abilityReq = character.charClass.abilityRequirements

        for ability, minVal in abilityReq:
            for lookupabil in lookupArray:
                if (ability == lookupabil):
                    if (abilityArray[lookupArray.index(lookupabil)] < minVal):
                        abilityArray[lookupArray.index(lookupabil)] = minVal
        print(abilityArray)
        return abilityArray
            
    def raceSelection(self, character):
        # Game options has the ability to restrict character race.  Two logical flows.
        
        # Declarations
        ignoreRaceRestrictions = self.gameData.gameOptions['ignoreRaceRestrictions']
        charClass = character.charClass
        allowedRaces = []

        # Turn to boolean for my own sanity
        if ignoreRaceRestrictions == "yes":
            ignoreRaceRestrictions = True
        else:
            ignoreRaceRestrictions = False
        
        # Seperate based upon game options
        if ignoreRaceRestrictions == True:
            # If ignoring race restrictions, we can return a random race.
            return random.choice(self.gameData.races)
        else:
            # If we are not, we must find the allowed ones.
            for race in charClass.races:
                allowedRaces.append(race)
            return self.gameData.getRaceByString(random.choice(allowedRaces))
            
    def rollAbilities(self):
        # Game option declarations
        rollMethod = self.gameData.gameOptions['rollMethod']
        minimumReroll = int(self.gameData.gameOptions['minimumReroll'])
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

    def verifyAbilities(self, character):
        # We have several checks we need to perform in order to ensure that the stats are capped where they should be.
        # Male to Female (if enabled)
        # Race
        # Add racial bonuses

        # Game options declarations
        enforceSexAbilities = self.gameData.gameOptions['enforceSexAbilities']
        enforceRacialAbilities = self.gameData.gameOptions['enforceRacialAbilities']
        abilityOrder = ["Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution", "Charisma"] # Used for finding corresponding stats in the min / max racial dictionaries
        sexModifiedFlag = False
        
        # Find out if the sex should be modified for comparison reasons
        if enforceSexAbilities == "yes":
            sexModifiedFlag = False
        else:
            # For logical reasons, we set the females to male to skip the check on females.  We change it back later
            if character.sex == "Female":
                sexModifiedFlag = True
                character.sex = "Male"
    
        if enforceRacialAbilities == "yes":
            enforceRacialAbilities = True
        else:
            enforceRacialAbilities = False

        # We perform the racial stat bonuses first as per the RAW
        for ability in character.charRace.abilityBonus:
            # Confusing I know...
            # Set the character's ability in the ability array that corresponds to the modified stat
            character.abilityArray[abilityOrder.index(ability)] = int(character.abilityArray[abilityOrder.index(ability)]) + int(character.charRace.abilityBonus[ability])

        # Break down by racial comparison
        if enforceRacialAbilities == True:
            # Break down by sex comparison
            if character.sex == "Female":
                # Racial cap data is stored as a dictionary (whoops) so we need to use this counter to keep track of indexes
                counter = 0
                # Loop over each ability
                for ability in abilityOrder:
                    # Get the current ability are are looking at
                    charAbility = character.abilityArray[counter]
                    # If ability is above the cap, set it to the cap
                    if charAbility >= int(character.charRace.abilityCapsMaxFemale[ability]):
                        character.abilityArray[counter] = int(character.charRace.abilityCapsMaxFemale[ability])
                    # If ability is below the floor, set it to the floor
                    if charAbility <= int(character.charRace.abilityCapsMinFemale[ability]):
                        character.abilityArray[counter] = int(character.charRace.abilityCapsMinFemale[ability])
                    # Increment the counter
                    counter += 1

            # If we have turned off the sexual disparity, all comparisons will be male.
            if character.sex == "Male":
                counter = 0
                for ability in abilityOrder:
                    charAbility = character.abilityArray[counter]
                    # If ability is above the cap, set it to the cap
                    if charAbility >= int(character.charRace.abilityCapsMaxMale[ability]):
                        character.abilityArray[counter] = int(character.charRace.abilityCapsMaxMale[ability])
                    # If ability is below the floor, set it to the floor
                    if charAbility <= int(character.charRace.abilityCapsMinMale[ability]):
                        character.abilityArray[counter] = int(character.charRace.abilityCapsMinMale[ability])
                    counter += 1

        # If we are turning this off, compare against human stats (a good baseline)
        elif enforceRacialAbilities == False:
            comparisonRace = self.gameData.getRaceByString("Human")
            if character.sex == "Female":
                counter = 0
                for ability in abilityOrder:
                    charAbility = character.abilityArray[counter]
                    # If ability is above the cap, set it to the cap
                    if charAbility >= int(comparisonRace.abilityCapsMaxFemale[ability]):
                        character.abilityArray[counter] = int(comparisonRace.abilityCapsMaxFemale[ability])
                    # If ability is below the floor, set it to the floor
                    if charAbility <= int(comparisonRace.abilityCapsMinFemale[ability]):
                        character.abilityArray[counter] = int(comparisonRace.abilityCapsMinFemale[ability])
                    counter += 1

            if character.sex == "Male":
                counter = 0
                for ability in abilityOrder:
                    charAbility = character.abilityArray[counter]
                    # If ability is above the cap, set it to the cap
                    if (charAbility >= int(comparisonRace.abilityCapsMaxMale[ability])):
                        character.abilityArray[counter] = int(comparisonRace.abilityCapsMaxMale[ability])
                    # If ability is below the floor, set it to the floor
                    if charAbility <= int(comparisonRace.abilityCapsMinMale[ability]):
                        character.abilityArray[counter] = int(comparisonRace.abilityCapsMinMale[ability])
                    counter += 1

        # Reset the gender if necessary!
        if sexModifiedFlag == True:
            character.sex = "Female"

        # TODO Check if we have met the minimum stat reqs


        return character

    def exceptionalStrength(self, character):
        # Here we determine if the character has exceptional strength
        # Return if we have exceptional strength as a boolean, and the value of it (1d100)
        
        # Declarations
        exceptionalStrengthRoll = 0
        exceptionalStrengthFlag = False

        # For exceptional strength, character must be a fighter with 18 strength
        if character.charClass.className == "Fighter":
            if character.abilityArray[0] >= 18:
                exceptionalStrengthFlag = True
                exceptionalStrengthRoll = DiceRoller.rollDice("1d100")

        if exceptionalStrengthRoll == 0:
            return exceptionalStrengthFlag, 0
    
        if (exceptionalStrengthRoll < 51):
            return exceptionalStrengthFlag, 1

        if (exceptionalStrengthRoll >= 51) and (exceptionalStrengthRoll < 76):
            return exceptionalStrengthFlag, 2
    
        if (exceptionalStrengthRoll >= 76) and (exceptionalStrengthRoll < 91):
            return exceptionalStrengthFlag, 3
        
        if (exceptionalStrengthRoll >= 91) and (exceptionalStrengthRoll < 100):
            return exceptionalStrengthFlag, 4

        if (exceptionalStrengthRoll == 100):
            return exceptionalStrengthFlag, 5
        print("never get here")

    def skillSelection(self, character):
        # Declarations
        statArray = []
        # Method use for getting skill bonuses, as well as thief skills if applicable
        strengthLookupIndex = int(character.abilityArray[0]) - 3
        dexterityLookupIndex = int(character.abilityArray[3]) - 3
        wisdomLookupIndex = int(character.abilityArray[2]) - 3
        constitutionLookupIndex = int(character.abilityArray[4]) - 3

        if character.exceptionalStrengthFlag == True:
            # If the character has exceptional strength, we add it to the lookup index in order to return better stats
            strengthLookupIndex = strengthLookupIndex + character.exceptionalStrengthVal
        
        # Get the strength stats
        for i in range(0, 4):
            statArray.append(self.gameData.statAdjustments[i][strengthLookupIndex])    

        # Get the dex stats
        for i in range(4, 10):
            statArray.append(self.gameData.statAdjustments[i][dexterityLookupIndex])

        # Get the one and only wisdom stat
        statArray.append(self.gameData.statAdjustments[10][wisdomLookupIndex])

        # Get the one and only con stat
        statArray.append(self.gameData.statAdjustments[11][constitutionLookupIndex])
        return statArray

    def alignmentSelection(self, character):
        return random.choice(character.charClass.alignments)
        print("never reached but VS won't let me collapse this if it's a one liner")

    def spellSelection(self, character):
        # Declarations
        spellClass = character.charClass.spellClass
        level1Spells = character.charClass.spellsLevel1
        level2Spells = character.charClass.spellsLevel2
        class1Spells = []
        class2Spells = []
        charSpells = []
        
        # Get the class spells
        for spell in self.gameData.spells:
            if spell.spellClass == spellClass:
                if int(spell.spellLevel) == 1:
                    class1Spells.append(spell)

        for spell in self.gameData.spells:
            if spell.spellClass == spellClass:
                if int(spell.spellLevel) == 2:
                    class2Spells.append(spell)

        for i in range(0, int(level1Spells)):
            charSpells.append(random.choice(class1Spells))
        for i in range(0, int(level2Spells)):
            charSpells.append(random.choice(class2Spells))
        

        return charSpells
    
    def hpSelection(self, character):
        # Used to determine starting HP for the character
        hpDice = character.charClass.initialHitDice
        hpBonus = character.hpBonus

        hp = DiceRoller.rollDice(hpDice) + int(hpBonus)
        return hp
    
    def heightSelection(self, character):
        # Get height values, differed by sex
        if (character.sex == "Male"):
            heightBase = character.charRace.mHeight[0]
            heightMinus = character.charRace.mHeight[1]
            heightPlus = character.charRace.mHeight[2]
            heightOWeight = character.charRace.mHeight[3]
            heightUWeight = character.charRace.mHeight[4]
            
        elif (character.sex == "Female"):
            heightBase = character.charRace.fHeight[0]
            heightMinus = character.charRace.fHeight[1]
            heightPlus = character.charRace.fHeight[2]
            heightOWeight = character.charRace.fHeight[3]
            heightUWeight = character.charRace.fHeight[4]

        # Here we roll a d100, if the number is greater than or equal to the OWeight, we add a heightPlus dice.
        #                      if the number is less than or equal to the    UWeight, we subtract a heightMinus dice.
        heightRoll = DiceRoller.rollDice("1d100")

        if (heightRoll >= int(heightOWeight)):
            heightAdd = DiceRoller.rollDice(heightPlus)
            height = int(heightBase) + heightAdd

        elif (heightRoll <= int(heightUWeight)):
            heightSub = DiceRoller.rollDice(heightMinus)
            height = int(heightBase) - heightSub
        
        else:
            height = int(heightBase)
        # Convert the heightBase into feet
        heightInches = height % 12
        heightFeet = height // 12

        return (str(heightFeet) + "'" + str(heightInches) + "\"")

    def weightSelection(self, character):
        # Get height values, differed by sex
        if (character.sex == "Male"):
            weightBase = character.charRace.mWeight[0]
            weightMinus = character.charRace.mWeight[1]
            weightPlus = character.charRace.mWeight[2]
            weightOWeight = character.charRace.mWeight[3]
            weightUWeight = character.charRace.mWeight[4]
            
        elif (character.sex == "Female"):
            weightBase = character.charRace.fWeight[0]
            weightMinus = character.charRace.fWeight[1]
            weightPlus = character.charRace.fWeight[2]
            weightOWeight = character.charRace.fWeight[3]
            weightUWeight = character.charRace.fWeight[4]

        # Here we roll a d100, if the number is greater than or equal to the OWeight, we add a heightPlus dice.
        #                      if the number is less than or equal to the    UWeight, we subtract a heightMinus dice.
        weightRoll = DiceRoller.rollDice("1d100")

        if (weightRoll >= int(weightOWeight)):
            weightAdd = DiceRoller.rollDice(weightPlus)
            weight = int(weightBase) + weightAdd

        elif (weightRoll <= int(weightUWeight)):
            weightSub = DiceRoller.rollDice(weightMinus)
            weight = int(weightBase) - weightSub
        
        else:
            weight = int(weightBase)\

        return (str(weight))

    def saveSelection(self, character):
        # Get class definition of saving throws
        poisonSave = character.charClass.poisonSave
        petrificationSave = character.charClass.petrificationSave
        wandSave = character.charClass.wandSave
        breathSave = character.charClass.breathSave
        spellSave = character.charClass.spellSave
        saveArray = []

        # Get the constitution score
        conScore = character.abilityArray[4]
        conScoreIndex = conScore - 3 # To use to lookup in the racial charts, as they are listed from 3-18 (index 0 - 15)

        # Add up all bonuses, including racial bonus.  Except on key error if the race does not have a bonus on that save.
        try:
            saveArray.append(int(poisonSave) + int(character.charRace.saveBonuses["Poison"][conScoreIndex]))
        except KeyError:
            saveArray.append(poisonSave)

        try:
            saveArray.append(int(petrificationSave) + int(character.charRace.saveBonuses["Petrification"][conScoreIndex]))
        except KeyError:
            saveArray.append(petrificationSave)

        try:
            saveArray.append(int(wandSave) + int(character.charRace.saveBonuses["Wand"][conScoreIndex]))
        except KeyError:
            saveArray.append(wandSave)

        try:
            saveArray.append(int(breathSave) + int(character.charRace.saveBonuses["Breath"][conScoreIndex]))
        except KeyError:
            saveArray.append(breathSave)

        try:
            saveArray.append(int(breathSave) + int(character.charRace.saveBonuses["Spell"][conScoreIndex]) - int(character.spellSaveBonus)) # By RAW, spell save index is affected by con.  Add this in here
        except KeyError:
            saveArray.append(int(breathSave) - int(character.spellSaveBonus))
    
        return saveArray

    def thiefSelection(self, character):
        # Declarations
        thiefSkillArray = []
        # Get the racial bonus
        racialBonusDict = character.charRace.thiefBonuses

        # Perform a lookup on the racial bonus dictionary, except on KeyError if the race does not have a bonus on the skill
        try:
            thiefSkillArray.append(int(racialBonusDict["Steal"]) + int(self.gameData.thiefSkills.steal) + int(character.stealBonus))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.steal) + int(character.stealBonus))
    
        try:
            thiefSkillArray.append(int(racialBonusDict["Locks"]) + int(self.gameData.thiefSkills.locks) + int(character.locksBonus))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.locks) + int(character.locksBonus))

        try:
            thiefSkillArray.append(int(racialBonusDict["Traps"]) + int(self.gameData.thiefSkills.traps) + int(character.trapsBonus))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.traps) + int(character.trapsBonus))

        try:
            thiefSkillArray.append(int(racialBonusDict["Sneak"]) + int(self.gameData.thiefSkills.sneak) + int(character.sneakBonus))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.sneak) + int(character.sneakBonus))

        try:
            thiefSkillArray.append(int(racialBonusDict["Hide"]) + int(self.gameData.thiefSkills.hide) + int(character.hideBonus))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.hide) + int(character.hideBonus))

        try:
            thiefSkillArray.append(int(racialBonusDict["Listen"]) + int(self.gameData.thiefSkills.listen))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.listen))\

        try:
            thiefSkillArray.append(int(racialBonusDict["Climb"]) + int(self.gameData.thiefSkills.climb))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.climb))

        try:
            thiefSkillArray.append(int(racialBonusDict["Read"]) + int(self.gameData.thiefSkills.read))
        except KeyError:
            thiefSkillArray.append(int(self.gameData.thiefSkills.read))

        index = 0
        for skill in thiefSkillArray:
            if skill < 0:
                thiefSkillArray[index] = 0
            if skill > 100:
                thiefSkillArray[index] = 100
            index += 1
        return thiefSkillArray     

    def weaponSelection(self, character):
        # Declarations
        eligibleWeaponsList = []
        charRequiredWeaponsList = []
        weaponsList = []
        rollFlag = False

        # Create a list of weapons that match the specific considerations of the character's class definition
        for weapon in character.charClass.weaponsList:
            # Get the weapon definition
            weaponType = weapon[0]
            weaponWeight = weapon[1]
            weaponTag = weapon[2]
            weaponOrTag = weapon[3].split(" ")
            weaponAndTag = weapon[4].split(" ")
            weaponNotTag = weapon[5].split(" ")

            # If the weapon is required, we roll it definitely.  If the weapon is optional, we roll 1d100 depending on weight
            if (weaponType == "required"):
                rollFlag = True

            if (weaponType == "optional"):
                weaponRoll = DiceRoller.rollDice("1d100")
                if (int(weaponRoll) > int(weaponWeight)):
                    rollFlag = True

            # If we are rolling the weapon...
            if (rollFlag == True):
                # Loop over each weapon loaded into the game during weaponsImporter
                for weaponData in self.gameData.weapons:
                    # If the tag in class definition matches any tag on the weapon...
                    if (weaponTag in weaponData.weaponTags or weaponTag == ""):
                        # If any of the ORTAG in class definition matches any tag on the weapon...
                        if (set(weaponOrTag).intersection(set(weaponData.weaponTags)) or weaponOrTag == ['']):
                            # If ALL of the ANDTAG in the class definition matches tags on the weapon...
                            if (set(weaponAndTag).issubset(set(weaponData.weaponTags)) or weaponAndTag == ['']):
                                # If NONE of the NOTTAG in the class definition matches tags on the weapon...
                                if (not set(weaponNotTag).intersection(set(weaponData.weaponTags)) or weaponNotTag == ['']):
                                    # Append the weapon to the eligible weapons list
                                    eligibleWeaponsList.append(weaponData)
                # Append a random weapon from the eligible weapons into the character's weapon list
                weaponsList.append(random.choice(eligibleWeaponsList))
                # Reset eligible weapons list
                eligibleWeaponsList = []
            # Reset roll flag
            rollFlag = False

        # Return list of weapons
        return weaponsList

    #def ammoSelection(self, character):
        # If we have a ranged weapon, we need to get the ammo for it.
        # Declarations
    #    weaponsList = character.weaponsList
    #    ammoList = []

        return ammoList

    def goldSelection(self, character):
        goldDice = character.charClass.startingGold
        gold = DiceRoller.rollDice(goldDice) * 10
        return gold

    def armorSelection(self, character):
        eligibleArmors = character.charClass.armors.copy()
        if "Shields" in eligibleArmors:
            eligibleArmors.remove("Shields")
        return random.choice(self.gameData.getArmorListByString(random.choice(eligibleArmors)))      

    def shieldSelection(self, character):
        eligibleArmors = character.charClass.armors.copy()
        if "Shields" in eligibleArmors:
            return random.choice(self.gameData.getArmorListByString("Shields"))
        return None

    def itemSelection(self, character):
        # Declarations
        itemData = self.gameData.items
        eligibleItemsCategories = []
        eligibleItemsList = []
        itemsList = []
        
        # We want a reference list for item categories
        for item in itemData:
            if item.itemCategory not in eligibleItemsCategories:
                eligibleItemsCategories.append(item.itemCategory)       
                eligibleItemsList.append([])     

        # We want to append items of that category into a matching slot of the list
        for item in itemData:
            eligibleItemsList[eligibleItemsCategories.index(item.itemCategory)].append(item)
            
        # This gives us a list of items broken down by item category.
        # for now we are just going to roll 1-3 miscellaneous
        amountOfItems = DiceRoller.rollDice("1d3")

        for i in range(0,amountOfItems):
            itemsList.append(random.choice(eligibleItemsList[eligibleItemsCategories.index("Miscellaneous")]))

        return itemsList
