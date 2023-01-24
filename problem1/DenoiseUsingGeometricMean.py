import cv2
import numpy as np

def geometric_mean_denoise(
  image : np.ndarray,
  m : int = 3,
  n : int = 3
) -> np.ndarray:
  '''
  geometric_mean_denoise()
    Approximate a geometric mean filter to denoise an image using OpenCV.

    Parameters:
    image (ndarray): The image to be denoised.
    m (int): the number of rows in the filter mask
    n (int): the number of columns in the filter mask

    Returns:
    ndarray: The denoised image.
  '''
  kernel = np.ones((m, n))
  n = kernel.size

  denoised_image = image.copy()

  H, W = image.shape[:2]

  for i in range(m // 2, H - m // 2):
      for j in range(n // 2, W - n // 2):
          pixels = image[
            i - m / /2 : i + m // 2 + 1,
            j - n // 2 : j + n // 2 + 1
          ]
          mean = np.power(np.prod(pixels), 1 / n)

          denoised_image[i][j] = mean

  return denoised_image
