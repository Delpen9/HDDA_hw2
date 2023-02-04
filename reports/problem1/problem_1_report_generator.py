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
        doc.append(LargeText(bold('HW2: Problem 1')))
        doc.append(LineBreak())
        doc.append(MediumText(bold('Ian Dover')))

    return doc

if __name__ == '__main__':
    geometry_options = {'margin': '0.7in'}
    doc = Document(geometry_options = geometry_options)

    doc = generate_header(doc, date.today())

    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)

    # Part A
    with doc.create(Section('Part A')):
        doc.append('Image converted to greyscale:')

        image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_a_grayscale.jpg')

        with doc.create(Figure(position = 'h!')) as first_figure:
            first_figure.add_image(image_path, width = '120px')
            first_figure.add_caption('Greyscale image.')

    # Part B
    with doc.create(Section('Part B')):
        with doc.create(Subsection('Subsection 1')):
            doc.append('Image with zero-mean Gaussian white noise with variance of 0.01:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_b_1_gaussian.jpg')

            with doc.create(Figure(position = 'h!')) as second_figure:
                second_figure.add_image(image_path, width = '120px')
                second_figure.add_caption('J1: Greyscale image with gaussian noise applied.')

        with doc.create(Subsection('Subsection 2')):
            doc.append(r'Image with salt-and-pepper noise, affecting approximately 5% of pixels:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_b_2_salt_and_pepper.jpg')

            with doc.create(Figure(position = 'h!')) as third_figure:
                third_figure.add_image(image_path, width = '120px')
                third_figure.add_caption('J2: Greyscale image with salt-and-pepper noise applied.')

    # Part C
    with doc.create(Section('Part C')):
        with doc.create(Subsection('Gaussian De-noise: J1')):
            doc.append('Images with gaussian filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_1_j1.jpg')

            with doc.create(Figure(position = 'h!')) as fourth_figure:
                fourth_figure.add_image(image_path, width = '120px')
                fourth_figure.add_caption('Gaussian filter denoised J1.')

        with doc.create(Subsection('Gaussian De-noise: J2')):
            doc.append('Images with gaussian filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_1_j2.jpg')

            with doc.create(Figure(position = 'h!')) as fifth_figure:
                fifth_figure.add_image(image_path, width = '120px')
                fifth_figure.add_caption('Gaussian filter denoised J2.')

        with doc.create(Subsection('Median De-noise: J1')):
            doc.append('Images with median filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_2_j1.jpg')

            with doc.create(Figure(position = 'h!')) as sixth_figure:
                sixth_figure.add_image(image_path, width = '120px')
                sixth_figure.add_caption('Median filter denoised J1.')

        with doc.create(Subsection('Median De-noise: J2')):
            doc.append('Images with median filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_2_j2.jpg')

            with doc.create(Figure(position = 'h!')) as seventh_figure:
                seventh_figure.add_image(image_path, width = '120px')
                seventh_figure.add_caption('Median filter denoised J2.')


    doc.generate_pdf('problem1', clean_tex = False)