import os
import copy
from html.parser import HTMLParser
import codecs
from bs4 import BeautifulSoup

class HtmlFactory(object):
    
    characters = None
    templateHtml = None

    """description of class"""
    def __init__(self, characters):
        self.characters = characters
        self.createOutputFile()
        templateHtml = self.importTemplate()
        #for character in self.characters:
        charHtml = copy.deepcopy(templateHtml)
        charHtml = self.importAbilities(characters[0], charHtml)
        charHtml = self.importClassRaceSex(characters[0], charHtml)
        charHtml = self.importHeightWeight(characters[0], charHtml)
        charHtml = self.importDoorsBblgToHitDamage(characters[0], charHtml)
        charHtml = self.importSaves(characters[0], charHtml)
        charHtml = self.importThiefSkills(characters[0], charHtml)
        charHtml = self.importHpAcAlignment(characters[0], charHtml)
        charHtml = self.importSpells(characters[0], charHtml)
        charHtml = self.importWeaponsArmor(characters[0], charHtml)
        charHtml = self.importItems(characters[0], charHtml)

        print(charHtml)        

        # Write to file
        with open("src\html\TestName.html", "w+") as file:
            file.writelines(str(charHtml))

    def createOutputFile(self):
        # Create the file if it does not already exist
        f = open("src\html\output.html","w+")
        f.close()

    def importTemplate(self):
        with open("src\\html\\template.html","r") as templateFile:
            templateHtmlString = templateFile.read()
        templateHtml = BeautifulSoup(templateHtmlString, "html.parser")
        return templateHtml

    def importClassRaceSex(self, character, charHtml):
        charClass = character.charClass.className
        charRace = character.charRace.raceName
        charSex = character.sex

        classTag = charHtml.find("li", {"id": "class"})
        newClassTag = str(classTag).replace("Class:", "Class: " + str(charClass))
        classTag.replaceWith(BeautifulSoup(newClassTag, "html.parser"))

        raceTag = charHtml.find("li", {"id": "race"})
        newRaceTag = str(raceTag).replace("Race:", "Race: " + str(charRace))
        raceTag.replaceWith(BeautifulSoup(newRaceTag, "html.parser"))

        sexTag = charHtml.find("li", {"id": "sex"})
        newSexTag = str(sexTag).replace("Sex:", "Sex: " + str(charSex))
        sexTag.replaceWith(BeautifulSoup(newSexTag, "html.parser"))
        
        return charHtml

    def importAbilities(self, character, charHtml):
        #Declarations
        strength = character.abilityArray[0]
        wisdom = character.abilityArray[1]
        intelligence = character.abilityArray[2]
        dexterity = character.abilityArray[3]
        constitution = character.abilityArray[4]
        charisma = character.abilityArray[5]

        # Find and replace the tag text with the tag text + attribute value
        strengthTag = charHtml.find("dd", {"id": "strength"})
        newStrengthTag = str(strengthTag).replace("Strength:", "Strength: " + str(strength))
        strengthTag.replaceWith(BeautifulSoup(newStrengthTag, "html.parser"))
        
        wisdomTag = charHtml.find("dd", {"id": "wisdom"})
        newWisdomTag = str(wisdomTag).replace("Wisdom:", "Wisdom: " + str(wisdom))
        wisdomTag.replaceWith(BeautifulSoup(newWisdomTag, "html.parser"))

        intelligenceTag = charHtml.find("dd", {"id": "intelligence"})
        newIntelligenceTag = str(intelligenceTag).replace("Intelligence:", "Intelligence: " + str(intelligence))
        intelligenceTag.replaceWith(BeautifulSoup(newIntelligenceTag, "html.parser"))

        dexterityTag = charHtml.find("dd", {"id": "dexterity"})
        newDexterityTag = str(dexterityTag).replace("Dexterity:", "Dexterity: " + str(dexterity))
        dexterityTag.replaceWith(BeautifulSoup(newDexterityTag, "html.parser"))

        constitutionTag = charHtml.find("dd", {"id": "constitution"})
        newCharismaTag = str(constitutionTag).replace("Constitution:", "Constitution: " + str(constitution))
        constitutionTag.replaceWith(BeautifulSoup(newCharismaTag, "html.parser"))

        charismaTag = charHtml.find("dd", {"id": "charisma"})
        newCharismaTag = str(charismaTag).replace("Charisma:", "Charisma: " + str(charisma))
        charismaTag.replaceWith(BeautifulSoup(newCharismaTag, "html.parser"))

        # Return the updated HTML
        return charHtml

    def importHeightWeight(self, character, charHtml):
        # Declarations
        height = character.height
        weight = character.weight

        # Find and replace the tag text with the tag text + attribute value
        heightTag = charHtml.find("li", {"id": "height"})
        newHeightTag = str(heightTag).replace("Height:", "Height: " + str(height))
        heightTag.replaceWith(BeautifulSoup(newHeightTag, "html.parser"))
        
        weightTag = charHtml.find("li", {"id": "weight"})
        newWeightTag = str(weightTag).replace("Weight:", "Weight: " + str(weight))
        weightTag.replaceWith(BeautifulSoup(newWeightTag, "html.parser"))

        return charHtml

    def importDoorsBblgToHitDamage(self, character, charHtml):
        doors = character.openDoors
        bblg = character.bblg
        toHit = character.toHitBonus
        damage = character.damageBonus

        doorsTag = charHtml.find("li", {"id": "opendoors"})
        newDoorsTag = str(doorsTag).replace("Open Doors:", "Open Doors: " + str(doors))
        doorsTag.replaceWith(BeautifulSoup(newDoorsTag, "html.parser"))

        bblgTag = charHtml.find("li", {"id": "bblg"})
        newBblgTag = str(bblgTag).replace("BB/LG:", "BB/LG: " + str(bblg))
        bblgTag.replaceWith(BeautifulSoup(newBblgTag, "html.parser"))

        toHitTag = charHtml.find("li", {"id": "tohitbonus"})
        newToHitTag = str(toHitTag).replace("To-Hit Bonus:", "To-Hit Bonus: " + str(toHit))
        toHitTag.replaceWith(BeautifulSoup(newToHitTag, "html.parser"))

        damageTag = charHtml.find("li", {"id": "damagebonus"})
        newDamageTag = str(damageTag).replace("Damage Bonus:", "Damage Bonus: " + str(damage))
        damageTag.replaceWith(BeautifulSoup(newDamageTag, "html.parser"))

        return charHtml

    def importSaves(self, character, charHtml):
        poison = character.saveArray[0]
        petrification = character.saveArray[1]
        wand = character.saveArray[2]
        breath = character.saveArray[3]
        spell = character.saveArray[4]

        poisonTag = charHtml.find("dd", {"id": "poison"})
        newPoisonTag = str(poisonTag).replace("Poison:", "Poison: " + str(poison))
        poisonTag.replaceWith(BeautifulSoup(newPoisonTag, "html.parser"))

        petrificationTag = charHtml.find("dd", {"id": "petrification"})
        newPetrificationTag = str(petrificationTag).replace("Petrification:", "Petrification: " + str(petrification))
        petrificationTag.replaceWith(BeautifulSoup(newPetrificationTag, "html.parser"))

        wandTag = charHtml.find("dd", {"id": "wand"})
        newWandTag = str(wandTag).replace("Wand:", "Wand: " + str(wand))
        wandTag.replaceWith(BeautifulSoup(newWandTag, "html.parser"))

        breathTag = charHtml.find("dd", {"id": "breath"})
        newBreathTag = str(breathTag).replace("Breath:", "Breath: " + str(breath))
        breathTag.replaceWith(BeautifulSoup(newBreathTag, "html.parser"))

        spellTag = charHtml.find("dd", {"id": "spell"})
        newSpellTag = str(spellTag).replace("Spell:", "Spell: " + str(spell))
        spellTag.replaceWith(BeautifulSoup(newSpellTag, "html.parser"))

        return charHtml

    def importThiefSkills(self, character, charHtml):
        thiefFlag = character.thiefFlag
        steal = character.steal
        locks = character.locks
        traps = character.traps
        sneak = character.sneak
        hide = character.hide
        listen = character.listen
        climb = character.climb
        read = character.read
    
        # If we have a thief, we need to add the thief skills to the HTML.
        if thiefFlag == True:
            stealTag = charHtml.find("dd", {"id": "steal"})
            newStealTag = str(stealTag).replace("Steal: N/A", "Steal: " + str(steal))
            stealTag.replaceWith(BeautifulSoup(newStealTag, "html.parser"))
                        
            locksTag = charHtml.find("dd", {"id": "locks"})
            newLocksTag = str(locksTag).replace("Locks: N/A", "Locks: " + str(locks))
            locksTag.replaceWith(BeautifulSoup(newLocksTag, "html.parser"))

            trapsTag = charHtml.find("dd", {"id": "traps"})
            newTrapsTag = str(trapsTag).replace("Traps: N/A", "Traps: " + str(traps))
            trapsTag.replaceWith(BeautifulSoup(newTrapsTag, "html.parser"))

            sneakTag = charHtml.find("dd", {"id": "sneak"})
            newSneakTag = str(sneakTag).replace("Sneak: N/A", "Sneak: " + str(sneak))
            sneakTag.replaceWith(BeautifulSoup(newSneakTag, "html.parser"))

            hideTag = charHtml.find("dd", {"id": "hide"})
            newHideTag = str(hideTag).replace("Hide: N/A", "Hide: " + str(hide))
            hideTag.replaceWith(BeautifulSoup(newHideTag, "html.parser"))

            listenTag = charHtml.find("dd", {"id": "listen"})
            newListenTag = str(listenTag).replace("Listen: N/A", "Listen: " + str(listen))
            listenTag.replaceWith(BeautifulSoup(newListenTag, "html.parser"))

            climbTag = charHtml.find("dd", {"id": "climb"})
            newClimbTag = str(climbTag).replace("Climb: N/A", "Climb: " + str(climb))
            climbTag.replaceWith(BeautifulSoup(newClimbTag, "html.parser"))

            readTag = charHtml.find("dd", {"id": "read"})
            newReadTag = str(readTag).replace("Read: N/A", "Read: " + str(read))
            readTag.replaceWith(BeautifulSoup(newReadTag, "html.parser"))

        # If the char does not have thief skills, we remove the tags
        if thiefFlag == False:
            charHtml.find("li", {"id":"thiefSkills"}).decompose()
            for dd in charHtml.find_all("dd", {"subcat":"thiefSkills"}):
                dd.decompose()

        return charHtml
            
    def importHpAcAlignment(self, character, charHtml):
        hp = character.hp
        ac = character.ac
        alignment = character.alignment

        hpTag = charHtml.find("li", {"id": "hp"})
        newHpTag = str(hpTag).replace("HP:", "HP: " + str(hp))
        hpTag.replaceWith(BeautifulSoup(newHpTag, "html.parser"))

        acTag = charHtml.find("li", {"id": "ac"})
        newAcTag = str(acTag).replace("AC:", "AC: " + str(ac))
        acTag.replaceWith(BeautifulSoup(newAcTag, "html.parser"))

        alignmentTag = charHtml.find("li", {"id": "alignment"})
        newAlignmentTag = str(alignmentTag).replace("Alignment:", "Alignment: " + str(alignment))
        alignmentTag.replaceWith(BeautifulSoup(newAlignmentTag, "html.parser"))

        return charHtml

    def importSpells(self, character, charHtml):
        spellsList = character.spells

        # If the character does not have spells, delete the template elements
        if (spellsList == []):
            charHtml.find("li", {"id":"spells"}).decompose()
            #charHtml.find("dd", {"subcat":"spells"}).decompose()
        else:
            counter = 0
            for spell in spellsList:
                # Create a new tag for each spell
                spellTag = charHtml.new_tag("dd")
                spellTag['id'] = ("spell" + str(counter))
                spellTag.string = spell.spellName
                counter += 1

                charHtml.find("li",{"id":"spells"}).insert_after(spellTag)

        return charHtml

    def importWeaponsArmor(self, character, charHtml):
        weapons = character.weapons
        armor = character.armor
        shield = character.shield
        counter = 0

        # Create a new tag using beautiful soup and append it after the weapons header
        for weapon in weapons:
            weaponTag = charHtml.new_tag("dd")
            weaponTag['id'] = ("weapon" + str(counter))
            weaponTag.string = weapon.weaponName
            counter += 1
            charHtml.find("li",{"id":"weapons"}).insert_after(weaponTag)
    
        # Only one armor, so it has a placeholder tag we can replace
        armorTag = charHtml.find("dd", {"id": "armor"})
        newArmorTag = str(armorTag).replace("placeholder", str(armor.armorName))
        armorTag.replaceWith(BeautifulSoup(newArmorTag, "html.parser"))

        # Shield can be none
        if shield is not None:
            shieldTag = charHtml.find("dd", {"id": "shield"})
            newShieldTag = str(shieldTag).replace("placeholder", str(shield.armorName))
            shieldTag.replaceWith(BeautifulSoup(newShieldTag, "html.parser"))         

        # If it is none, we need to decompose the shield tag
        else:
            charHtml.find("dd", {"id":"shield"}).decompose()            

        return charHtml

    def importItems(self, character, charHtml):
       itemsList = character.items
       counter = 0
        
       for item in itemsList:
            itemTag = charHtml.new_tag("dd")
            itemTag['id'] = ("item" + str(counter))
            itemTag.string = item.itemName
            charHtml.find("li",{"id":"items"}).insert_after(itemTag)
            counter += 1

       return charHtml
        