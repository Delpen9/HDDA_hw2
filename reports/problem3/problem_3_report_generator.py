import numpy as np
import os
from datetime import date

from pylatex import *
from pylatex.utils import *

def generate_header(
    doc : any,
    todays_date : str,
    company : str = 'Georgia Institute of Technology'
) -> any:
    '''
    '''
    header = PageStyle('header')

    with header.create(Head('L')):
        header.append('Page date: ')
        header.append(LineBreak())
        header.append(todays_date)
    
    with header.create(Head('C')):
        header.append(company)

    with header.create(Head('R')):
        header.append(simple_page_number())

    doc.preamble.append(header)
    doc.change_document_style('header')

    with doc.create(MiniPage(align = 'c')):
        doc.append(LargeText(bold('HW2: Problem 3')))
        doc.append(LineBreak())
        doc.append(MediumText(bold('Ian Dover')))

    return doc

if __name__ == '__main__':
    geometry_options = {'margin': '0.7in'}
    doc = Document(geometry_options = geometry_options)

    doc = generate_header(doc, date.today())

    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)

    # Read and display the image
    with doc.create(Section('Read and display the image:')):
        doc.append('The rose on ice image:')

        image_path = os.path.join(parent_directory, '..', '..', 'images', 'RoseonIce-1.jpg')

        with doc.create(Figure(position = 'h!')) as first_figure:
            first_figure.add_image(image_path, width = '120px')
            first_figure.add_caption('Rose on ice image.')

    # Part 1
    with doc.create(Section('Part 1')):
        # 2 Clusters
        with doc.create(Subsection('K-means Clustering: 2 Clusters')):
            doc.append('Image split into two clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_2.jpg')

            with doc.create(Figure(position = 'h!')) as second_figure:
                second_figure.add_image(image_path, width = '120px')
                second_figure.add_caption('Image with K-means Clustering: 2 Clusters.')

        with doc.create(Subsection('K-means Clustering Histogram: 2 Clusters')):
            doc.append('Histogram of the image split into two clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_2_histogram.jpg')

            with doc.create(Figure(position = 'h!')) as third_figure:
                third_figure.add_image(image_path, width = '200px')
                third_figure.add_caption('Histogram of image with K-means Clustering: 2 Clusters.')

        doc.append(NewPage())

        # 3 Clusters
        with doc.create(Subsection('K-means Clustering: 3 Clusters')):
            doc.append('Image split into three clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_3.jpg')

            with doc.create(Figure(position = 'h!')) as second_figure:
                second_figure.add_image(image_path, width = '120px')
                second_figure.add_caption('Image with K-means Clustering: 3 Clusters.')

        with doc.create(Subsection('K-means Clustering Histogram: 3 Clusters')):
            doc.append('Histogram of the image split into three clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_3_histogram.jpg')

            with doc.create(Figure(position = 'h!')) as third_figure:
                third_figure.add_image(image_path, width = '200px')
                third_figure.add_caption('Histogram of image with K-means Clustering: 3 Clusters.')

        # 4 Clusters
        with doc.create(Subsection('K-means Clustering: 4 Clusters')):
            doc.append('Image split into four clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_4.jpg')

            with doc.create(Figure(position = 'h!')) as second_figure:
                second_figure.add_image(image_path, width = '120px')
                second_figure.add_caption('Image with K-means Clustering: 4 Clusters.')

        doc.append(NewPage())

        with doc.create(Subsection('K-means Clustering Histogram: 4 Clusters')):
            doc.append('Histogram of the image split into four clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_4_histogram.jpg')

            with doc.create(Figure(position = 'h!')) as third_figure:
                third_figure.add_image(image_path, width = '200px')
                third_figure.add_caption('Histogram of image with K-means Clustering: 4 Clusters.')

        # 5 Clusters
        with doc.create(Subsection('K-means Clustering: 5 Clusters')):
            doc.append('Image split into five clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_5.jpg')

            with doc.create(Figure(position = 'h!')) as second_figure:
                second_figure.add_image(image_path, width = '120px')
                second_figure.add_caption('Image with K-means Clustering: 5 Clusters.')

        with doc.create(Subsection('K-means Clustering Histogram: 5 Clusters')):
            doc.append('Histogram of the image split into five clusters:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_1_kmeans_5_histogram.jpg')

            with doc.create(Figure(position = 'h!')) as third_figure:
                third_figure.add_image(image_path, width = '200px')
                third_figure.add_caption('Histogram of image with K-means Clustering: 5 Clusters.')

    # Part 2
    with doc.create(Section('Part 2')):
        with doc.create(Subsection('Convert the image into greyscale:')):
            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_2_grayscale.jpg')

            with doc.create(Figure(position = 'h!')) as second_figure:
                second_figure.add_image(image_path, width = '120px')
                second_figure.add_caption('Convert the image into greyscale.')

        with doc.create(Subsection('Plot the histogram:')):
            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem3', 'p3_2_histogram.jpg')

            with doc.create(Figure(position = 'h!')) as third_figure:
                third_figure.add_image(image_path, width = '200px')
                third_figure.add_caption('Histogram of greyscale image.')

    doc.generate_pdf('problem3', clean_tex = False)