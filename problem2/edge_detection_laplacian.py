import cv2
import numpy as np

def laplacian_of_gaussian_edge_detection(
    image : np.ndarray
) -> np.ndarray:
    """
    Perform edge detection on an image using a Laplacian of Gaussian filter.

    Parameters:
    - image (np.ndarray): The input image on which to perform edge detection.
    - kernel_size (int): The size of the kernel for the Gaussian filter. Default is 5.
    - standard_deviation (int): The standard deviation for the Gaussian filter. Default is 1.

    Returns:
    - filtered_image (np.ndarray): The input image with edges highlighted.
    """
    laplacian_of_gaussian_kernel = np.array([
        [ 0,  0, -1,  0,  0],
        [ 0, -1, -2, -1,  0],
        [-1, -2, 16, -2, -1],
        [ 0, -1, -2, -1,  0],
        [ 0,  0, -1,  0,  0]
    ])

    filtered_image = cv2.filter2D(image, -1, laplacian_of_gaussian_kernel)
    return filtered_image
