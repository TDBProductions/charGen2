import xml.etree.ElementTree as ET
import os
from data.Spell import Spell

class SpellImporter:
    """Used to import the spells into the char gen"""

    def __init__(self):
        pass

    def importSpells():
        print("Importing armors...")
        # Try to parse the XML.  Catch broken XML and abort.
        try:
            tree = ET.parse("data\Spells.xml")
        except ET.ParseError:
            print("Import unsuccessful!  Check the file: Spells.xml")
            input('Press Enter to exit')
            exit(0)

        # Declarations
        spellsList = []
        spellName = ""
        spellDescription = ""
        spellClass = ""
        spellLevel = 0
        index = 0

        # Outer loop for classes
        for spellClassElement in tree._root.findall("spellclass"):

            # Get the spell class
            spellClass = spellClassElement.attrib['name']

            # Loop over spell levels in class
            for spellLevelElement in spellClassElement:

                # Get the spell level
                spellLevel = spellLevelElement.attrib['level']

                # Loop over spells in spell level
                for spellElement in spellLevelElement:

                    # Get the spell name
                    spellName = spellElement.attrib['name']

                    # Get spell description (in a different tree than spells)
                    for spellElement in tree._root.find('spelldescriptions').findall('spell'):
                        if spellElement.attrib['name'] == spellName:
                            spellDescription = spellElement.find('desc').attrib['value']
                            break
                        
                    spellsList.append(Spell())
                    spellsList[index].spellName = spellName
                    spellsList[index].spellDescription = spellDescription
                    spellsList[index].spellClass = spellClass
                    spellsList[index].spellLevel = spellLevel

                    index += 1
                        
        print("Got the following spells...")
        spellPrinterClass = ""
        spellPrinterLevel = 0
        spellPrinterClassFlag = False
        spellPrinterLevelFlag = False
        for i in spellsList:
            # Get first class
            if (spellPrinterClass == ""):
                spellPrinterClass = i.spellClass
                spellPrinterLevel = 1

            elif (spellPrinterClass != i.spellClass):
                spellPrinterClass = i.spellClass
                spellPrinterClassFlag = False

            if (spellPrinterLevel != i.spellLevel):
                spellPrinterLevel = i.spellLevel
                spellPrinterLevelFlag = False

            if (spellPrinterClassFlag == False):
                print("\t " + i.spellClass)
                spellPrinterClassFlag = True

            if (spellPrinterLevelFlag == False):
                print("\t\tLevel " + i.spellLevel)
                spellPrinterLevelFlag = True

            print("\t\t\t" + i.spellName)

        print("Spells imported!\n")
        return spellsList


