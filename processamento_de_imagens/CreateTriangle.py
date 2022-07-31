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

def createFranceFlag(width):
    BLUE = (0, 85, 164)
    WHITE = (255, 255, 255)
    RED = (239, 65, 53)

    height = width*2//3    

    image = Image.new("RGB", (width, height), BLUE)

    band_width = width//3

    for x in range(band_width):
        for y in range(height):
            image.putpixel((x + band_width, y), WHITE)
            image.putpixel((x + band_width*2, y), RED)

    return image

if __name__ == "__main__":
    france_flag = createFranceFlag(600)
    france_flag.show()