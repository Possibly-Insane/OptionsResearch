import numpy as np
from PIL import Image
import imagehash
import matplotlib.pyplot as plt
import glob
import scipy.spatial.distance

max = 16
count = np.zeros(10, dtype=int)
data = np.zeros((36, 10, max), dtype=int)
average = np.zeros((10, max), dtype=int)

for n1 in range(10):
    print(n1)
    index = 0
    images = glob.glob('C:/Users/bruno/Documents/Python/Options Research/numbers/15x20/Beige/%s/*.png'%n1)
    for image in images:
        with open(image, 'rb') as file:
            hash = str(imagehash.dhash_vertical(Image.open(file), hash_size=4))
            #hash = str(imagehash.phash(Image.open(file)))
            scale = 16 ## equals to hexadecimal
            num_of_bits = max
            binary = bin(int(hash, scale))[2:].zfill(num_of_bits)
            data[index, n1] = list(binary)
            print(binary)
        count[n1] += 1
        index += 1

for n2 in range(10):
    for n3 in range(max):
        average[n2, n3] = int(round(np.sum(data[:, n2, n3]) / count[n2]))

for n4 in range(len(average)):
    Groups = np.zeros((data.shape[0], data.shape[1]), dtype=int)
    for n5 in range(Groups.shape[0]):
        for n6 in range(Groups.shape[1]):
            if np.sum(data[n5, n6]) != 0:
                Groups[n5, n6] = scipy.spatial.distance.hamming(average[n4], data[n5, n6]) * max + 1
    width = 0.8 / len(Groups)
    Pos = np.array(range(len(Groups[0]))) 
    for i in range(len(Groups)):
        plt.bar(Pos + i * width, Groups[i], width = width)
    plt.show()