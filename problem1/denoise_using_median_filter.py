import cv2
import numpy as np

def median_denoise(
  image : np.ndarray,
  _m : int = 3,
  _n : int = 3
):
    '''
    median_denoise()
    '''
    denoised_image = cv2.medianBlur(image, (_m, _n))
    return denoised_image
