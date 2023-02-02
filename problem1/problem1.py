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
from denoise_using_mean_filter import mean_filter_denoise
from denoise_using_geometric_mean import geometric_mean_denoise
from denoise_using_harmonic_mean_filter import harmonic_denoise
from denoise_using_contraharmonic_mean_filter import contraharmonic_mean_filter
from denoise_using_minimum_filter import minimum_filter
from denoise_using_maximum_filter import maximum_filter
from denoise_using_midpoint_filter import midpoint_denoise

if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'images', 'theAlps-1.jpg')
    image = cv2.imread(image_path)

    # Part A
    image_grayscale = convert2grayscale(image)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_a_grayscale.jpg')
    cv2.imwrite(image_path, image_grayscale)

    # Part B.1
    image_gaussian_noise = add_gaussian_noise(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_b_1_gaussian.jpg')
    cv2.imwrite(image_path, image_gaussian_noise)

    # Part B.2
    image_salt_and_pepper_noise = salt_and_pepper(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_b_2_salt_and_pepper.jpg')
    cv2.imwrite(image_path, image_salt_and_pepper_noise)

    # Part C.1
    image_gaussian_denoised_j1 = gaussian_denoise(image_gaussian_noise)
    image_gaussian_denoised_j2 = gaussian_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_1_j1.jpg')
    cv2.imwrite(image_path, image_gaussian_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_1_j2.jpg')
    cv2.imwrite(image_path, image_gaussian_denoised_j2)

    # Part C.2
    image_median_denoised_j1 = median_denoise(image_gaussian_noise)
    image_median_denoised_j2 = median_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_2_j1.jpg')
    cv2.imwrite(image_path, image_median_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_2_j2.jpg')
    cv2.imwrite(image_path, image_median_denoised_j2)

    # Part C.3
    image_mean_filter_denoised_j1 = mean_filter_denoise(image_gaussian_noise)
    image_mean_filter_denoised_j2 = mean_filter_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_3_j1.jpg')
    cv2.imwrite(image_path, image_mean_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_3_j2.jpg')
    cv2.imwrite(image_path, image_mean_filter_denoised_j2)

    # Part C.4
    ## TODO: Fix this
    # image_geometric_mean_filter_denoised_j1 = geometric_mean_denoise(image_gaussian_noise)
    # image_geometric_mean_filter_denoised_j2 = geometric_mean_denoise(image_salt_and_pepper_noise)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_4_j1.jpg')
    # cv2.imwrite(image_path, image_geometric_mean_filter_denoised_j1)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_4_j2.jpg')
    # cv2.imwrite(image_path, image_geometric_mean_filter_denoised_j2)

    # Part C.5
    ## TODO: Fix this
    # image_harmonic_mean_filter_denoised_j1 = harmonic_denoise(image_gaussian_noise)
    # image_harmonic_mean_filter_denoised_j2 = harmonic_denoise(image_salt_and_pepper_noise)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_5_j1.jpg')
    # cv2.imwrite(image_path, image_harmonic_mean_filter_denoised_j1)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_5_j2.jpg')
    # cv2.imwrite(image_path, image_harmonic_mean_filter_denoised_j2)

    # Part C.6
    # TODO: Fix this
    # _q = -1
    # image_contraharmonic_mean_filter_denoised_j1_q_neg_1 = contraharmonic_mean_filter(image_gaussian_noise, -1)
    # image_contraharmonic_mean_filter_denoised_j2_q_neg_1 = contraharmonic_mean_filter(image_salt_and_pepper_noise, -1)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j1_q_neg1.jpg')
    # cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j1)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j2_q_neg1.jpg')
    # cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j2)

    # # _q = 0
    # image_contraharmonic_mean_filter_denoised_j1_q_0 = contraharmonic_mean_filter(image_gaussian_noise, 0)
    # image_contraharmonic_mean_filter_denoised_j2_q_0 = contraharmonic_mean_filter(image_salt_and_pepper_noise, 0)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j1_q_0.jpg')
    # cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j1_q_0)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j2_q_0.jpg')
    # cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j2_q_0)

    # # _q = 1
    # image_contraharmonic_mean_filter_denoised_j1_q_1 = contraharmonic_mean_filter(image_gaussian_noise, 1)
    # image_contraharmonic_mean_filter_denoised_j2_q_1 = contraharmonic_mean_filter(image_salt_and_pepper_noise, 1)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j1_q_1.jpg')
    # cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j1_q_1)

    # image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j2_q_1.jpg')
    # cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j2_q_1)

    # Part C.7
    image_minimum_filter_denoised_j1 = minimum_filter(image_gaussian_noise)
    image_minimum_filter_denoised_j2 = minimum_filter(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_7_j1.jpg')
    cv2.imwrite(image_path, image_minimum_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_7_j2.jpg')
    cv2.imwrite(image_path, image_minimum_filter_denoised_j2)

    # Part C.8
    image_maximum_filter_denoised_j1 = maximum_filter(image_gaussian_noise)
    image_maximum_filter_denoised_j2 = maximum_filter(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_8_j1.jpg')
    cv2.imwrite(image_path, image_maximum_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_8_j2.jpg')
    cv2.imwrite(image_path, image_maximum_filter_denoised_j2)

    # Part C.9
    image_midpoint_filter_denoised_j1 = midpoint_denoise(image_gaussian_noise)
    image_midpoint_filter_denoised_j2 = midpoint_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_9_j1.jpg')
    cv2.imwrite(image_path, image_midpoint_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_9_j2.jpg')
    cv2.imwrite(image_path, image_midpoint_filter_denoised_j2)