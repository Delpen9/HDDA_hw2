import numpy as np
import os
import cv2

from convert_to_grayscale import convert2grayscale

if __name__ == '__main__':
    file_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'images', 'theAlps-1.jpg'))
    image = cv2.imread(file_path)

    image_grayscale = convert2grayscale(image)

    image_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'output', 'p1_a_grayscale.jpg'))
    cv2.imwrite(image_path, image_grayscale)

    