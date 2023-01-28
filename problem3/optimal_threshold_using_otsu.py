import cv2
import numpy as np

def find_optimal_otsu_threshold_then_perform(
    image : np.ndarray
) -> tuple[np.ndarray, int]:
    '''
    Finds the optimal threshold value using Otsu's method and applies it to the input image.
    The function returns the thresholded image and the optimal threshold value.
    Parameters:
    - image (np.ndarray): The input image as a numpy array.
    Returns:
    - tuple: A tuple of thresholded image (np.ndarray) and optimal threshold value(int)
    '''
    thresholded_image, otsu_threshold = cv2.threshold(
        image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return thresholded_image, int(otsu_threshold)
