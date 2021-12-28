import numpy as np
from PIL import Image
import imagehash
from pandas import read_csv



def identify(image, colour, guess=False):
    # data used for identification
    beige_sure = get_array("data/beige_sure.csv")
    beige_sure_threshold = get_array("data/beige_sure_threshold.csv")
    beige_guess = get_array("data/beige_guess.csv")
    beige_guess_threshold = get_array("data/beige_guess_threshold.csv")

    white_sure = get_array("data/white_sure.csv")
    white_guess = get_array("data/white_guess.csv")
    white_sure_threshold = get_array("data/white_sure_threshold.csv")
    white_guess_threshold = get_array("data/white_guess_threshold.csv")

    grey_sure = get_array("data/grey_sure.csv")
    grey_guess = get_array("data/grey_guess.csv")
    grey_sure_threshold = get_array("data/grey_sure_threshold.csv")
    grey_guess_threshold = get_array("data/grey_guess_threshold.csv")

    # choosing correct data
    if colour == "beige":
        if guess == False:
            scores = beige_sure
            threshold = beige_sure_threshold
        else:
            scores = beige_guess
            threshold = beige_guess_threshold
    if colour == "white":
        if guess == False:
            scores = white_sure
            threshold = white_sure_threshold
        else:
            scores = white_guess
            threshold = white_guess_threshold
    if colour == "grey":
        if guess == False:
            scores = grey_sure
            threshold = grey_sure_threshold
        else:
            scores = grey_guess
            threshold = grey_guess_threshold

    # variable setup for later
    count = np.zeros(10, dtype=int)

    # image is hashed and hash is translated from hex to binary
    hash = str(imagehash.dhash_vertical(Image.open(image), hash_size=4))
    binary = bin(int(hash, 16))[2:].zfill(16)
    array = np.array(list(binary), dtype=int)

    # scoring of hash
    for n1 in range(16):
        if array[n1] == 0:
            count -= scores[n1]
        else:
            count += scores[n1]

    # checking of scores
    if not guess:
        for n2 in range(10):
            if count[n2] == threshold[n2]:
                output = n2
    else:
        adjusted = count / threshold
        highscore = 0
        for n3 in range(10):
            if adjusted[n3] > highscore:
                output = n3
                highscore = adjusted[n3]

    return output


def get_array(filename):
    reader = read_csv(filename, header=None)
    return np.array(reader.values.tolist())
