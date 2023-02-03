import cv2
import numpy as np

def gaussian_denoise(
  image : np.ndarray,
  kernel_size : int = 3,
  standard_deviation : int = 2
):
    '''
    gaussian_denoise()
    '''
    new_image = image.copy()

    kernel = cv2.getGaussianKernel(kernel_size, standard_deviation)
    denoised_image = cv2.sepFilter2D(new_image, -1, kernel, kernel)
    return denoised_image
