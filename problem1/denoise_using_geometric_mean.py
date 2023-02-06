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
    assert _m == _n
    
    image_copy = image.copy()

    pad_size = 1
    padded_image = cv2.copyMakeBorder(image_copy, *[pad_size] * 4, cv2.BORDER_DEFAULT)

    geometric_mean_image = np.zeros_like(image_copy)

    _h, _w = image_copy.shape[:2]

    for h in range(_h):
        for w in range(_w):
            geometric_mean_image[h, w] = np.prod(padded_image[h : h + _m, w : w + _n])**(1 / (_m**2))

    denoised_image = np.uint8(geometric_mean_image)

    return denoised_image
