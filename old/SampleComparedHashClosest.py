import numpy as np
from PIL import Image
import imagehash
import matplotlib.pyplot as plt
import glob
import scipy.spatial.distance

max = 225
count = np.zeros(10, dtype=int)
data = np.zeros((17, 10, max), dtype=int)
average = np.zeros((10, max), dtype=int)

for n1 in range(10):
    index = 0
    images = glob.glob('C:/Users/bruno/Documents/Python/Options Research/numbers/10x15/White/%s/*.png'%n1)
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

for n2 in range(10):
    for n3 in range(max):
        average[n2, n3] = int(round(np.sum(data[:, n2, n3]) / count[n2]))

for n4 in range(10):
    results = np.full(data.shape[0], 290)
    for n5 in range(len(results)):
        if np.sum(data[n5, n4]) != 0:
            for n6 in range(len(average)):
                if (scipy.spatial.distance.hamming(data[n5, n4], average[n6]) * max) < results[n5]:
  results[n5] = n6 + 1
        else:
            results[n5] = 0
    plt.bar(range(len(results)),results)
    plt.show()