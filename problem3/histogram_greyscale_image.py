import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_greyscale_histogram(
    image: np.ndarray,
    filename : str
) -> None:
    '''
    Converts an image to greyscale and plots a histogram of the pixel intensities.

    Parameters:
    - image (np.ndarray): The input image as a numpy array.
    - filename (str): The output image file.

    Returns:
    - None
    '''
    plt.hist(
        image.ravel(),
        bins = 256,
        range = [0, 256]
    )

    plt.title('Greyscale Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Count')

    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', filename)
    plt.savefig(image_path)
