import randomizer
import fileReaderWriter
import sys

config = fileReaderWriter.getConfig()
game = randomizer.createWorld(config)
# todo write game to files: game files, spoiler solution, shop spoiler