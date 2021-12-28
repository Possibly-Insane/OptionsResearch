import numpy as np
from PIL import Image
import imagehash
import matplotlib.pyplot as plt
import glob
import scipy.spatial.distance

max = 16
count = np.zeros(10, dtype=int)
data = np.zeros((128, 10, max), dtype=int)
result = np.zeros((10, max, 2), dtype=int)
output = np.zeros(max)

for n1 in range(10):
    index = 0
    images = glob.glob('C:/Users/bruno/Documents/Python/Options Research/numbers/10x15/Grey/%s/*.png'%n1)
    for image in images:
        with open(image, 'rb') as file:
            hash = str(imagehash.dhash_vertical(Image.open(file), hash_size=4))
            #hash = str(imagehash.phash(Image.open(file)))
            scale = 16 ## equals to hexadecimal
            num_of_bits = max
            binary = bin(int(hash, scale))[2:].zfill(num_of_bits)
            data[index, n1] = list(binary)
        count[n1] += 1
        index += 1

for n2 in range(data.shape[0]):
    for n3 in range(data.shape[1]):
        if np.sum(data[n2, n3]) != 0:
            for n4 in range(data.shape[2]):
                if data[n2, n3, n4] == 0:
  result[n3, n4, 0] += 1
                else:
  result[n3, n4, 1] += 1

for n5 in range(len(result)):
    for n6 in range(len(output)):
        if result[n5, n6, 1] == 0:
            output[n6] = 0
        elif result[n5, n6, 0] == 0:
            output[n6] = 1
        else:
            rounded = np.round(result[n5, n6, 1] / (np.sum(result[n5, n6, :])), decimals=2)
            if rounded == 0:
                output[n6] = 0.01
            elif rounded == 1:
                output[n6] = 0.99
            else:
                output[n6] = rounded
    print(n5)
    print(output)

