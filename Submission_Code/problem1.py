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


def add_gaussian_noise(
  image : np.ndarray,
  mean : float = 0.0,
  variance : float = 0.01
) -> np.ndarray:
    '''
    add_gaussian_noise()
    '''
    new_image = image.copy()

    noise = np.random.normal(mean, variance, new_image.shape)
    noisy_image = new_image + noise

    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = np.uint8(noisy_image)

    return noisy_image

def salt_and_pepper(
  image : np.ndarray,
  prob : float = 0.05
) -> np.ndarray:
    '''
    salt_and_pepper()
    '''
    output = np.copy(image)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
    return output

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

def median_denoise(
  image : np.ndarray,
  kernel_size : int = 3
) -> np.ndarray:
    '''
    median_denoise()
    '''
    new_image = image.copy()

    denoised_image = cv2.medianBlur(new_image, kernel_size)
    return denoised_image

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
    new_image = image.copy()
    
    kernel = np.ones((_m, _n)).astype(np.float32) / (_m * _n)

    denoised_image = cv2.filter2D(new_image, -1, kernel)
    return denoised_image

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

def harmonic_denoise(
    image : np.ndarray,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    """
    harmonic_denoise():
      Applies a harmonic mean filter to an image to remove noise.
      Args:
          image (np.ndarray): The image to be denoised.
          _m (int): The number of rows in the kernel (default is 3).
          _n (int): The number of columns in the kernel (default is 3).
      Returns:
          np.ndarray: The denoised image.
    """
    new_image = image.copy()

    kernel = (_m * _n) * 1 / np.ones((_m, _n)).astype(np.float32)

    denoised_image = cv2.filter2D(new_image, -1, kernel)
    return denoised_image

def contraharmonic_mean_filter(
    image : np.ndarray,
    _q : int,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    """
    This function applies a Contraharmonic mean filter to an image using the openCV library.

    Parameters:
        new_image (ndarray): The new_image which you want to apply the filter on.
        _q (float): The order of the filter. It can be -1, 0, 1.
                    If _q = 0, it applies an arithmetic mean filter
                    If _q = -1, it applies a harmonic mean filter
                    If _q = 1, it applies a subharmonic mean filter
        _m (int): The number of rows in the kernel (default is 3).
        _n (int): The number of columns in the kernel (default is 3).

    Returns:
        denoised_image (ndarray): The filtered image
    """
    image_copy = image.copy()
    
    numerator = np.power(image_copy, _q + 1)

    if _q == -1:
        denominator = 1 / np.power(image_copy, 1)
    else:
        denominator = np.power(image_copy, _q)

    kernel = np.full((_m, _n), 1.0)

    denoised_image = cv2.filter2D(numerator, -1, kernel) / cv2.filter2D(denominator, -1, kernel)
    return denoised_image

def minimum_filter(
    image : np.ndarray,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    """
    This function applies a minimum filter to an image using the openCV library.

    Parameters:
        image (ndarray): The image which you want to apply the filter on.
        _m (int): The number of rows in the kernel (default is 3).
        _n (int): The number of columns in the kernel (default is 3).

    Returns:
        denoised_image (ndarray): The filtered image
    """
    new_image = image.copy()

    size = (_m, _n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)
    denoised_image = cv2.erode(new_image, kernel)
    return denoised_image

def maximum_filter(
    image : np.ndarray,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    """
    This function applies a maximum filter to an image using the openCV library.

    Parameters:
        image (ndarray): The image which you want to apply the filter on.
        _m (int): The number of rows in the kernel (default is 3).
        _n (int): The number of columns in the kernel (default is 3).

    Returns:
        denoised_image (ndarray): The filtered image
    """
    new_image = image.copy()

    size = (_m, _n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)
    denoised_image = cv2.dilate(new_image, kernel)
    return denoised_image

def midpoint_denoise(
    image : np.ndarray,
    _m : int = 3,
    _n : int = 3
) -> np.ndarray:
    '''
    Applies a midpoint filter to denoise a colored image using the OpenCV library.
    
    Parameters:
        image (ndarray): the image to be denoised
        _m (int): the kernel width
        _n (int): the kernel height
    
    Returns:
        ndarray: the denoised image
    '''
    new_image = image.copy()

    size = (_m, _n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)

    max_image = cv2.dilate(new_image, kernel)
    min_image = cv2.erode(new_image, kernel)

    denoised_image = 0.5 * (max_image + min_image)
    return denoised_image

if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'images', 'theAlps-1.jpg')
    image = cv2.imread(image_path)

    # Part A
    image_grayscale = convert2grayscale(image)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_a_grayscale.jpg')
    cv2.imwrite(image_path, image_grayscale)

    # Part B.1
    image_gaussian_noise = add_gaussian_noise(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_b_1_gaussian.jpg')
    cv2.imwrite(image_path, image_gaussian_noise)

    # Part B.2
    image_salt_and_pepper_noise = salt_and_pepper(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_b_2_salt_and_pepper.jpg')
    cv2.imwrite(image_path, image_salt_and_pepper_noise)

    # Part C.1
    image_gaussian_denoised_j1 = gaussian_denoise(image_gaussian_noise)
    image_gaussian_denoised_j2 = gaussian_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_1_j1.jpg')
    cv2.imwrite(image_path, image_gaussian_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_1_j2.jpg')
    cv2.imwrite(image_path, image_gaussian_denoised_j2)

    # Part C.2
    image_median_denoised_j1 = median_denoise(image_gaussian_noise)
    image_median_denoised_j2 = median_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_2_j1.jpg')
    cv2.imwrite(image_path, image_median_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_2_j2.jpg')
    cv2.imwrite(image_path, image_median_denoised_j2)

    # Part C.3
    image_mean_filter_denoised_j1 = mean_filter_denoise(image_gaussian_noise)
    image_mean_filter_denoised_j2 = mean_filter_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_3_j1.jpg')
    cv2.imwrite(image_path, image_mean_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_3_j2.jpg')
    cv2.imwrite(image_path, image_mean_filter_denoised_j2)

    # Part C.4
    image_geometric_mean_filter_denoised_j1 = geometric_mean_denoise(image_gaussian_noise)
    image_geometric_mean_filter_denoised_j2 = geometric_mean_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_4_j1.jpg')
    cv2.imwrite(image_path, image_geometric_mean_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_4_j2.jpg')
    cv2.imwrite(image_path, image_geometric_mean_filter_denoised_j2)

    # Part C.5
    image_harmonic_mean_filter_denoised_j1 = harmonic_denoise(image_gaussian_noise)
    image_harmonic_mean_filter_denoised_j2 = harmonic_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_5_j1.jpg')
    cv2.imwrite(image_path, image_harmonic_mean_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_5_j2.jpg')
    cv2.imwrite(image_path, image_harmonic_mean_filter_denoised_j2)

    # Part C.6
    # _q = -1
    image_contraharmonic_mean_filter_denoised_j1_q_neg_1 = contraharmonic_mean_filter(image_gaussian_noise, -1)
    image_contraharmonic_mean_filter_denoised_j2_q_neg_1 = contraharmonic_mean_filter(image_salt_and_pepper_noise, -1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j1_q_neg1.jpg')
    cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j2_q_neg1.jpg')
    cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j2)

    # _q = 0
    image_contraharmonic_mean_filter_denoised_j1_q_0 = contraharmonic_mean_filter(image_gaussian_noise, 0)
    image_contraharmonic_mean_filter_denoised_j2_q_0 = contraharmonic_mean_filter(image_salt_and_pepper_noise, 0)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j1_q_0.jpg')
    cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j1_q_0)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j2_q_0.jpg')
    cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j2_q_0)

    # _q = 1
    image_contraharmonic_mean_filter_denoised_j1_q_1 = contraharmonic_mean_filter(image_gaussian_noise, 1)
    image_contraharmonic_mean_filter_denoised_j2_q_1 = contraharmonic_mean_filter(image_salt_and_pepper_noise, 1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j1_q_1.jpg')
    cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j1_q_1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_6_j2_q_1.jpg')
    cv2.imwrite(image_path, image_contraharmonic_mean_filter_denoised_j2_q_1)

    # Part C.7
    image_minimum_filter_denoised_j1 = minimum_filter(image_gaussian_noise)
    image_minimum_filter_denoised_j2 = minimum_filter(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_7_j1.jpg')
    cv2.imwrite(image_path, image_minimum_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_7_j2.jpg')
    cv2.imwrite(image_path, image_minimum_filter_denoised_j2)

    # Part C.8
    image_maximum_filter_denoised_j1 = maximum_filter(image_gaussian_noise)
    image_maximum_filter_denoised_j2 = maximum_filter(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_8_j1.jpg')
    cv2.imwrite(image_path, image_maximum_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_8_j2.jpg')
    cv2.imwrite(image_path, image_maximum_filter_denoised_j2)

    # Part C.9
    image_midpoint_filter_denoised_j1 = midpoint_denoise(image_gaussian_noise)
    image_midpoint_filter_denoised_j2 = midpoint_denoise(image_salt_and_pepper_noise)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_9_j1.jpg')
    cv2.imwrite(image_path, image_midpoint_filter_denoised_j1)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem1', 'p1_c_9_j2.jpg')
    cv2.imwrite(image_path, image_midpoint_filter_denoised_j2)