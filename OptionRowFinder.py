import numpy as np
import pyautogui as gui
import matplotlib
import matplotlib.pyplot as plt
from mss.windows import MSS as mss


area = [400, 1615, 248, 905]  #area of screen you want to capture

#screen captured and turned into numpy array
with mss() as sct:
    monitor = {"top": area[0], "left": area[1], "width": area[2], "height": area[3]}
    img = np.array(sct.grab(monitor))

h = img.shape[0]
w = img.shape[1]
lbound = 120    #lower bound for beigecount for a row to be considered as containing text
ubound = 240    #upper bound for beigecount for a row to be considered as containing text
beige = [227, 251, 255, 255]    #BRGA code of beige
beigecount = np.zeros(h, np.int16)
rowpos = np.zeros((32, 3), np.int16)
rowcount = 0
for y in range(h): #iterates through rows of image
    for x in range(w):  #iterates through pixels of row
        if np.all(img[y, x] == beige):
            beigecount[y] += 1  #counts number of beige pixels in row
    if lbound < beigecount[y] < ubound and not lbound < beigecount[y-1] < ubound:
        rowpos[rowcount, 0] = y #records at what row a line of text begins
    elif not lbound < beigecount[y] < ubound and lbound < beigecount[y-1] < ubound:
        rowpos[rowcount, 1] = y #records at what row a line of text ends
        rowcount += 1

for z in range(len(rowpos)):
    rowpos[z, 2] = rowpos[z, 1] - rowpos[z, 0]

count = np.arange(1, h+1)

print("h = ", h)
print("w = ", w)
print(rowpos)

plt.plot(count, beigecount)
plt.show()