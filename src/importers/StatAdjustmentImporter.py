import xml.etree.ElementTree as ET
import os

class StatAdjustmentImporter:
    """Used to import the stat adjustments into the generator"""

    def __init__(self):
        pass

    def importStatAdjustments():
        print("Importing stat adjustments...")
        # Try to parse the XML.  Catch broken XML and abort.
        try:
            tree = ET.parse("data\StatAdjustments.xml")
        except ET.ParseError:
            print("Import unsuccessful!  Check the file: StatAdjustments.xml")
            input('Press Enter to exit')
            exit(0)

        # Declarations
        statAdjustmentArray = []

        # Strength
        statAdjustmentArray.append(tree._root[0][0].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[0][1].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[0][2].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[0][3].attrib['value'].split(" "))

        # Dexterity
        statAdjustmentArray.append(tree._root[1][0].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[1][1].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[1][2].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[1][3].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[1][4].attrib['value'].split(" "))
        statAdjustmentArray.append(tree._root[1][5].attrib['value'].split(" "))

        # Wisdom
        statAdjustmentArray.append(tree._root[2][0].attrib['value'].split(" "))
        
        # Constituation
        statAdjustmentArray.append(tree._root[3][0].attrib['value'].split(" "))

        print("Stat adjusments imported!\n")
        return statAdjustmentArray
                
            


