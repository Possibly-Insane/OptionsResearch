import numpy as np
from PIL import Image
from mss.windows import MSS as mss

offset = 15
area = [400, 0, 2560, 905]  #area of screen you want to capture

#screen captured and turned into numpy array
with mss() as sct:
    monitor = {"top": area[0], "left": area[1], "width": area[2], "height": area[3]}
    img = np.array(sct.grab(monitor))

h = img.shape[0]
w = img.shape[1]
lbound = 400    #lower bound for beigecount for a row to be considered as containing text
ubound = 950    #upper bound for beigecount for a row to be considered as containing text
beige = [227, 251, 255, 255]    #BRGA code of beige
beigecount = np.zeros(h, np.int16)
rowpos = np.zeros((32), np.int16)
rowcount = 0
for y in range(h): #iterates through rows of image
    for x in range(w):  #iterates through pixels of row
        if np.all(img[y, x] == beige):
            beigecount[y] += 1  #counts number of beige pixels in row
    if lbound < beigecount[y] < ubound and not lbound < beigecount[y-1] < ubound:
        rowpos[rowcount] = y #records at what row a line of text begins
        rowcount += 1

colpos = [870, 1058, 1510, 1698, 1887]
ch = 15
cw = 10

count = 1 + 160*offset

for cy in range(len(rowpos)):
    for cx in range(len(colpos)):
        crop = img[rowpos[cy]:rowpos[cy] + ch, colpos[cx]:colpos[cx] + cw]
        export = Image.fromarray(crop)
        name = "%s.png"%count
        export = export.save(name)
        count += 1