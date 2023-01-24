"""
Author: Ian Dover

This module contains a function for applying mean filter denoising to images.

The function mean_filter_denoise() applies a mean
filter to an image using a kernel of specified size.
The kernel is a square matrix with the same number of rows and columns,
where each element has the same value (1/(m*n)) and the sum of all elements is 1.
This kernel is convolved with the image resulting in a denoised image.
"""
import cv2
import numpy as np

# pylint: disable=no-member
def mean_filter_denoise(
  image : np.ndarray,
  _m : int = 3,
  _n : int = 3
) -> np.ndarray:
    """
    mean_filter_denoise():
      Applies a mean filter to an image to remove noise.
      Args:
          image (np.ndarray): The image to be denoised.
          _m (int): The number of rows in the kernel (default is 3).
          _n (int): The number of columns in the kernel (default is 3).
      Returns:
          np.ndarray: The denoised image.
    """
    kernel = np.ones((_m, _n), np.float32) / (_m * _n)

    denoised = cv2.filter2D(image, -1, kernel)
    return denoised
