import numpy as np
import pyautogui as gui
import matplotlib
import matplotlib.pyplot as plt
from mss.windows import MSS as mss

with mss() as sct:
    monitor = {"top": 0, "left": 0, "width": 2560, "height": 1440}
    img = np.array(sct.grab(sct.monitors[1]))

h = img.shape[0]
w = img.shape[1]
beige = [227, 251, 255, 255]
bcount = np.zeros(h, np.int16)
count = bcount
for y in range(h):
    count[y] = y + 1
    for x in range(w):
        if np.all(img[y, x] == beige):
            bcount[y] += 1

print("h = ", h)
print("w = ", w)
print(bcount)

plt.plot(count, bcount)
plt.show()

#if np.any(img[0, 0] == [60, 60, 60, 255]):
#    print("yes")