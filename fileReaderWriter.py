import shutil
import os
import re

def getConfig():
    #TODO read config from ini file
    return {
	    "hardLogic": true,
	    "shuffleFluids": false
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
	# Map of vanilla item id to vanilla verb id for that item TODO
	verbs = {
	    0: ,
		1: ,
		2: ,
	    3: 29,
		4: ,
		5: ,
	    6: ,
	    7: ,
	    8: ,
	    9: ,
	    10: ,
	    11: ,
	    12: ,
	    13: ,
	    14: 31,
	    15: ,
	    16: ,
	    17: ,
	    18: ,
	    19: ,
	    20: ,
	    21: ,
	    22: ,
	    23: ,
	    24: ,
	    25: ,
	    26: ,
	    27: 37,
	    28: ,
	    29: ,
	    30: ,
	    31: ,
	    32: ,
	    33: ,
	    34: ,
	    35: ,
	    36: ,
	    37: ,
	    38: ,
	    39: ,
	    40: ,
	    41: ,
	    42: ,
	    43: ,
	    44: ,
	    45: ,
	    46: ,
	    47: ,
	    48: 20,
	    49: ,
	    50: ,
	    51: 
	}
	# Map of item string key to vanilla owner id for that item TODO
	vanillaOwners = {
	    "map": 280,
		"boringBook": 
		"brick": 
		"brush": 280
		"hair": 
		"clothes": 
		"coal": 
		"deadMansCoin": 
		"dagger": 
		"coin": 200
		"egg": 
		"skull": 
		"feather": 
		"flower": 
		"flute": 280
		"gauntlet": 
		"cassimaHair": 
		"handkerchief": 
		"holeInTheWall": 
		"huntersLamp": 
		"letter": 
		"lettuce": 
		"milk": 
		"mint": 
		"mirror": 
		"newLamp": 
		"nail": 
		"nightingale": 280
		"ticket": 
		"participle": 
		"pearl": 
		"pepperMint": 
		"note": 
		"potion": 
		"rabbitFoot": 
		"ribbon": 
		"riddleBook": 
		"ring": 
		"rose": 
		"royalRing": 200
		"sacredWater": 
		"scarf": 
		"scythe": 
		"shield": 
		"skeletonKey": 
		"spellBook": 
		"teaCup": 
		"poem": 
		"tinderBox": 280
		"tomato": 
		"sentence": 
		"ink": 
	}
    # Map that helps replace item owners
	# The game initializes each item with its starting room: for example, royalRing and coin are owned by room 200, the beach
	# Let's say for example that coin is replaced with map, which is normally owned by room 280, the shop
	# We have to change map to be owned by the vanilla owner of the item that it is replacing.
	# This is the converse of the normal replacement, where we replace coin with the map id: we are now replacing map with a coin id.
    owners = {}
	for key in game["world"].keys():
	    stringKeyForReplacingItem = vanillaItemIds[game["world"][key]] #look up item string based on ID
	    owners[stringKeyForReplacingItem] = vanillaOwners[key] # String key for replacing item: owner room ID for replaced item
	
	readFileFolder = "./gameScripts"
	writeFileFolder = "./src"
	# Read list of game files
	listOfScFilenames = os.listdir(readFileFolder)
	for filename in listOfScFilenames:
		changed = false
		newLines = []
	    if re.search("\.sc$", filename): # Look only in files with extension .sc
			rf = open(readFileFolder + "/" + filename, "r", encoding="utf-8")
			oldLines = rf.readlines()
			rf.close()
			# Replace strings. Check for three types of strings, looping the check of each type until there are no more matches to replace, then moving on.
			for line in oldLines:
				# replace owner
				match = true
				while match:
					match = re.search("([A-Za-z]*)OwnerReplacement", line)
					if match:
						id = owners[match.group(1)] # Look up shuffled owner id
						line = re.sub("[A-Za-z]*OwnerReplacement", id, line)
						changed = true
				# replace verb
				match = true
				while match:
					match = re.search("([A-Za-z]*)VerbReplacement", line)
					if match:
						id = verbs[game["world"][match.group(1)]] # Look up verb id for shuffled item id
						line = re.sub("[A-Za-z]*VerbReplacement", id, line)
						changed = true
				# replace items (after owners and verbs, because this regex would also match those strings. Just a design quirk)
				match = true
				while match:
					match = re.search("([A-Za-z]*)Replacement", line)
					if match:
						id = game["world"][match.group(1)] # Get shuffled item id based on string key
						line = re.sub("[A-Za-z]*Replacement", id, line)
						changed = true
				newLines.append(line)
		if changed:
			# Write modified file
			wf = open(writeFileFolder + "/" + filename, "w", encoding="utf-8")
			wf.writeLines(newLines)
			wf.close()
		else:
			# Copy unmodified file
			shutil.copy2(readFileFolder + "/" + filename, writeFileFolder + "/" + filename)
    # TODO write spoiler log with solution and item list
	# TODO write spoiler log for just the shopkeeper cheap trade items
	return