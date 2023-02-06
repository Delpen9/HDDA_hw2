import cv2
import numpy as np

def contraharmonic_mean_filter(
    image : np.ndarray,
    _q : int,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    """
    This function applies a Contraharmonic mean filter to an image using the openCV library.

    Parameters:
        new_image (ndarray): The new_image which you want to apply the filter on.
        _q (float): The order of the filter. It can be -1, 0, 1.
                    If _q = 0, it applies an arithmetic mean filter
                    If _q = -1, it applies a harmonic mean filter
                    If _q = 1, it applies a subharmonic mean filter
        _m (int): The number of rows in the kernel (default is 3).
        _n (int): The number of columns in the kernel (default is 3).

    Returns:
        denoised_image (ndarray): The filtered image
    """
    image_copy = image.copy()
    
    numerator = np.power(image_copy, _q + 1)

    if _q == -1:
        denominator = 1 / np.power(image_copy, 1)
    else:
        denominator = np.power(image_copy, _q)

    kernel = np.full((_m, _n), 1.0)

    denoised_image = cv2.filter2D(numerator, -1, kernel) / cv2.filter2D(denominator, -1, kernel)
    return denoised_image
