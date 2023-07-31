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
    return {
		"map": 0,
		"boringBook": 1
	}