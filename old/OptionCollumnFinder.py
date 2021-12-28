import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mss.windows import MSS as mss

area = [400, 1024, 32, 905]  #area of screen you want to capture

#screen captured and turned into numpy array
with mss() as sct:
    monitor = {"top": area[0], "left": area[1], "width": area[2], "height": area[3]}
    img = np.array(sct.grab(monitor))

h = img.shape[0]
w = img.shape[1]
lbound = 2    #lower bound for beigecount for a row to be considered as containing text
ubound = 30   #upper bound for beigecount for a row to be considered as containing text
beige = [227, 251, 255, 255]    #BRGA code of beige
beigecount = np.zeros(w, np.int16)
colpos = np.zeros((50, 3), np.int16)
rowcount = 0
for x in range(w): #iterates through rows of image
    for y in range(h):  #iterates through pixels of row
        if np.all(img[y, x] == beige):
            beigecount[x] += 1 #counts number of beige pixels in row
    if beigecount[x] == 0 and beigecount[x-1] > 0:
        colpos[rowcount, 0] = x
    elif beigecount[x] > 0 and beigecount[x-1] == 0:
        colpos[rowcount, 1] = x
        rowcount += 1


for z in range(len(colpos)):
    colpos[z, 2] = colpos[z, 1] - colpos[z, 0]

count = np.arange(1, w+1)

print("h = ", h)
print("w = ", w)
print(colpos)

plt.plot(count, beigecount)
#plt.show()