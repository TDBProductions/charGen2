class Character:
    """Object used to house the character data"""
    charName = ""
    sex = None
    abilityArray = []
    saveArray = []
    exceptionalStrengthFlag = False
    exceptionalStrengthVal = 0
    charClass = None
    charRace = None
    hp = 0
    height = ""

    toHitBonus = 0
    damageBonus = 0
    openDoorsBonus = 0
    bblgBonus = 0
    acBonus = 0
    thiefFlag = False
    stealBonus = 0
    locksBonus = 0
    trapsBonus = 0
    sneakBonus = 0
    hideBonus = 0
    spellSaveBonus = 0
    alignment = ""
    hpBonus = 0
    gold = 0

    ac = 0

    # Thief skills
    steal = 0
    locks = 0
    traps = 0
    sneak = 0
    hide = 0
    listen = 0
    climb = 0
    read = 0

    weapons = []
    ammo = []
    armor = None

    def __init__(self):
        pass



