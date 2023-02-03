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
    image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem1', 'p1_a_grayscale.jpg')

    with doc.create(Section('Section 1')):
        doc.append('Image converted to greyscale:')
        with doc.create(Figure(position = 'c')) as first_figure:
            first_figure.add_image(image_path, width = '120px')
            first_figure.add_caption('Greyscale dimensionally reduces the image and assigns weights to RGB values to created a weighted sum.')

    doc.generate_pdf('problem1', clean_tex = False)