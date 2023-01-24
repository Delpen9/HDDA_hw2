Here is a Python function that takes an image as input and adds zero-mean Gaussian white noise with a variance of 0.01:

Copy code
import cv2
import numpy as np

def add_gaussian_noise(
  image : np.ndarray
) -> np.ndarray:
  '''
  add_gaussian_noise()
  '''
  noise = np.random.normal(0, 0.01, image.shape)
  noisy_image = image + noise

  noisy_image = np.clip(noisy_image, 0, 255)
  noisy_image = np.uint8(noisy_image)

  return noisy_image
