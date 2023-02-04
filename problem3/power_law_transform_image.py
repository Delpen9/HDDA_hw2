import cv2
import numpy as np

def power_law_transform(
    image : np.ndarray,
    _c : float = 0.1,
    gamma : float = 1.4
):
    '''
    Perform power law transformation on a given OpenCV image.

    Parameters:
    image (np.ndarray): A pre-loaded OpenCV image to perform the power law transformation on.
    _c (float): The constant used in the power law transformation. Default is 0.1.
    gamma (float): The gamma value used in the power law transformation. Default is 1.4.

    Returns:
    power_law_image (np.ndarray): The power law transformed image.
    '''
    power_law_image = _c * np.power(np.array(image, dtype = 'float') / 255, gamma)
    power_law_image = np.uint8(
        (power_law_image - np.min(power_law_image)) * (255 / np.max(power_law_image))
    )
    return power_law_image
