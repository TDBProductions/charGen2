import xml.etree.ElementTree as ET
import os
from data.Item import Item

class ItemImporter:
    """Used to import the items.xml file into the char gen"""

    def __init__(self):
        pass

    def importItems():
        print("Importing items...")
        # Try to parse the XML.  Catch broken XML and abort.
        try:
            tree = ET.parse("data\Items.xml")
        except ET.ParseError:
            print("Import unsuccessful!  Check the file: Items.xml")
            input('Press Enter to exit')
            exit(0)

        itemList = []
        itemName = ""
        itemCost = 0
        itemCostStr = ""
        itemCategory = ""
        itemWeaponLink = None
        index = 0

        # Outer loop traverses the item categories
        for categoryElement in tree._root:
            itemCategory = categoryElement.attrib['name']

            for itemElement in categoryElement:
                # Get item name
                itemName = itemElement.attrib['name']
                
                # Get item cost
                itemCost = itemElement.attrib['cost']

                # Get item cost str
                itemCostStr = itemElement.attrib['coststr']

                # If the item has a weapon linked to it that is not its name, get that too.
                if (itemElement.find("weapon") != None):
                    itemWeaponLink = itemElement.attrib['weapon']

                itemList.append(Item())
                itemList[index].itemCategory = itemCategory
                itemList[index].itemName = itemName
                itemList[index].itemCost = itemCost
                itemList[index].itemCostStr = itemCostStr
                itemList[index].itemWeaponLink = itemWeaponLink

                index += 1

        print("Got the following items...")
        for i in itemList:
            print("\t" + i.itemName)
        print("Items imported!\n")

        # Return Items
        return itemList
               

