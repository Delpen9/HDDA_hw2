import cv2
import numpy as np

def midpoint_denoise(
    image : np.ndarray,
    _m : int,
    _n : int
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
    kernel = np.ones((_m, _n)).astype(int)
    denoised_image = cv2.filter2D(image, -1, kernel)
    return denoised_image
