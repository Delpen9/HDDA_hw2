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

def find_optimal_otsu_threshold_then_perform(
    image : np.ndarray
) -> tuple[np.ndarray, any]:
    '''
    Finds the optimal threshold value using Otsu's method and applies it to the input image.
    The function returns the thresholded image and the optimal threshold value.

    Parameters:
    - image (np.ndarray): The input image as a numpy array.

    Returns:
    - tuple: A tuple of thresholded image (np.ndarray) and optimal threshold value (int).
    '''
    temp_image = image.copy()

    otsu_threshold, thresholded_image = cv2.threshold(
        temp_image,
        0,
        255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
    )
    return thresholded_image, int(otsu_threshold)

def log_transform_image(
    image : np.ndarray,
    _c : float = 40
):
    '''
    log_transform_image():
        Perform logarithmic transformation on a given OpenCV image.

        Parameters:
        image (np.ndarray): A pre-loaded OpenCV image to perform the logarithmic transformation on.
        _c (float): The constant used in the logarithmic transformation. Default is 40.

        Returns:
        logarithmic_image (np.ndarray): The logarithmically transformed image.
    '''
    logarithmic_image = _c * np.log1p(np.array(image, dtype = 'float') / 255)
    logarithmic_image = np.uint8(np.expm1(logarithmic_image))
    return logarithmic_image

def power_law_transform(
    image : np.ndarray,
    _c : float = 0.1,
    gamma : float = 1.4
):
    '''
    Perform power law transformation on a given OpenCV image.

    Parameters:
    image (np.ndarray): A pre-loaded OpenCV image to perform the power law transformation on.
    _c (float): The constant used in the power law transformation. Default is 0.1.
    gamma (float): The gamma value used in the power law transformation. Default is 1.4.

    Returns:
    power_law_image (np.ndarray): The power law transformed image.
    '''
    power_law_image = _c * np.power(np.array(image, dtype = 'float') / 255, gamma)
    power_law_image = np.uint8(
        (power_law_image - np.min(power_law_image)) * (255 / np.max(power_law_image))
    )
    return power_law_image

if __name__ == '__main__':
    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)
    image_path = os.path.join(parent_directory, '..', 'images', 'RoseonIce-1.jpg')
    image = cv2.imread(image_path)

    # Part 1
    image_k_means_2_clusters = image_clustering(image, 2)
    image_k_means_3_clusters = image_clustering(image, 3)
    image_k_means_4_clusters = image_clustering(image, 4)
    image_k_means_5_clusters = image_clustering(image, 5)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_1_kmeans_2.jpg')
    cv2.imwrite(image_path, image_k_means_2_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_2_clusters), 'p3_1_kmeans_2_histogram.jpg')

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_1_kmeans_3.jpg')
    cv2.imwrite(image_path, image_k_means_3_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_3_clusters), 'p3_1_kmeans_3_histogram.jpg')

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_1_kmeans_4.jpg')
    cv2.imwrite(image_path, image_k_means_4_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_4_clusters), 'p3_1_kmeans_4_histogram.jpg')

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_1_kmeans_5.jpg')
    cv2.imwrite(image_path, image_k_means_5_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_5_clusters), 'p3_1_kmeans_5_histogram.jpg')

    # Part 2
    image_grayscale = convert2grayscale(image)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_2_grayscale.jpg')
    cv2.imwrite(image_path, image_grayscale)

    plot_greyscale_histogram(image_grayscale, 'p3_2_histogram.jpg')

    # Part 3
    thresholded_image, best_threshold = find_optimal_otsu_threshold_then_perform(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_3_otsu_threshold_image.jpg')
    cv2.imwrite(image_path, thresholded_image)

    text_file_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_3_otsu_threshold.txt')
    otsu_file = open(text_file_path, 'w')
    otsu_file.write(fr'The optimal threshold for the grayscale image determined by Otsu is: {best_threshold}')
    otsu_file.close()

    plot_greyscale_histogram(thresholded_image, 'p3_3_otsu_histogram.jpg')

    # Part 4
    logarithmic_image = log_transform_image(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_4_log_transform_image.jpg')
    cv2.imwrite(image_path, logarithmic_image)
    plot_greyscale_histogram(logarithmic_image, 'p3_4_log_transform_image_histogram.jpg')

    # Part 5
    power_law_transform_image = power_law_transform(image_grayscale)

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_5_power_law_transform_image.jpg')
    cv2.imwrite(image_path, power_law_transform_image)
    plot_greyscale_histogram(power_law_transform_image, 'p3_5_power_law_transform_image_histogram.jpg')
