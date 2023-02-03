import cv2
import numpy as np

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
    new_image = image.copy()
    
    kernel = np.ones((_m, _n))

    if _q == 0:
        kernel = kernel / (_m * _n)
        denoised_image = cv2.filter2D(new_image, -1, kernel)

    else:
        denoised_image = np.zeros_like(new_image)

        for i in range(new_image.shape[2]):
            denoised_image[i] = (
                np.power(
                        np.sum(np.power(new_image[i], _q + 1)),
                        1 / (_q + 1)
                    ) / np.sum(np.power(new_image[i], _q)
                )
            )

    return denoised_image
