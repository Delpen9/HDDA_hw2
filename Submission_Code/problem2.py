# Standard Libraries
import numpy as np
import os
import cv2

def convert2grayscale(
  image : np.ndarray
) -> np.ndarray:
    '''
    convert2greyscale()
    '''
    new_image = image.copy()

    grayscale_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def get_gradient_magnitude_sobel(
    image : np.ndarray
) -> np.ndarray:
    '''
    Computes the gradient magnitude of an image using the Sobel operator.

    Parameters:
        image (ndarray): the image to compute the gradient magnitude of

    Returns:
        ndarray: the gradient magnitude of the image
    '''
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    gradient_magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))

    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient_magnitude

def threshold_gradient_sobel(
    image : np.ndarray,
    threshold : np.ndarray
) -> np.ndarray:
    '''
    Applies a threshold to the gradient magnitude of an image.

    Parameters:
        image (ndarray): the gradient magnitude image
        threshold (int): the threshold value (0-255)

    Returns:
        ndarray: the thresholded gradient magnitude image
    '''
    assert threshold >= 0
    assert threshold <= 255

    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return thresholded_image

def sobel_edge_detection(
    image: np.ndarray,
    threshold : int = 150
) -> np.ndarray:
    '''
    Creates a gradient magnitude and then applies a threshold to the gradient magnitude of an image.

    Parameters:
        image (ndarray): the gradient magnitude image
        threshold (int): the threshold value (0-255)

    Returns:
        ndarray: the thresholded gradient magnitude image
    '''
    assert threshold >= 0
    assert threshold <= 255

    new_image = image.copy()

    gradient_image = get_gradient_magnitude_sobel(new_image)
    thresholded_gradient = threshold_gradient_sobel(gradient_image, threshold)
    return thresholded_gradient

def get_gradient_magnitude_prewitt(
    image : np.ndarray
) -> np.ndarray:
    '''
    Computes the gradient magnitude of an image using the Prewitt operator.

    Parameters:
        image (ndarray): the image to compute the gradient magnitude of

    Returns:
        ndarray: the gradient magnitude of the image
    '''
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewittx = cv2.filter2D(image, -1, kernelx)
    prewitty = cv2.filter2D(image, -1, kernely)

    gradient_magnitude = np.sqrt(np.square(prewittx) + np.square(prewitty)).astype(np.uint8)

    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return gradient_magnitude

def threshold_gradient_prewitt(
    image : np.ndarray,
    threshold : np.ndarray
) -> np.ndarray:
    '''
    Applies a threshold to the gradient magnitude of an image.

    Parameters:
        image (ndarray): the gradient magnitude image
        threshold (int): the threshold value (0-255)

    Returns:
        ndarray: the thresholded gradient magnitude image
    '''
    assert threshold >= 0
    assert threshold <= 255

    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return thresholded_image

def prewitt_edge_detection(
    image: np.ndarray,
    threshold : int = 150
) -> np.ndarray:
    '''
    Creates a gradient magnitude and then applies a threshold to the gradient magnitude of an image.

    Parameters:
        image (ndarray): the gradient magnitude image
        threshold (int): the threshold value (0-255)

    Returns:
        ndarray: the thresholded gradient magnitude image
    '''
    assert threshold >= 0
    assert threshold <= 255

    new_image = image.copy()

    gradient_image = get_gradient_magnitude_prewitt(new_image)
    thresholded_gradient = threshold_gradient_prewitt(gradient_image, threshold)
    return thresholded_gradient

def laplacian_of_gaussian_edge_detection(
    image : np.ndarray
) -> np.ndarray:
    """
    Perform edge detection on an image using a Laplacian of Gaussian filter.

    Parameters:
    - image (np.ndarray): The input image on which to perform edge detection.
    - kernel_size (int): The size of the kernel for the Gaussian filter. Default is 5.
    - standard_deviation (int): The standard deviation for the Gaussian filter. Default is 1.

    Returns:
    - filtered_image (np.ndarray): The input image with edges highlighted.
    """
    laplacian_of_gaussian_kernel = np.array([
        [ 0,  0, -1,  0,  0],
        [ 0, -1, -2, -1,  0],
        [-1, -2, 16, -2, -1],
        [ 0, -1, -2, -1,  0],
        [ 0,  0, -1,  0,  0]
    ])

    filtered_image = cv2.filter2D(image, -1, laplacian_of_gaussian_kernel)
    return filtered_image

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

if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'images', 'Eagle-1.jpg')
    image = cv2.imread(image_path)
    image_grayscale = convert2grayscale(image)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_Eagle_grayscale.jpg')
    cv2.imwrite(image_path, image_grayscale)

    # Part 1
    image_sobel_thresh_10 = sobel_edge_detection(image_grayscale, 10)
    image_sobel_thresh_50 = sobel_edge_detection(image_grayscale, 50)
    image_sobel_thresh_100 = sobel_edge_detection(image_grayscale, 100)
    image_sobel_thresh_150 = sobel_edge_detection(image_grayscale, 150)
    image_sobel_thresh_200 = sobel_edge_detection(image_grayscale, 200)
    image_sobel_thresh_255 = sobel_edge_detection(image_grayscale, 255)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_10.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_10)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_50.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_50)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_100.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_100)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_150.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_150)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_200.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_200)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_255.jpg')
    cv2.imwrite(image_path, image_sobel_thresh_255)

    # Part 2
    image_prewitt_thresh_10 = prewitt_edge_detection(image_grayscale, 10)
    image_prewitt_thresh_50 = prewitt_edge_detection(image_grayscale, 50)
    image_prewitt_thresh_100 = prewitt_edge_detection(image_grayscale, 100)
    image_prewitt_thresh_150 = prewitt_edge_detection(image_grayscale, 150)
    image_prewitt_thresh_200 = prewitt_edge_detection(image_grayscale, 200)
    image_prewitt_thresh_255 = prewitt_edge_detection(image_grayscale, 255)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_10.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_10)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_50.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_50)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_100.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_100)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_150.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_150)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_200.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_200)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_255.jpg')
    cv2.imwrite(image_path, image_prewitt_thresh_255)

    # Part 3
    image_laplacian_of_gaussian = laplacian_of_gaussian_edge_detection(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_3_laplacian_of_gaussian.jpg')
    cv2.imwrite(image_path, image_laplacian_of_gaussian)

    # Part 4
    image_difference_of_gaussian = display_output_image(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem2', 'p2_part_4_difference_of_gaussian.jpg')
    cv2.imwrite(image_path, image_difference_of_gaussian)