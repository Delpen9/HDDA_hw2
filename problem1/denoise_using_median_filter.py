import cv2
import numpy as np

def median_denoise(
  image : np.ndarray,
  kernel_size : int = 3
) -> np.ndarray:
    '''
    median_denoise()
    '''
    denoised_image = cv2.medianBlur(image, kernel_size)
    return denoised_image
