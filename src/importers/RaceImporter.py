import xml.etree.ElementTree as ET
import os
from data.PlayerRace import PlayerRace
from data.Feature import Feature


class RaceImporter:
    """Used to parse the XML of the race files for import into the generator"""

    def __init__(self):
        pass

    def importRaces():
        raceList = []
        index = 0

        print("Importing character races...")
        raceFiles = os.listdir("Data\Race")
        for charRace in raceFiles:
            # Try to parse the XML.  Catch broken XML and abort.
            try:
                tree = ET.parse("Data\Race\\" + charRace)
            except ET.ParseError:
                print("Import unsuccessful!  Check the file: " + charRace)
                print("Exiting...")
                input('Press Enter to exit')
                exit(0)

            # Create new instance of PlayerRace per file in the race directory
            raceList.append(PlayerRace())

            # Get Race name, assign to race
            raceList[index].raceName = tree._root.get("name")

            # Get the Min Male ability scores
            minMale = {}
            for i in tree._root[0][0]:
                ability = i.attrib['name']
                value = i.attrib['min']
                minMale[ability] = value
            raceList[index].abilityCapsMinMale = minMale

            # Get the Min Female ability scores
            minFemale = {}
            for i in tree._root[0][1]:
                ability = i.attrib['name']
                value = i.attrib['min']
                minFemale[ability] = value
            raceList[index].abilityCapsMinFemale = minFemale

            # Get the Max Male ability scores
            maxMale = {}
            for i in tree._root[0][0]:
                ability = i.attrib['name']
                value = i.attrib['max']
                maxMale[ability] = value
            raceList[index].abilityCapsMaxMale = maxMale

            # Get the Max Female ability scores
            maxFemale = {}
            for i in tree._root[0][1]:
                ability = i.attrib['name']
                value = i.attrib['max']
                maxFemale[ability] = value
            raceList[index].abilityCapsMaxFemale = maxFemale

            # Get the ability score bonuses
            abilityBonus = {}
            for i in tree._root[1]:
                ability = i.attrib['name']
                value = i.attrib['value']
                abilityBonus[ability] = value
            raceList[index].abilityBonus = abilityBonus

            # Get the race features
            featuresList = []
            for i in tree._root[2]:
                feature = Feature()
                feature.featureName = i.attrib['name']
                feature.featureDesc = i.attrib['description']
                # If the feature has child nodes, these will affect a stat.
                if (i.find("affectedStat") != None):
                    feature.affectedStat = i[0].attrib['name']
                    feature.affectedEff = i[0][0].attrib['effect']
                    feature.affectedVal = i[0][0].attrib['value']

                featuresList.append(feature)
            raceList[index].raceFeatures = featuresList

            # Get the languages
            languageList = []
            for i in tree._root[3]:
                languageList.append(i.attrib['name'])
            raceList[index].languages = languageList
            
            # Get the height, weight and age values
            mWeightList = []
            mHeightList = []
            fWeightList = []
            fHeightList = []

            mHeightList.append(tree._root[4].attrib['value'])
            mHeightList.append(tree._root[4].attrib['minus'])
            mHeightList.append(tree._root[4].attrib['plus'])
            mHeightList.append(tree._root[4].attrib['oweight'])
            mHeightList.append(tree._root[4].attrib['uweight'])            

            mWeightList.append(tree._root[5].attrib['value'])
            mWeightList.append(tree._root[5].attrib['minus'])
            mWeightList.append(tree._root[5].attrib['plus'])
            mWeightList.append(tree._root[5].attrib['oweight'])
            mWeightList.append(tree._root[5].attrib['uweight'])

            fHeightList.append(tree._root[6].attrib['value'])
            fHeightList.append(tree._root[6].attrib['minus'])
            fHeightList.append(tree._root[6].attrib['plus'])
            fHeightList.append(tree._root[6].attrib['oweight'])
            fHeightList.append(tree._root[6].attrib['uweight'])

            fWeightList.append(tree._root[7].attrib['value'])
            fWeightList.append(tree._root[7].attrib['minus'])
            fWeightList.append(tree._root[7].attrib['plus'])
            fWeightList.append(tree._root[7].attrib['oweight'])
            fWeightList.append(tree._root[7].attrib['uweight'])

            raceList[index].mWeight = mWeightList
            raceList[index].mHeight = mHeightList
            raceList[index].fWeight = fWeightList
            raceList[index].fHeight = fHeightList

            # Get the racial save bonuses, split the 'value' into a list
            racialSaveBonuses = {}
            valueList = []
            for save in tree._root[8]:
                valueList = save.attrib['value'].split(" ")
                racialSaveBonuses[save.attrib['name']] = valueList
            raceList[index].saveBonuses = racialSaveBonuses
            
            # Get the racial thief bonuses
            racialThiefBonuses = {}
            for stat in tree._root[9]:
                racialThiefBonuses[stat.attrib['name']] = stat.attrib['value']
            raceList[index].thiefBonuses = racialThiefBonuses

            index += 1

        print("Got the following races...")
        for i in raceList:
            print("\t" + i.raceName)

        print("Character races imported!\n")
        return raceList
