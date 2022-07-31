from email.mime import image
from sre_parse import WHITESPACE
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


def create_japan_flag(width):

    height = width*2//3

    WHITE = (255, 255, 255)
    RED = (173, 35, 51)

    # The radius is 3/5 of the halph of the height flag
    radius = 3*height//10

    # Calculate the center point
    center = (width//2, height//2)

    # Create the image
    image = Image.new("RGB", (width, height), WHITE)

    # Loops only througth the pixels that are circumscriged
    # into the square that tangecies the red circle
    for x in range(center[0] - radius, center[0] + radius):
        for y in range(center[1] - radius, center[1] + radius):

            xc = center[0] - x
            yc = center[1] - y

            if((pow(xc, 2) + pow(yc, 2)) <= pow(radius, 2)):
                image.putpixel((x, y), RED)                                                                                                                                                                                                      
    
    return image

if __name__ == "__main__":
    japan_flag = create_japan_flag(600)
    japan_flag.show()