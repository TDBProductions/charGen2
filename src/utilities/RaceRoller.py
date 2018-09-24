import random

class RaceRoller(object):
    """Used for rolling the characters races"""

    def __init__(self):
        pass

    def rollRace(gameData):
        return random.choice(gameData.races)


