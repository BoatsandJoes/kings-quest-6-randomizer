def solve(world):
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
    # TODO Try to solve world. Return empty string if impossible
    result = ""
    inventory = []
    visitedNodes = ["isleOfTheCrown"]
    graph = {
        "isleOfTheCrown": {
            "items": ["coin", "royalRing", "rabbitFoot", "boringBook", "poem", "mint"]
            "edges": [
                {
                    "target": "letter",
                    "requirements": [
                        "brush",
                        "teaCup",
                        "swampOoze",
                        "styx",
                        "feather",
                        "handkerchief",
                        "dagger",
                        ["nail", "skeletonKey"]
                    ]
                }
            ]
        }
        "letter": {
            "items": ["letter"]
            "edges": [
                {
                    "target": "win",
                    "requirements": [
                        "letter",
                        ["mirror", "parentsSaved"],
                        ["mint", "pepperMint", "lampSwitched"]
                    ]
                }
            ]
        }
        "win": {}
    }
    for item in graph["IsleOfTheCrown"]["items"]:
        inventory.append(item)
    # Try to traverse the game and get to the end. TODO respect one-way dives like catacombs
    stuck = False
    while !stuck and visitedNodes.count("win") == 0 :
        stuck = True
        for nodeName in visitedNodes.copy(): #Iterate over a copy so that we can change the list in the loop and not break anything
            node = graph[nodeName]
            for edge in node["edges"]:
                # If we haven't already visited and we fulfill all item requirements
                if visitedNodes.count(edge["target"]) == 0 and invContainsRequirements(inventory, edge["requirements"]):
                    # Visit node and collect its items
                    visitedNodes.append(edge["target"])
                    for item in graph[edge["target"]]["items"]:
                        inventory.append(vanillaItemIds[world[item]]) #Append the string of the item that is actually in that location.
                    stuck = False
    if stuck:
        result = ""
    else:
        result = "Text that will be put in solution spoiler file" #TODO Probably use visitedNodes: they're in order
    return result

def invContainsRequirements(inv, requirements):
    hasItem = False
    for item in requirements:
        hasItem = False
        if type(item) == list:
            for orItem in item:
                if inv.count(orItem) > 0:
                    hasItem = True
                    break
        elif inv.count(item) > 0:
            hasItem = True
        if !hasItem:
            break
    return hasItem