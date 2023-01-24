import cv2
import numpy as np

def median_denoise(
  image : np.ndarray,
  m : int = 3,
  n : int = 3
):
    '''
    median_denoise()
    '''
    denoised_image = cv2.medianBlur(image, (m, n))
    return denoised_image
