import numpy as np
import os
import cv2

from convert_to_grayscale import convert2grayscale
from add_gaussian_noise import add_gaussian_noise
from salt_and_pepper_noise import salt_and_pepper

if __name__ == '__main__':
    file_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'images', 'theAlps-1.jpg'))
    image = cv2.imread(file_path)

    # Part A
    image_grayscale = convert2grayscale(image)

    image_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'output', 'p1_a_grayscale.jpg'))
    cv2.imwrite(image_path, image_grayscale)

    # Part B.1
    image_gaussian_noise = add_gaussian_noise(image_grayscale)

    image_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'output', 'p1_b_1_gaussian.jpg'))
    cv2.imwrite(image_path, image_gaussian_noise)

    # Part B.2
    image_salt_and_pepper_noise = salt_and_pepper(image_grayscale)

    image_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'output', 'p1_b_2_salt_and_pepper.jpg'))
    cv2.imwrite(image_path, image_salt_and_pepper_noise)

    


