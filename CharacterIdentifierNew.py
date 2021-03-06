import numpy as np
from PIL import Image
import imagehash


def identify(image, srcSet: tuple):
    
    (scores, threshold, guess) = srcSet
    # variable setup for later
    # image is hashed and hash is translated from hex to binary
    hash_value = str(imagehash.dhash_vertical(Image.open(image), hash_size=4))
    binary = bin(int(hash_value, 16))[2:].zfill(16)
    array = np.array(list(binary), dtype=int)

    # scoring of hash
    count = np.zeros(10)
    for n1 in range(16):
        if array[n1] == 0:
            count -= scores[n1]
        else:
            count += scores[n1]

    output = -1  # assigning default value in case of failure
    # checking of scores
    if not guess:
        for n2 in range(10):
            # print(count[n2], threshold[n2])
            if count[n2] == threshold[n2]:
                output = n2
    else:
        adjusted = count / threshold
        high_score = 0
        for n3 in range(10):
            if adjusted[n3] > high_score:
                output = n3
                high_score = adjusted[n3]

    return output

