"""
Author: Ian Dover

This module contains a function for converting a color image to grayscale.
"""

import cv2
import numpy as np

def convert2grayscale(
  image : np.ndarray
) -> np.ndarray:
    '''
    convert2greyscale()
    '''
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image
