import cv2
import numpy as np

def log_transform_image(
    image : np.ndarray,
    _c : float = 40
):
    '''
    log_transform_image():
        Perform logarithmic transformation on a given OpenCV image.

        Parameters:
        image (np.ndarray): A pre-loaded OpenCV image to perform the logarithmic transformation on.
        _c (float): The constant used in the logarithmic transformation. Default is 40.

        Returns:
        logarithmic_image (np.ndarray): The logarithmically transformed image.
    '''
    logarithmic_image = _c * np.log1p(np.array(image, dtype = 'float') / 255)
    logarithmic_image = np.uint8(np.expm1(logarithmic_image))
    return logarithmic_image
