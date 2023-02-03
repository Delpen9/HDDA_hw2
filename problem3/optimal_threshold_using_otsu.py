import cv2
import numpy as np

def find_optimal_otsu_threshold_then_perform(
    image : np.ndarray
) -> tuple[np.ndarray, any]:
    '''
    Finds the optimal threshold value using Otsu's method and applies it to the input image.
    The function returns the thresholded image and the optimal threshold value.

    Parameters:
    - image (np.ndarray): The input image as a numpy array.

    Returns:
    - tuple: A tuple of thresholded image (np.ndarray) and optimal threshold value (int).
    '''
    temp_image = image.copy()

    otsu_threshold, thresholded_image = cv2.threshold(
        temp_image,
        0,
        255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )
    return thresholded_image, int(otsu_threshold)
