# Standard Libraries
import numpy as np
import os
import cv2

# Convert to grayscale
from convert_to_grayscale import convert2grayscale

# image segmentation
from k_means_clustering_of_image import image_clustering
from histogram_greyscale_image import plot_greyscale_histogram
from optimal_threshold_using_otsu import find_optimal_otsu_threshold_then_perform

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

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_kmeans_2.jpg')
    cv2.imwrite(image_path, image_k_means_2_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_2_clusters), 'p3_kmeans_2_histogram.jpg')

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_kmeans_3.jpg')
    cv2.imwrite(image_path, image_k_means_3_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_3_clusters), 'p3_kmeans_3_histogram.jpg')

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_kmeans_4.jpg')
    cv2.imwrite(image_path, image_k_means_4_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_4_clusters), 'p3_kmeans_4_histogram.jpg')

    image_path = os.path.join(parent_directory, '..', 'output', 'problem3', 'p3_kmeans_5.jpg')
    cv2.imwrite(image_path, image_k_means_5_clusters)
    plot_greyscale_histogram(convert2grayscale(image_k_means_5_clusters), 'p3_kmeans_5_histogram.jpg')

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
    



