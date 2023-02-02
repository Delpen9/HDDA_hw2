# Standard Libraries
import numpy as np
import os
import cv2

# Convert to grayscale
from convert_to_grayscale import convert2grayscale

# image segmentation
from k_means_clustering_of_image import image_clustering

if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'images', 'RoseonIce-1.jpg')
    image = cv2.imread(image_path)
    image_grayscale = convert2grayscale(image)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_Rose_grayscale.jpg')
    cv2.imwrite(image_path, image_grayscale)
