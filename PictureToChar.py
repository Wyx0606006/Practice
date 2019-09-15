

import numpy as np
from PIL import Image

if __name__=='__main__':
    image_file = 'lena.png'
    height = 100

    img = Image.open(image_file)
    img_width,img_height = img.size
    width = 2 * height * img_width // img_height
    img = img.resize((width,height),Image.ANTIALIAS)
    pixels = np.array(img.convert('L'))
    chars = "MNHQ$OC?7>!:-;. "
    N = len(chars)
    step = 256 // N
    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[pixels[i][j] // step]
        result += '\n'
    with open('text.txt', mode='w') as f:
        f.write(result)
