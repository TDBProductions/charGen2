import xml.etree.ElementTree as ET
import os
from data.PlayerClass import PlayerClass

class ClassImporter:
    """Used to parse the XML of the class files for import into the generator"""

    def __init__(self):
        pass

    def importClass():
        index = 0
        # Define the Class List
        classList = []

        print("Importing character classes...")
        classFiles = os.listdir("Data\Class")
        for charClass in classFiles:
            # Try to parse the XML.  Catch broken XML and abort.
            try:
                tree = ET.parse("Data\Class\\" + charClass)
            except ET.ParseError:
                print("Import unsuccessful!  Check the file: " + charClass)
                print("Exiting...")
                input('Press Enter to exit')
                exit(0)

            # Create a new instance of Player Class per file in the class directory
            classList.append(PlayerClass())

            # Get Class Name, assign to class
            classList[index].className = tree._root.get("name")

            # Get Class Type, assign to class
            classList[index].classType = tree._root[0].get("value")

            # Get Floor Val, assign to class
            classList[index].floorVal = tree._root[1].get("value")

            # Get Class requirements, assign to class.  This is a dictionary object
            abilityReqs = {}
            for i in tree._root[2]:
                ability = i.attrib['name']
                value = i.attrib['value']
                abilityReqs[ability] = value
            classList[index].abilityRequirements = abilityReqs

            # Get hit dice
            classList[index].initialHitDice = tree._root[3][0].get("value")
            classList[index].levelHitDice = tree._root[3][1].get("value")
            
            # Get race list
            raceList = []
            for i in tree._root[4]:
                race = i.attrib['name']
                raceList.append(race)
            classList[index].races = raceList
            
            # Get armor list
            armorList = []
            for i in tree._root[5]:
                armor = i.attrib['name']
                armorList.append(armor)
            classList[index].armors = armorList

            # Get the class features
            classFeatures = {}
            for i in tree._root[6]:
                feature = i.attrib['name']
                featureDesc = i.attrib['description']
                classFeatures[feature] = featureDesc
            classList[index].features = classFeatures

            # Get the class alignments
            alignments = []
            for i in tree._root[7]:
                alignment = i.attrib['name']
                alignments.append(alignment)
            classList[index].alignments = alignments

            # Get the Saves
            saveArray = []
            for i in tree._root[8]:
                saveArray.append(i.attrib['value'])
            classList[index].poisonSave = int(saveArray[0])
            classList[index].petrificationSave = int(saveArray[1])
            classList[index].wandSave = int(saveArray[2])
            classList[index].breathSave = int(saveArray[3])
            classList[index].spellSave = int(saveArray[4])

            # Get the Starting Gold
            classList[index].startingGold = tree._root[9].get("value")

            # Get amount of spells
            # If we return something here, character has spells
            if (tree._root[10].find("spell") != None):
                # Note the spell class
                classList[index].spellClass = tree._root[10].attrib['class']
                # Loop through all levels:
                for spellElement in tree._root[10]:
                    # Get level 1 spells
                    if spellElement.attrib["name"] == "Level 1":
                        classList[index].spellsLevel1 = int(spellElement.attrib['value'])
                    # Get level 2 spells
                    if spellElement.attrib["name"] == "Level 2":
                        classList[index].spellsLevel2 = int(spellElement.attrib['value'])
           
            else:
                classList[index].spellClass = "noclass"
                classList[index].spellsLevel1 = 0
                classList[index].spellsLevel2 = 0

            # Get the weapons
            weaponsDataList = []
            weaponList = []
            weaponType = ""
            weaponWeight = ""
            weaponTag = ""
            weaponOrTag = ""
            weaponAndTag = ""
            weaponNotTag = ""
            for weaponReq in tree._root[11]:
                try:
                    weaponType = weaponReq.attrib['type']
                except KeyError:
                    weaponType = ""

                try:
                    weaponWeight = weaponReq.attrib['weight']
                except KeyError:
                    weaponWeight = "50" # Default value if not set
    
                try:
                    weaponTag = weaponReq.attrib['tag']
                except KeyError:
                    weaponTag = ""

                try:
                    weaponOrTag = weaponReq.attrib['ortag']
                except KeyError:
                    weaponOrTag = ""

                try:
                    weaponAndTag = weaponReq.attrib['andtag']
                except KeyError:
                    weaponAndTag = ""
    
                try:
                    weaponNotTag = weaponReq.attrib['nottag']
                except KeyError:
                    weaponNotTag = ""
                
                weaponList = [weaponType, weaponWeight, weaponTag, weaponOrTag, weaponAndTag, weaponNotTag]
                weaponsDataList.append(weaponList)
                weaponList = []    
            classList[index].weaponsList = weaponsDataList       

            # Get the thief flag
            thiefFlag = tree._root[12].attrib['value']
            if thiefFlag == "true":
                classList[index].thiefFlag = True
            else:
                classList[index].thiefFlag = False

            index += 1

        print("Got the following classes...")
        for i in classList:
            print("\t" + i.className)

        print("Character classes imported!\n")
        return classList