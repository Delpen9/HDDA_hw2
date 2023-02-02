import cv2
import numpy as np

def midpoint_denoise(
    image : np.ndarray,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    '''
    Applies a midpoint filter to denoise a colored image using the OpenCV library.
    
    Parameters:
        image (ndarray): the image to be denoised
        _m (int): the kernel width
        _n (int): the kernel height
    
    Returns:
        ndarray: the denoised image
    '''
    new_image = image.copy()

    size = (_m, _n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)

    max_image = cv2.dilate(new_image, kernel)
    min_image = cv2.erode(new_image, kernel)

    denoised_image = 0.5 * (max_image + min_image)
    return denoised_image
