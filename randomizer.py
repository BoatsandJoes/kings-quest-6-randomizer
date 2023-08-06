import solver

def createWorld(config):
    solution = ""
    while ("" == solution) {
	    print("Attempting generation...\n")
	    world = shuffleItems(config)
        solution = solver.solve(world)
	}
    result = {
	    "world": world
		"solution": solution
	}
    return result

def shuffleItems(config):
    #TODO make random
	#TODO add logic
    return {
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