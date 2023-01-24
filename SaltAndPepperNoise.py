import numpy as np
import random

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
              output[i][j] = (0, 0, 0)
          elif rdn > thres:
              output[i][j] = (255, 255, 255)
  return output
