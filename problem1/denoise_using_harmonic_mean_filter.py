import cv2
import numpy as np

def harmonic_denoise(
    image : np.ndarray,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    """
    harmonic_denoise():
      Applies a harmonic mean filter to an image to remove noise.
      Args:
          image (np.ndarray): The image to be denoised.
          _m (int): The number of rows in the kernel (default is 3).
          _n (int): The number of columns in the kernel (default is 3).
      Returns:
          np.ndarray: The denoised image.
    """
    new_image = image.copy()

    kernel = (_m * _n) * 1 / np.ones((_m, _n)).astype(np.float32)

    denoised_image = cv2.filter2D(new_image, -1, kernel)
    return denoised_image
