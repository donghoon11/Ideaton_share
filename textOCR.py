import pytesseract
from PIL import Image
import cv2
import requests
import numpy as np
import re
import os


def img2text(img_path):
    image = cv2.imread(img_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = '{}.png'.format(os.getpid())
    cv2.imwrite(filename, gray_image)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor+eng')
    # text = re.sub('[^a-zA-Z가-힣]'," ", text).strip().replace(" ","")
    return text

# if __name__ == '__main__':
#     text = img2text(img_path)
#     print(text)