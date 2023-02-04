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

    doc.append(NewPage())

    # Part C
    with doc.create(Section('Part C')):
        # Gaussian
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

        # Median
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

        doc.append(NewPage())

        # Arithematic Mean
        with doc.create(Subsection('Arithematic Mean De-noise: J1')):
            doc.append('Images with arithematic mean filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_3_j1.jpg')

            with doc.create(Figure(position = 'h!')) as eigth_figure:
                eigth_figure.add_image(image_path, width = '120px')
                eigth_figure.add_caption('Arithematic mean filter denoised J1.')

        with doc.create(Subsection('Arithematic Mean De-noise: J2')):
            doc.append('Images with arithematic mean filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_3_j2.jpg')

            with doc.create(Figure(position = 'h!')) as ninth_figure:
                ninth_figure.add_image(image_path, width = '120px')
                ninth_figure.add_caption('Arithematic mean filter denoised J2.')

        # Geometric Mean
        with doc.create(Subsection('Geometric Mean De-noise: J1')):
            doc.append('Images with geometric mean filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_4_j1.jpg')

            with doc.create(Figure(position = 'h!')) as tenth_figure:
                tenth_figure.add_image(image_path, width = '120px')
                tenth_figure.add_caption('Geometric mean filter denoised J1.')

        with doc.create(Subsection('Geometric Mean De-noise: J2')):
            doc.append('Images with geometric mean filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_4_j2.jpg')

            with doc.create(Figure(position = 'h!')) as eleventh_figure:
                eleventh_figure.add_image(image_path, width = '120px')
                eleventh_figure.add_caption('Geometric mean filter denoised J2.')

        # Harmonic Mean
        with doc.create(Subsection('Harmonic Mean De-noise: J1')):
            doc.append('Images with harmonic mean filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_5_j1.jpg')

            with doc.create(Figure(position = 'h!')) as twelth_figure:
                twelth_figure.add_image(image_path, width = '120px')
                twelth_figure.add_caption('Harmonic mean filter denoised J1.')

        with doc.create(Subsection('Harmonic Mean De-noise: J2')):
            doc.append('Images with harmonic mean filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_5_j2.jpg')

            with doc.create(Figure(position = 'h!')) as thirteenth_figure:
                thirteenth_figure.add_image(image_path, width = '120px')
                thirteenth_figure.add_caption('Harmonic mean filter denoised J2.')

        # Contraharmonic Mean
        # with doc.create(Subsection('Contraharmonic Mean De-noise: J1')):
        #     doc.append('Images with contraharmonic mean filter denoise on J1:')

        #     image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_6_j1.jpg')

        #     with doc.create(Figure(position = 'h!')) as fourteenth_figure:
        #         fourteenth_figure.add_image(image_path, width = '120px')
        #         fourteenth_figure.add_caption('Contraharmonic mean filter denoised J1.')

        # with doc.create(Subsection('Contraharmonic Mean De-noise: J2')):
        #     doc.append('Images with contraharmonic mean filter denoise on J2:')

        #     image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_6_j2.jpg')

        #     with doc.create(Figure(position = 'h!')) as fifteenth_figure:
        #         fifteenth_figure.add_image(image_path, width = '120px')
        #         fifteenth_figure.add_caption('Contraharmonic mean filter denoised J2.')

        # Minimum
        with doc.create(Subsection('Minimum De-noise: J1')):
            doc.append('Images with minimum filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_7_j1.jpg')

            with doc.create(Figure(position = 'h!')) as sixteenth_figure:
                sixteenth_figure.add_image(image_path, width = '120px')
                sixteenth_figure.add_caption('Minimum filter denoised J1.')

        with doc.create(Subsection('Minimum De-noise: J2')):
            doc.append('Images with minimum filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_7_j2.jpg')

            with doc.create(Figure(position = 'h!')) as seventeenth_figure:
                seventeenth_figure.add_image(image_path, width = '120px')
                seventeenth_figure.add_caption('Minimum filter denoised J2.')

        doc.append(NewPage())

        # Maximum
        with doc.create(Subsection('Maximum De-noise: J1')):
            doc.append('Images with maximum filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_8_j1.jpg')

            with doc.create(Figure(position = 'h!')) as eighteenth_figure:
                eighteenth_figure.add_image(image_path, width = '120px')
                eighteenth_figure.add_caption('Maximum filter denoised J1.')

        with doc.create(Subsection('Maximum De-noise: J2')):
            doc.append('Images with maximum filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_8_j2.jpg')

            with doc.create(Figure(position = 'h!')) as nineteenth_figure:
                nineteenth_figure.add_image(image_path, width = '120px')
                nineteenth_figure.add_caption('Maximum filter denoised J2.')

        # Mid-point
        with doc.create(Subsection('Mid-point De-noise: J1')):
            doc.append('Images with mid-point filter denoise on J1:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_8_j1.jpg')

            with doc.create(Figure(position = 'h!')) as twentieth_figure:
                twentieth_figure.add_image(image_path, width = '120px')
                twentieth_figure.add_caption('Mid-point filter denoised J1.')

        with doc.create(Subsection('Mid-point De-noise: J2')):
            doc.append('Images with mid-point filter denoise on J2:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_c_8_j2.jpg')

            with doc.create(Figure(position = 'h!')) as twentyoneieth_figure:
                twentyoneieth_figure.add_image(image_path, width = '120px')
                twentyoneieth_figure.add_caption('Mid-point filter denoised J2.')

    doc.generate_pdf('problem1', clean_tex = False)