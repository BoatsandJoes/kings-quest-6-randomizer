import shutil
import os
import re

def getConfig():
    #TODO read config from ini file
    return {
        "hardLogic": True,
        "shuffleFluids": False,
        "itemsToNotShuffle": [
            "nail",
            "boringBook",
            "deadMansCoin",
            "newLamp"
        ]
    }

def writeGameToFiles(game):
    # Map of vanilla item id key to string value
    vanillaItemIds = {
        0: "map",
        1: "boringBook",
        2: "brick",
        3: "brush",
        4: "hair",
        5: "clothes",
        6: "coal",
        7: "deadMansCoin",
        8: "dagger",
        9: "coin",
        10: "egg",
        11: "skull",
        12: "feather",
        13: "flower",
        14: "flute",
        15: "gauntlet",
        16: "cassimaHair",
        17: "handkerchief",
        18: "holeInTheWall",
        19: "huntersLamp",
        20: "letter",
        21: "lettuce",
        22: "milk",
        23: "mint",
        24: "mirror",
        25: "newLamp",
        26: "nail",
        27: "nightingale",
        28: "ticket",
        29: "participle",
        30: "pearl",
        31: "pepperMint",
        32: "note",
        33: "potion",
        34: "rabbitFoot",
        35: "ribbon",
        36: "riddleBook",
        37: "ring",
        38: "rose",
        39: "royalRing",
        40: "sacredWater",
        41: "scarf",
        42: "scythe",
        43: "shield",
        44: "skeletonKey",
        45: "spellBook",
        46: "teaCup",
        47: "poem",
        48: "tinderBox",
        49: "tomato",
        50: "sentence",
        51: "ink"
    }
    # Map of vanilla item id to vanilla verb id for that item
    verbs = {
        0: 12,
        1: 42,
        2: 39,
        3: 29,
        4: 15,
        5: 45,
        6: 46,
        7: 7,
        8: 8,
        9: 40,
        10: 19,
        11: 51,
        12: 30,
        13: 47,
        14: 31,
        15: 48,
        16: 18,
        17: 50,
        18: 25,
        19: 43,
        20: 61,
        21: 52, #Melting is 53, melted 54
        22: 62,
        23: 63,
        24: 13,
        25: 96, #One of these 57 58 59 60 96 56
        26: 64,
        27: 37,
        28: 49,
        29: 94,
        30: 66,
        31: 67,
        32: 65,
        33: 14,
        34: 68,
        35: 33,
        36: 27,
        37: 69,
        38: 71,
        39: 70,
        40: 24,
        41: 72,
        42: 16,
        43: 17,
        44: 35,
        45: 28,
        46: 44,
        47: 32,
        48: 20,
        49: 34,
        50: 85,
        51: 83
    }
    # Map of item string key to vanilla owner id for that item
    vanillaOwners = {
        "map": 280,
        "boringBook": 270,
        "brick": 510,
        "brush": 280,
        "hair": 530,
        "clothes": 540,
        "coal": 560,
        "deadMansCoin": 430,
        "dagger": 440,
        "coin": 200,
        "egg": 490,
        "skull": 415,
        "feather": 300,
        "flower": 300,
        "flute": 280,
        "gauntlet": 650,
        "cassimaHair": 210,
        "handkerchief": 680,
        "holeInTheWall": 480,
        "huntersLamp": 520,
        "letter": 780,
        "lettuce": 480,
        "milk": 470,
        "mint": 280,
        "mirror": 540,
        "newLamp": 240,
        "nail": 880, #may be 0 actually; nail owner is special and I haven't fully understood how it works
        "nightingale": 280,
        "ticket": 600,
        "participle": 500,
        "pearl": 450,
        "pepperMint": 390,
        "note": 210,
        "potion": 480,
        "rabbitFoot": 290,
        "ribbon": 210,
        "riddleBook": 460,
        "ring": 540,
        "rose": 530, #Don't know why this is different from brick. I double checked it though; it's correct
        "royalRing": 200,
        "sacredWater": 380,
        "scarf": 490,
        "scythe": 560,
        "shield": 408,
        "skeletonKey": 670,
        "spellBook": 270,
        "teaCup": 480,
        "poem": 270,
        "tinderBox": 280,
        "tomato": 480,
        "sentence": 450,
        "ink": 240
    }
    # Map that helps replace item owners
    # The game initializes each item with its starting room: for example, royalRing and coin are owned by room 200, the beach
    # Let's say for example that coin is replaced with map, which is normally owned by room 280, the shop
    # We have to change map to be owned by the vanilla owner of the item that it is replacing.
    # This is the converse of the normal replacement, where we replace coin with the map id: we are now replacing map with a coin id.
    owners = dict(vanillaOwners) # Clone to keep vanilla ids for any unshuffled items. Others will be overwritten
    for key in game["world"].keys():
        stringKeyForReplacingItem = vanillaItemIds[game["world"][key]] #look up item string based on ID
        owners[stringKeyForReplacingItem] = vanillaOwners[key] # String key for replacing item: owner room ID for replaced item
    
    readFileFolder = "./gameScripts"
    writeFileFolder = "./src"
	# Delete output folder and recreate
    if os.path.exists(writeFileFolder):
        deleteFolderRecursive(writeFileFolder)
    os.makedirs(writeFileFolder)
    # Read list of game files
    listOfScFilenames = os.listdir(readFileFolder)
    for filename in listOfScFilenames:
        changed = False
        newLines = []
        if re.search("\.sc$", filename): # Look only in files with extension .sc
            rf = open(readFileFolder + "/" + filename, "r", encoding="utf-8")
            oldLines = rf.readlines()
            rf.close()
            # Replace strings. Check for three types of strings, looping the check of each type until there are no more matches to replace, then moving on.
            for line in oldLines:
                # replace owner
                match = True
                while match:
                    match = re.search("([A-Za-z]*)OwnerReplacement", line)
                    if match:
                        id = owners[match.group(1)] # Look up shuffled owner id
                        line = re.sub("[A-Za-z]*OwnerReplacement", str(id), line)
                        changed = True
                # replace verb
                match = True
                while match:
                    match = re.search("([A-Za-z]*)VerbReplacement", line)
                    if match:
                        id = verbs[game["world"][match.group(1)]] # Look up verb id for shuffled item id
                        line = re.sub("[A-Za-z]*VerbReplacement", str(id), line)
                        changed = True
                # replace items (after owners and verbs, because this regex would also match those strings. Just a design quirk)
                match = True
                while match:
                    match = re.search("([A-Za-z]*)Replacement", line)
                    if match:
                        id = game["world"][match.group(1)] # Get shuffled item id based on string key
                        line = re.sub("[A-Za-z]*Replacement", str(id), line)
                        changed = True
                newLines.append(line)
        if changed:
            # Write modified file
            wf = open(writeFileFolder + "/" + filename, "w", encoding="utf-8")
            wf.writelines(newLines)
            wf.close()
        else:
            # Copy unmodified file
            shutil.copy2(readFileFolder + "/" + filename, writeFileFolder + "/" + filename)
    # TODO write spoiler log with solution and item list
    # TODO write spoiler log for just the shopkeeper cheap trade items
    return

def deleteFolderRecursive(writeFileFolder):
    for filename in os.listdir(writeFileFolder):
        path = os.path.join(writeFileFolder, filename)
        if os.path.isfile(path):
            os.remove(path)
        else:
            deleteFolderRecursive(path)
    os.rmdir(writeFileFolder)