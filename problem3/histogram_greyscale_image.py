import cv2
import matplotlib.pyplot as plt
import numpy as np

def plot_greyscale_histogram(
    image: np.ndarray
) -> None:
    '''
    Converts an image to greyscale and plots a histogram of the pixel intensities.

    Parameters:
    - image (np.ndarray): The input image as a numpy array.

    Returns:
    - None
    '''
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.hist(
        grayscale_image.ravel(),
        bins = 256,
        range = [0, 256]
    )

    plt.title('Greyscale Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Count')
    plt.show()
