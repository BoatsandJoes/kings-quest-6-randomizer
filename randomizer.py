import solver
import random

def createWorld(config):
    solution = ""
    while ("" == solution):
        print("Attempting generation...\n")
        world = shuffleItems(config)
        solution = solver.solve(world)
    result = {
        "world": world,
        "solution": solution
    }
    return result

def shuffleItems(config):
    random.seed()
    vanillaItems = {
        "map": 0,
        "boringBook": 1,
        "brick": 2,
        "brush": 3,
        "hair": 4,
        "clothes": 5,
        "coal": 6,
        "deadMansCoin": 7,
        "dagger": 8,
        "coin": 9,
        "egg": 10,
        "skull": 11,
        "feather": 12,
        "flower": 13,
        "flute": 14,
        "gauntlet": 15,
        "cassimaHair": 16,
        "handkerchief": 17,
        "holeInTheWall": 18,
        "huntersLamp": 19,
        "letter": 20,
        "lettuce": 21,
        "milk": 22,
        "mint": 23,
        "mirror": 24,
        "newLamp": 25,
        "nail": 26,
        "nightingale": 27,
        "ticket": 28,
        "participle": 29,
        "pearl": 30,
        "pepperMint": 31,
        "note": 32,
        "potion": 33,
        "rabbitFoot": 34,
        "ribbon": 35,
        "riddleBook": 36,
        "ring": 37,
        "rose": 38,
        "royalRing": 39,
        "sacredWater": 40,
        "scarf": 41,
        "scythe": 42,
        "shield": 43,
        "skeletonKey": 44,
        "spellBook": 45,
        "teaCup": 46,
        "poem": 47,
        "tinderBox": 48,
        "tomato": 49,
        "sentence": 50,
        "ink": 51
    }
    itemIdsToRandomize = []
    locationsToRandomize = []
    for key in vanillaItems.keys():
        if config["itemsToNotShuffle"].count(key) == 0:
            itemIdsToRandomize.append(vanillaItems[key])
            locationsToRandomize.append(key)
    result = dict(vanillaItems) # Clone to keep vanilla ids for any unshuffled items. Others will be overwritten
    
    if locationsToRandomize.count("map") > 0:
        # Map is a really critical item, so it's the first bit of logic that I'm writing for the randomizer
        possibleMapLocations = []
        possibleMapLocations = addToList(possibleMapLocations, config["itemsToNotShuffle"], "royalRing", 1)
        possibleMapLocations = addToList(possibleMapLocations, config["itemsToNotShuffle"], "coin", 1)
        possibleMapLocations = addToList(possibleMapLocations, config["itemsToNotShuffle"], "rabbitFoot", 1)
        possibleMapLocations = addToList(possibleMapLocations, config["itemsToNotShuffle"], "boringBook", 1)
        possibleMapLocations = addToList(possibleMapLocations, config["itemsToNotShuffle"], "poem", 1)
        possibleMapLocations = addToList(possibleMapLocations, config["itemsToNotShuffle"], "mint", 1)
        #ignoring spellBook, ink, map, and the 4 counter item locations. Let's keep this version simple for now.
        result[possibleMapLocations[random.randrange(0, len(possibleMapLocations))]] = 0
        itemIdsToRandomize.remove(0)
        locationsToRandomize.remove("map")
    
    for location in locationsToRandomize:
        #TODO add logic
        result[location] = itemIdsToRandomize.pop(random.randrange(0, len(itemIdsToRandomize)))
    return result

def addToList(list, notAllowedList, itemToAdd, count):
    if notAllowedList.count(itemToAdd) == 0:
        for i in range(0, count):
            list.append(itemToAdd)
    return list