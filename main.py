import randomizer
import fileReaderWriter
import sys

config = fileReaderWriter.getConfig()
game = randomizer.createWorld(config)
fileReaderWriter.writeGameToFiles(game)