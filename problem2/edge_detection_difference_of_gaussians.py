import cv2
import numpy as np

def difference_of_gaussian_edge_detection(
    image: np.ndarray,
    sigma : float = 3,
    _k : float = 2,
    gamma : float = 1.5
) -> np.ndarray:
    '''
    Finds edges in an image using a Difference of Gaussian (DoG) operator.

    Parameters:
    - image (np.ndarray): The input image as a numpy array.
    - sigma (float): Sigma of first gaussian. Default is 3.
    - _k (float): Factor to multiply sigma by in second gaussian. Default is 2.
    - gamma (float): Factor to multiply second gaussian by. Default is 1.5.

    Returns:
    - difference_of_gaussian_image (np.ndarray): Difference of Gaussian image.
    '''
    image_1 = cv2.GaussianBlur(image, (sigma, sigma), 0)

    sigma_2 = -_k * sigma
    image_2 = gamma * cv2.GaussianBlur(image, (sigma_2, sigma_2), 0)

    difference_of_gaussian_image = image_1 - image_2

    return difference_of_gaussian_image
