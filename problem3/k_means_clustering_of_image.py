import numpy as np
from sklearn.cluster import KMeans

def image_clustering(
    colored_image: np.ndarray,
    clusters: int
) -> np.ndarray:
    '''
    Clusters a colored image into multiple clusters using k-means clustering.

    Parameters:
    - colored_image (np.ndarray): The input colored image as a numpy array.
    - clusters (int): The number of clusters for the image.

    Returns:
    - np.ndarray: The image with each pixel assigned to a cluster as a numpy array.
    '''
    pixels = colored_image.reshape(-1, 3)

    kmeans = KMeans(
        n_clusters = clusters,
        random_state = 0
    ).fit(pixels)

    return kmeans.cluster_centers_[kmeans.labels_].reshape(colored_image.shape).astype(np.uint8)
