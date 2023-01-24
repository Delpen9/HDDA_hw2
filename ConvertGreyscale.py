import cv2

def convert2greyscale(
  image : np.ndarray
):
  '''
  convert2greyscale()
  '''
  grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  return grayscale_image
