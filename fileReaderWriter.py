import shutil
import os

def getConfig():
    #TODO read config from ini file
    return {
	    "hardLogic": true,
	    "shuffleFluids": false
	}

def writeGameToFiles(game):
	readFileFolder = "./gameScripts"
	writeFileFolder = "./src"
	# Read list of game files
	listOfScFilenames = os.listdir(readFileFolder)
	for filename in listOfScFilenames:
		changed = false
		newLines = []
	    if false: #TODO extension is .sc
			rf = open(readFileFolder + "/" + filename, "r", encoding="utf-8")
			oldLines = rf.readlines()
			rf.close()
			for line in oldLines:
				# TODO replace items
				if false: # TODO regex match on line
					newLine = "line with regex-matched string replaced with the shuffled number item id"
					changed = true
				else:
					newLine = line
				newLines.append(newLine)
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