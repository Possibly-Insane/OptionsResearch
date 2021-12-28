import numpy as np
import pyautogui as gui
from mss.windows import MSS as mss

with mss() as sct:
    monitor = {"top": 0, "left": 0, "width": 2560, "height": 1440}
    img = np.array(sct.grab(sct.monitors[1]))
    print(img)