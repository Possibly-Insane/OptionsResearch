import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
import glob

data = np.zeros((25, 17, 10))

for n1 in range(10):
    count = 0
    images = glob.glob('C:/Users/bruno/Documents/Python/Options Research/numbers/Beige/%s/*.png'%n1)
    for image in images:
        with open(image, 'rb') as file:
            img = Image.open(file)
            img = np.array(img)
            img = img[:, :, 2]
            Bh = np.average(img, axis=0)
            Bv = np.average(img, axis=1)
            B = np.append(Bh, Bv)
            for n2 in range(25):
                data[n2, count, n1] = B[n2]
        count += 1

"""
width = 0.8 / len(B)
pos = np.array(range(len(B[0])))
for i in range(len(B)):
    plt.bar(pos + i * width, B[i], width = width)
plt.show()
"""
fig, ax = plt.subplots(5, 5)
for n3 in range(25):
    subdata = data[n3]
    width = 0.8 / len(subdata)
    pos = np.array(range(len(subdata[0])))
    for i in range(len(subdata)):
        ax[n3 // 5 - 1, n3 % 5].bar(pos + i * width, subdata[i], width = width)

plt.show()