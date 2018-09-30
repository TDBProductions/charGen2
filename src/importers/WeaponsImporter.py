import xml.etree.ElementTree as ET
import os
from data.Weapon import Weapon

class WeaponsImporter:
    """Used to parse the XML of the Weapon XML file into the generator"""

    def __init__(self):
        pass

    def importWeapons():
        print("Importing weapons...")
        # Try to parse the XML.  Catch broken XML and abort.
        try:
            tree = ET.parse("data\Weapons.xml")
        except ET.ParseError:
            print("Import unsuccessful!  Check the file: Weapons.xml")
            input('Press Enter to exit')
            exit(0)

        # Declarations for ease of reading
        weaponsList = []
        weaponName = ""
        weaponDamage = ""
        weaponType = ""
        weaponSize = ""
        weaponTagsString = ""
        weaponTags = []
        index = 0

        for weaponsElement in tree._root:

            # Get weapon name
            weaponName = weaponsElement.attrib['name']

            # Get weapon damage
            weaponDamage = weaponsElement.attrib['damage']

            # Get weapon type
            weaponType = weaponsElement.attrib['armstype']
    
            # Get a list of the weapon tags
            weaponTagsString = weaponsElement.attrib['tags']
            weaponTags = weaponTagsString.split(" ")

            # Get Weapon Size TODO weapon size in XML
            # weaponSize = weaponsElement.attrib['size']
            
            # Import into object
            weaponsList.append(Weapon())
            weaponsList[index].weaponName = weaponName
            weaponsList[index].weaponDamage = weaponDamage
            weaponsList[index].weaponType = weaponType
            weaponsList[index].weaponTags = weaponTags
            #weaponsList[index].weaponSize = weaponSize

            index += 1

        print("Got the following weapons...")
        for i in weaponsList:
            print("\t" + i.weaponName)
        print("Weapons imported!\n")
        return weaponsList


        



