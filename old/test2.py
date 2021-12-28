import numpy as np
import pyautogui as gui
import matplotlib
import matplotlib.pyplot as plt
from mss.windows import MSS as mss


area = [400, 0, 2560, 650]  #area of screen you want to capture

#screen captured and turned into numpy array
with mss() as sct:
    monitor = {"top": area[0], "left": area[1], "width": area[2], "height": area[3]}
    img = np.array(sct.grab(monitor))

h = img.shape[0]
w = img.shape[1]
lbound = 20    #lower bound for beigecount for a row to be considered as containing text
ubound = 227   #upper bound for beigecount for a row to be considered as containing text
beige = [227, 251, 255, 255]    #BRGA code of beige
beigecount = np.zeros(w, np.int16)
rowpos = np.zeros((15, 3), np.int16)
rowcount = 0
for x in range(w): #iterates through rows of image
    for y in range(h):  #iterates through pixels of row
        if np.all(img[y, x] == beige):
            beigecount[x] += 1 #counts number of beige pixels in row
    if lbound < beigecount[x] < ubound and not lbound < beigecount[x-1] < ubound:
        rowpos[rowcount, 0] = x + area[1]  #records at what row a line of text begins
    elif not lbound < beigecount[x] < ubound and lbound < beigecount[x-1] < ubound:
        rowpos[rowcount, 1] = x + area[1]  #records at what row a line of text ends
        rowcount += 1

for z in range(len(rowpos)):
    rowpos[z, 2] = rowpos[z, 1] - rowpos[z, 0]

count = np.arange(1, w+1)

print("h = ", h)
print("w = ", w)
print(rowpos)

cut = beigecount[312:322]
print(cut)

plt.plot(count, beigecount)
#plt.show()