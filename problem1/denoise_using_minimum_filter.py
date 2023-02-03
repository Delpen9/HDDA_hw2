import cv2
import numpy as np

def minimum_filter(
    image : np.ndarray,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    """
    This function applies a minimum filter to an image using the openCV library.

    Parameters:
        image (ndarray): The image which you want to apply the filter on.
        _m (int): The number of rows in the kernel (default is 3).
        _n (int): The number of columns in the kernel (default is 3).

    Returns:
        denoised_image (ndarray): The filtered image
    """
    new_image = image.copy()

    size = (_m, _n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)
    denoised_image = cv2.erode(new_image, kernel)
    return denoised_image
