from MrData import *
from CharacterIdentifierNew import *

"""
returns tuple. First is number in 0,9
Second is True if result had to be guessed
"""
def get_identified(image_path, dataset: MrData, colour: Colour):
    srcSet = dataset.get_set(colour)
    num = identify(image_path, srcSet)
    if num != -1:
        return num, False
    else:
        srcSetGuess = dataset.get_set(colour, guess=True)
        num = identify(image_path, srcSetGuess)
        return num, True
    