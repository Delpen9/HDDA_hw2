import cv2
import numpy as np

def geometric_mean_denoise(
  image : np.ndarray,
  _m : int = 3,
  _n : int = 3
) -> np.ndarray:
    """
    geometric_mean_denoise()
      Approximate a geometric mean filter to denoise an image using OpenCV.

      Parameters:
      image (ndarray): The image to be denoised.
      _m (int): the number of rows in the filter mask
      _n (int): the number of columns in the filter mask

      Returns:
      ndarray: The denoised image.
    """
    kernel = np.ones((_m, _n))
    _n = kernel.size

    denoised_image = image.copy()

    _h, _w = image.shape[:2]

    for i in range(_m // 2, _h - _m // 2):
        for j in range(_n // 2, _w - _n // 2):
            pixels = image[
              i - _m // 2 : i + _m // 2 + 1,
              j - _n // 2 : j + _n // 2 + 1
            ]
            mean = np.power(np.prod(pixels), 1 / _n)

            denoised_image[i][j] = mean

    return denoised_image
