import cv2
import numpy as np

def difference_of_gaussian_edge_detection(
    image: np.ndarray,
    sigma : float = 0.8,
    _k : float = 1.6,
    gamma : float = 0.98
) -> np.ndarray:
    '''
    Finds edges in an image using a Difference of Gaussian (DoG) operator.

    Parameters:
    - image (np.ndarray): The input image as a numpy array.
    - sigma (float): Sigma of first gaussian. Default is 0.8.
    - _k (float): Factor to multiply sigma by in second gaussian. Default is 1.6.
    - gamma (float): Factor to multiply second gaussian by. Default is 0.98.

    Returns:
    - difference_of_gaussian_image (np.ndarray): Difference of Gaussian image.
    '''
    assert _k >= 1.0

    kernel_size = (3, 3)

    image_1 = cv2.GaussianBlur(image, ksize = kernel_size, sigmaX = sigma, sigmaY = sigma)

    sigma_2 = -_k * sigma
    image_2 = gamma * cv2.GaussianBlur(image, ksize = kernel_size, sigmaX = sigma_2, sigmaY = sigma_2)

    difference_of_gaussian_image = image_1 - image_2

    return difference_of_gaussian_image

def display_output_image(
    image: np.ndarray,
    sigma : float = 0.8,
    _k : float = 1.6,
    gamma : float = 0.98,
    phi : float = 200,
    epsilon : float = -0.1
) -> np.ndarray:
    '''
    Display the output image after applying difference of gaussian
    edge detection and applying a non-linear transformation.

    Parameters:
    - image (np.ndarray): The input image as a numpy array.
    - sigma (float): The standard deviation of the Gaussian kernel used in the edge detection.
    - _k (float): The difference between the two standard deviations used in the edge detection.
    - gamma (float): A constant value used in the edge detection.
    - phi (float): A constant value used in the non-linear transformation.
    - epsilon (float): A constant value used in the non-linear transformation.

    Returns:
    - _t (np.ndarray): The output image after applying the
    edge detection and non-linear transformation.
    '''
    difference_of_gaussian_image = difference_of_gaussian_edge_detection(image, sigma, _k, gamma)

    _u = np.multiply(difference_of_gaussian_image, image)

    condition = (_u >= epsilon)

    _t = np.ones(_u.shape)
    _t[~condition] = 1 + np.tanh(phi * (_u[~condition] * epsilon))

    return _t
