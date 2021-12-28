import numpy as np
from PIL import Image
import imagehash
import matplotlib.pyplot as plt
import glob
import scipy.spatial.distance

count = np.zeros(10, dtype=int)
data = np.zeros((10, 17, 64), dtype=int)
average = np.zeros((10, 64), dtype=int)

for n1 in range(10):
    index = 0
    images = glob.glob('C:/Users/bruno/Documents/Python/Options Research/numbers/Beige/%s/*.png'%n1)
    for image in images:
        with open(image, 'rb') as file:
            hash = str(imagehash.dhash_vertical(Image.open(file)))
            scale = 16 ## equals to hexadecimal
            num_of_bits = 64
            binary = bin(int(hash, scale))[2:].zfill(num_of_bits)
            data[n1, index] = list(binary)
        count[n1] += 1
        index += 1

for n2 in range(10):
    for n3 in range(64):
        average[n2, n3] = int(round(np.sum(data[n2, :, n3]) / count[n2]))

#print(average)

print(scipy.spatial.distance.hamming(average[0], data[0, 0]) * 64)