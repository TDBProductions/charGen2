import xml.etree.ElementTree as ET
import os
from data.Armor import Armor

class ArmorImporter(object):
    """Used to parse the XML of the Armor XML file into the generator"""

    def __init__(self):
        pass

    def importArmor():
        print("Importing armors...")
        # Try to parse the XML.  Catch broken XML and abort.
        try:
            tree = ET.parse("data\Armor.xml")
        except ET.ParseError:
            print("Import unsuccessful!  Check the file: Armor.xml")
            input('Press Enter to exit')
            exit(0)

        
        # Declarations for ease of reading
        armorList = []
        armorClass = ""
        armor = ""
        ac = 0
        char = []
        index = 0
        # Outter loop traverses armor classes (heaviest, heavy, medium, light, wizard)
        for armorClassElement in tree._root:
            # Get Armor Class name
            armorClass = armorClassElement.attrib['name']
            # Middle loop traverses individual armor pieces (Plate Armor, scale mail, etc.)
            for armorElement in armorClassElement:
                # Get armor name and AC
                armorName = armorElement.attrib['name']
                ac = armorElement.attrib['ac']
                # Inner loop traverses armor characteristics (Heavy, loud, metallic, etc.)
                for charElement in armorElement:
                    char.append(charElement.attrib['name'])

                # Create a new armor object and set attributes
                armorList.append(Armor())
                armorList[index].armorClass = armorClass
                armorList[index].armorName = armorName
                armorList[index].ac = int(ac)
                armorList[index].characteristics = char

                # Reset variables
                char = []

                index += 1

        # Print success statements
        print("Got the following armor pieces...")
        for i in armorList:
            print("\t" + i.armorName)
        print("Armor imported!\n")
        return armorList
