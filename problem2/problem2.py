# Standard Libraries
import numpy as np
import os
import cv2

# Convert to grayscale
from convert_to_grayscale import convert2grayscale

# Edge detection
from edge_detection_sobel import sobel_edge_detection
from edge_detection_prewitt import prewitt_edge_detection
from edge_detection_laplacian import laplacian_of_gaussian_edge_detection
from edge_detection_difference_of_gaussians import difference_of_gaussian_edge_detection

if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'images', 'Eagle-1.jpg')
    image = cv2.imread(image_path)
    image_grayscale = convert2grayscale(image)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_Eagle_grayscale.jpg')
    cv2.imwrite(image_path, image_grayscale)

    # Part 1
    image_sobel_thresh_10 = sobel_edge_detection(image_grayscale, 10)
    image_sobel_thresh_50 = sobel_edge_detection(image_grayscale, 50)
    image_sobel_thresh_100 = sobel_edge_detection(image_grayscale, 100)
    image_sobel_thresh_150 = sobel_edge_detection(image_grayscale, 150)
    image_sobel_thresh_200 = sobel_edge_detection(image_grayscale, 200)
    image_sobel_thresh_255 = sobel_edge_detection(image_grayscale, 255)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_10.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_10)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_50.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_50)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_100.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_100)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_150.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_150)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_200.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_200)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_255.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_255)

    # Part 2
    image_prewitt_thresh_10 = prewitt_edge_detection(image_grayscale, 10)
    image_prewitt_thresh_50 = prewitt_edge_detection(image_grayscale, 50)
    image_prewitt_thresh_100 = prewitt_edge_detection(image_grayscale, 100)
    image_prewitt_thresh_150 = prewitt_edge_detection(image_grayscale, 150)
    image_prewitt_thresh_200 = prewitt_edge_detection(image_grayscale, 200)
    image_prewitt_thresh_255 = prewitt_edge_detection(image_grayscale, 255)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_10.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_10)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_50.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_50)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_100.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_100)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_150.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_150)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_200.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_200)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_255.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_255)

    # Part 3
    image_laplacian_of_gaussian = laplacian_of_gaussian_edge_detection(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_3_laplacian_of_gaussian.jpg')
    cv2.imwrite(image_path, image_laplacian_of_gaussian)

    # Part 4
    # TODO: Fix this code
    # image_difference_of_gaussian = difference_of_gaussian_edge_detection(image_grayscale)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_4_difference_of_gaussian.jpg')
    # cv2.imwrite(image_path, image_difference_of_gaussian)