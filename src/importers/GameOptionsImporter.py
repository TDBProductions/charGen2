import configparser

class GameOptionsImporter:
    def __init__(self):
        pass
        
    def importGameOptions():
        print("Importing game options...")
    
        ## Get the configuration file and load it into memory.
        config = configparser.ConfigParser()
        config.read('config.ini')

        ## Memory structure for holding the dictionary
        gameOptions = {}
        try:
            gameOptions["generatorMode"]            = config['DEFAULT']['generatormode']
            gameOptions["enforceSexAbilities"]      = config['DEFAULT']['enforcesexabilities']
            gameOptions["enforceRacialAbilities"]   = config['DEFAULT']['enforceracialabilities']
            gameOptions["ignoreRaceRestrictions"]   = config['DEFAULT']['ignoreracerestrictions']
            gameOptions["minimumReroll"]            = config['DEFAULT']['minimumreroll']
            gameOptions["enforceFloorValues"]       = config['DEFAULT']['enforcefloorvalues']
            gameOptions["rollMethod"]               = config['DEFAULT']['rollmethod']
            gameOptions["enforceAbilityScores"]     = config['DEFAULT']['enforceabilityscores']
            gameOptions["charGenMode"]              = config['DEFAULT']['chargenmode']
            gameOptions["charactersGenerated"]      = config['DEFAULT']['charactersgenerated']
            gameOptions["basicClassWeight"]         = config['DEFAULT']['basicclassweight']
            gameOptions["prestigeClassWeight"]      = config['DEFAULT']['prestigeclassweight']
            gameOptions["basicClassMin"]            = config['DEFAULT']['basicclassmin']
            gameOptions["prestigeClassMin"]         = config['DEFAULT']['prestigeclassmin']
            gameOptions["basicClassCount"]          = config['DEFAULT']['basicclasscount']
            gameOptions["prestigeClassCount"]       = config['DEFAULT']['prestigeclasscount']
            gameOptions["outputMode"]               = config['DEFAULT']['outputmode']
        except KeyError:
            print("Error in config.ini file...exiting...")
            input("Press Enter to exit")
            exit(0)

        print("Game options imported!\n")
        return gameOptions

        