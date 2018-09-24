import xml.etree.ElementTree as ET
import os
from data.ThiefSkills import ThiefSkills

class ThiefSkillImporter(object):
    """Used to parse the xml data for the Thief Skills"""
     
    def __init__(self):
        pass

    def importThiefSkills():
        print("Importing Thief Skills...")
        # Try to parse the XML.  Catch broken XML and abort.
        try:
            tree = ET.parse("data\ThiefSkills.xml")
        except ET.ParseError:
            print("Import unsuccessful!  Check the file: ThiefSkills.xml")
            input('Press Enter to exit')
            exit(0)

        
        # Declarations
        thiefSkills = ThiefSkills()

        for skillElement in tree._root:
            # Get skill name
            skillName = skillElement.attrib['name']
            skillValue = skillElement.attrib['value']
            if skillName == "steal":
                thiefSkills.steal = skillValue
            elif skillName == "locks":
                thiefSkills.locks = skillValue
            elif skillName == "traps":
                thiefSkills.traps = skillValue
            elif skillName == "sneak":
                thiefSkills.sneak = skillValue
            elif skillName == "hide":
                thiefSkills.hide = skillValue
            elif skillName == "listen":
                thiefSkills.listen = skillValue
            elif skillName == "climb":
                thiefSkills.climb = skillValue
            elif skillName == "read":
                thiefSkills.read = skillValue
        print("Got the following skill values...")
        print("\tSteal: " + str(thiefSkills.steal))
        print("\tLocks: " + str(thiefSkills.locks)) 
        print("\tTraps: " + str(thiefSkills.traps)) 
        print("\tSneak: " + str(thiefSkills.sneak)) 
        print("\tHide: " + str(thiefSkills.hide)) 
        print("\tListen: " + str(thiefSkills.listen)) 
        print("\tClimb: " + str(thiefSkills.climb)) 
        print("\tRead: " + str(thiefSkills.read)) 
        print("Thief skill import successful!")
    
        return thiefSkills

