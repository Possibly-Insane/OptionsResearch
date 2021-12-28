import numpy as np
from PIL import Image
import imagehash

def identify(image, colour, guess=False):
    #data used for identification
    beige_sure = [[-1, 0, 1, 1, 0,-1,-1, 1,-1,-1], [ 1, 0, 1, 1,-1, 1, 0, 1, 1, 1], [ 1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [-1, 0,-1,-1, 0, 1, 1, 1,-1,-1], [ 0, 1, 1, 0,-1, 1,-1, 1, 1, 1], [ 1, 0,-1,-1, 0,-1,-1,-1,-1,-1], [-1, 0, 1, 1,-1,-1,-1, 1, 1,-1], [ 0,-1,-1, 0, 0, 1, 1, 0,-1, 1], [-1,-1,-1, 1,-1, 1, 1,-1, 1, 0], [-1,-1, 1, 1,-1, 1, 1, 1, 1, 0], [ 0,-1, 1,-1,-1,-1,-1, 0,-1, 1], [ 1,-1,-1,-1, 1,-1, 1,-1, 1,-1], [-1, 1,-1,-1, 1,-1,-1, 0,-1,-1], [-1, 1,-1, 0, 1,-1,-1, 1,-1, 0], [ 1,-1,-1, 1, 1, 1, 1,-1, 1, 1]]
    beige_guess = [[-1, -0.0196, 1, 1, -0.952576, -1, -1, 1, -1, -1], [ 1, 0.4624, 1, 1, -1, 1, -0.0016, 1, 1, 1], [ 1, -0.4356, 0.8464, 0.6724, 0.0196, 1, 1, 1, 1, 1], [-1, -0.0784, -1, -1, -0.5184, 1, 1, 1, -1, -1], [ 0.0484, 1, 1, 0.3844, -1, 1, -1, 1, 1, 1], [ 0.9216, 1, -0.4356, -1, 1, 0.16, 0.7396, -1, -1, -1], [ 1, -0.0016, -1, -1, 0.7744, -1, -1, -1, -1, -1], [-1, -0.09, 1, 1, -1, -1, -1, 1, 1, -1], [ 0.0144, -1, -1, -0.0196, -0.0016, 1, 1, -0.1444, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 0.6724], [-1, -1, 1, 1, -1, 1, 1, 1, 1, -0.7056], [ 0.0484, -1, 1, -1, -1, -1, -1, 0.6084, -1, 1], [ 1, -1, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, 0.0016, -1, -1], [-1, 1, -1, -0.81, 1, -1, -1, 1, -1, 0.1296], [ 1, -1, -1, 1, 1, 1, 1, -1, 1, 1]]
    beige_sure_threshold = np.array([12, 10, 14, 12, 11, 15, 14, 13, 16, 13])
    beige_guess_threshold = np.array([13.0328, 11.0876, 15.282, 13.8864, 13.266576, 15.16, 14.7412, 13.7544, 16, 14.5076])
    white_sure = [[-1, 0, 1, 1, 0,-1,-1, 1,-1,-1], [ 1, 0, 1, 1,-1, 1, 0, 1, 1, 1], [ 1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [-1, 0,-1,-1, 0, 1, 1, 1,-1,-1], [ 0, 1, 1, 0,-1, 1,-1, 0, 1, 1], [ 0, 1, 0,-1, 1, 0, 0, 0,-1,-1], [ 1, 0,-1,-1, 0,-1,-1,-1,-1,-1], [-1,-1, 1, 1,-1,-1,-1, 1, 1,-1], [ 0,-1,-1, 0, 0, 1, 1,-1,-1, 1], [-1,-1,-1, 1,-1, 1, 1,-1, 1, 0], [-1,-1, 1, 1,-1, 1, 1, 1, 1, 0], [ 0,-1, 1,-1,-1,-1,-1, 0,-1, 1], [ 1, 0,-1,-1, 1,-1, 1,-1, 1,-1], [-1, 1,-1,-1, 1,-1,-1, 0,-1,-1], [-1, 1,-1, 0, 1,-1,-1, 1,-1, 0], [ 1,-1,-1, 1, 1, 1, 1,-1, 1, 1]]
    white_guess = [[-1, -0.0576, 1, 1, -0.7056, -1, -1, 1, -1, -1], [ 1, 0.4096, 1, 1, -1, 1, -0.0144, 1, 1, 1], [ 1, -0.4096, 0.6084, 0.49, 0.0784, 1, 1, 1, 1, 1], [-1, -0.4096, -1, -1, -0.5184, 1, 1, 1, -1, -1], [ 0.3136, 1, 1, 0.3844, -1, 1, -1, 0.2304, 1, 1], [ 0.6724, 1, -0.5776, -1, 1, 0.0484, 0.81, -0.7056, -1, -1], [ 1, -0.01, -1, -1, 0.7056, -1, -1, -1, -1, -1], [-1, -1, 1, 1, -1, -1, -1, 1, 1, -1], [-0.0036, -1, -1, -0.0256, 0.0196, 1, 1, -1, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 0.81], [-1, -1, 1, 1, -1, 1, 1, 1, 1, -0.7396], [ 0.1156, -1, 1, -1, -1, -1, -1, 0.3844, -1, 1], [ 1, 0.1156, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, 0.0016, -1, -1], [-1, 1, -1, -0.7056, 1, -1, -1, 1, -1, 0.0784], [ 1, -1, -1, 1, 1, 1, 1, -1, 1, 1]]
    white_sure_threshold = np.array([12, 10, 14, 12, 11, 15, 14, 12, 16, 13])
    white_guess_threshold = np.array([13.1052, 11.412, 15.186, 13.6056, 13.0276, 15.0484, 14.8244, 13.322, 16, 14.628])
    grey_sure = [[-1, -1, 1, 1, 1, -1, -1, 1, -1, -1], [ 1, 0, 1, 1, -1, 1, -1, 1, 1, 1], [ 1, 0, 1, 1, 0, 1, 1, 1, 1, 1], [-1, -1, -1, -1, 0, 1, 1, 1, -1, -1], [-1, 1, 1, 1, -1, 1, -1, 0, 1, 1], [ 1, 1, 0, -1, -1, 1, 0, 0, -1, -1], [ 1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [ 1, -1, 1, 1, -1, -1, -1, 1, 1, -1], [ 1, -1, -1, -1, 0, 1, 1, 1, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 1], [-1, -1, 1, 1, -1, 1, 1, 0, 1, 0], [-1, -1, 1, -1, -1, -1, -1, 1, -1, 1], [ 1, 0, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1], [ 1, 0, -1, 1, 1, 1, 1, 0, 1, 1]]
    grey_guess = [[-1, -1, 1, 1, 1, -1, -1, 1, -1, -1], [ 1, 0.5776, 1, 1, -1, 1, -1, 1, 1, 1], [ 1, -0.0196, 1, 1, -0.0144, 1, 1, 1, 1, 1], [-1, -1, -1, -1, 0.0064, 1, 1, 1, -1, -1], [-1, 1, 1, 1, -1, 1, -1, 0.0196, 1, 1], [ 1, 1, 0.0324, -1, -1, 1, 0.01 , 0.0196, -1, -1], [ 1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [ 1, -1, 1, 1, -1, -1, -1, 1, 1, -1], [ 1, -1, -1, -1, -0.0144, 1, 1, 1, -1, 1], [-1, -1, -1, 1, -1, 1, 1, -1, 1, 1], [-1, -1, 1, 1, -1, 1, 1, 0.5776, 1, -0.4096], [-1, -1, 1, -1, -1, -1, -1, 1, -1, 1], [ 1, -0.8464, -1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, -1, -1, -1], [-1, 1, -1, -1, 1, -1, -1, 1, -1, -1], [ 1, 0.5776, -1, 1, 1, 1, 1, -0.5776, 1, 1]]
    grey_sure_threshold = np.array([16, 12, 15, 16, 13, 16, 15, 12, 16, 15])
    grey_guess_threshold = np.array([16, 14.0212, 15.0324, 16, 13.0352, 16, 15.01, 13.1944, 16, 15.4096])

    #choosing correct data
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

    #variable setup for later
    count = np.zeros(10, dtype=int)

    #image is hashed and hash is translated from hex to binary
    hash = str(imagehash.dhash_vertical(Image.open(image), hash_size=4))
    binary = bin(int(hash, 16))[2:].zfill(16)
    array = np.array(list(binary), dtype=int)

    #scoring of hash
    for n1 in range(16):
        if array[n1] == 0:
            count -= scores[n1]
        else:
            count += scores[n1]

    #checking of scores
    if guess == False:
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