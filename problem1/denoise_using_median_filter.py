import cv2
import numpy as np

def median_denoise(
  image : np.ndarray,
  kernel_size : int = 3
) -> np.ndarray:
    '''
    median_denoise()
    '''
    new_image = image.copy()

    denoised_image = cv2.medianBlur(new_image, kernel_size)
    return denoised_image
