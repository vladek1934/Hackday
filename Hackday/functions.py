import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#Importing libraries 

a = [0, 1, 1, 1, 0 ,-1, -1, -1]
b = [1, 1, 0, -1, -1, -1, 0 ,1]
weight = [0.299, 0.587, 0.114]

img = Image.open('download.jpg')
gray_img = img.convert('LA')
WIDTH_CONSTANT, HEIGHT_CONSTANT = gray_img.size

def within_boundaries(x, y):
    if (x < 0 or x > WIDTH_CONSTANT or y < 0 or y > HEIGHT_CONSTANT):
        return False
    return True    

def get_darkest_neighbour(x, y):
    darkest = 255
    id = -1
    for i in range(8):
        if (within_boundaries(x + a[i], y + b[i])):
            brightness = gray_img.getpixel((x + a[i], y + a[i]))[0]
            if (darkest > brightness):
                darkest = brightness
                id = i
    return id
def BGR_to_RGB(img):
    n = len(img)
    m = len(img[0])
    print(n, m)
    for i in range(n):
        for j in range(m):
            img[i][j][0], img[i][j][2] = img[i][j][2], img[i][j][0]
    return img

def RGB_to_GRAY(img):
    img = np.array(img)
    print(img.shape)
    new = np.dot(img, weight)
    return new