# Standard Libraries
import numpy as np
import os
import cv2

# Convert to grayscale
from convert_to_grayscale import convert2grayscale

# Add Noise
from add_gaussian_noise import add_gaussian_noise
from salt_and_pepper_noise import salt_and_pepper

# De-noise
from denoise_using_gaussian_kernel import gaussian_denoise
from denoise_using_median_filter import median_denoise


if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'images', 'theAlps-1.jpg')
    image = cv2.imread(image_path)

    # Part A
    image_grayscale = convert2grayscale(image)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_a_grayscale.jpg')
    cv2.imwrite(image_path, image_grayscale)

    # Part B.1
    image_gaussian_noise = add_gaussian_noise(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_b_1_gaussian.jpg')
    cv2.imwrite(image_path, image_gaussian_noise)

    # Part B.2
    image_salt_and_pepper_noise = salt_and_pepper(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_b_2_salt_and_pepper.jpg')
    cv2.imwrite(image_path, image_salt_and_pepper_noise)

    # Part C.1
    image_gaussian_denoised_j1 = gaussian_denoise(image_gaussian_noise)
    image_gaussian_denoised_j2 = gaussian_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_c_1_j1.jpg')
    cv2.imwrite(image_path, image_gaussian_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_c_1_j2.jpg')
    cv2.imwrite(image_path, image_gaussian_denoised_j2)

    # Part C.2
    image_median_denoised_j1 = median_denoise(image_gaussian_noise)
    image_median_denoised_j2 = median_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_c_2_j1.jpg')
    cv2.imwrite(image_path, image_median_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_c_2_j2.jpg')
    cv2.imwrite(image_path, image_median_denoised_j2)

    # Part C.3
    image_median_denoised_j1 = median_denoise(image_gaussian_noise)
    image_median_denoised_j2 = median_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_c_2_j1.jpg')
    cv2.imwrite(image_path, image_median_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'p1_c_2_j2.jpg')
    cv2.imwrite(image_path, image_median_denoised_j2)
