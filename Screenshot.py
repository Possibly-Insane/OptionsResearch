import mss
from PIL import Image


with mss.mss() as sct:
    # Get a screenshot of the 1st monitor
    sct_img = sct.grab(sct.monitors[1])

    # Create an Image
    img = Image.new("RGB", sct_img.size)
    
    # Best solution: create a list(tuple(R, G, B), ...) for putdata()
    pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[0::4])
    img.putdata(list(pixels))
    
    # But you can set individual pixels too (slower)
    """
    pixels = img.load()
    for x in range(sct_img.width):
        for y in range(sct_img.height):
             px = sct_img.pixel(x, y)
             grey = (px[0]+px[1]+px[2])//3
             pxx = [255, 255, 255]
             if grey < 191:
                 pxx[0] = grey
                 pxx[1] = grey
                 pxx[2] = grey
             
             pxxx = (pxx[0], pxx[1], pxx[2])
             pixels[x, y] = pxxx
    """
    # Show it!
    #img.show()
    output = "verylarge2.png"
    img.save(output)
    print(output)