import cv2
import numpy as np

def mean_filter_denoise(
  image : np.ndarray,
  m : int = 3,
  n : int = 3
):
  '''
  mean_filter_denoise()
  '''
  kernel = np.ones((m, n), np.float32) / (m * n)
  
  denoised = cv2.filter2D(image, -1, kernel)
  return denoised
