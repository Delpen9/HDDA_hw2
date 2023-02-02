import cv2
import numpy as np

def add_gaussian_noise(
  image : np.ndarray,
  mean : float = 0.0,
  variance : float = 0.01
) -> np.ndarray:
    '''
    add_gaussian_noise()
    '''
    noise = np.random.normal(mean, variance, image.shape)
    noisy_image = image + noise

    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = np.uint8(noisy_image)

    return noisy_image
