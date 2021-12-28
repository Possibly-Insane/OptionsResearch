import numpy as np
from PIL import Image
import imagehash
import matplotlib.pyplot as plt

def identify_beige(image):
    zero = np.array([[1, 0, 0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 0, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]], dtype=int)
    one = np.array([[0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 1, 0, 1, 1]], dtype=int)
    threshold = np.array([12, 10, 14, 12, 11, 15, 14, 13, 16, 13], dtype = int)
    count = np.zeros(10, dtype=int)
    countcount = count
    estimatevalue = 0
    hash = str(imagehash.dhash_vertical(Image.open(image), hash_size=4))
    binary = bin(int(hash, 16))[2:].zfill(16)
    array = np.array(list(binary), dtype=int)

    for n1 in range(16):
        if array[n1] == 0:
            count += zero[n1]
        else:
            count += one[n1]

    for n2 in range(10):
        if count[n2] == threshold[n2]:
            return n2

    countcount = count / threshold
    for n3 in range(10):
        if countcount[n3] > estimatevalue:
            estimate = n3
            estimatevalue = countcount[n3]
    return estimate