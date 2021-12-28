import numpy as np
from PIL import Image
import imagehash


def identify(image, srcSet: tuple):
    (scores, threshold, guess) = srcSet

    # variable setup for later
    count = np.zeros(10)

    # image is hashed and hash is translated from hex to binary
    hash = str(imagehash.dhash_vertical(Image.open(image), hash_size=4))
    binary = bin(int(hash, 16))[2:].zfill(16)
    array = np.array(list(binary), dtype=int)

    # scoring of hash
    for n1 in range(0, 15):
        if array[n1] == 0:
            count -= scores[n1]
        else:
            count += scores[n1]

    output = -1
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

