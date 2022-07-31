from PIL import Image
import os 

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename: str):
    '''
    # Description

    Gets the relative path to `filename` that must be at `input`
    folder

    ## Parameters
    `- filename:str` the name of the target file. This file must be
    located at `INPUT_FOLDER`;
    `- return:str` the relative path to `filename`.
    '''

    return os.path.join(INPUT_FOLDER, filename)

image = Image.new("RGB", (700,700), (10, 55, 30))
image.show()