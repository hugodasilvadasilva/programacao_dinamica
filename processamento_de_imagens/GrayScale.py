from audioop import avg
from PIL import Image 
from utils import in_path, out_path

def grayscale(file_name: str, base:int):
    '''
    # Description
    Converts a colored image to grayscale using the `base` informed.

    ## Parameters
    `file_name: str` with the name of the file. This file must be at `input` subfolder.
    `-base:int` with the corresponding option:
    - 0: utilize red value as base to convert the image to grayscale;
    - 1: utilize green value as base to convert the image to grayscale;
    - 2: utilize blue value as base to convert the image to grayscale;
    - 3: utilize average of red, green and blue as base to converte the image to grayscale.
    - other: any other value will convert to grayscale utilizing the most commum convertion which
    is 30% from red, 59% from green and 11% from blue.
    `- return: a new image in grayscale
    '''    

    colored_img = Image.open(in_path(file_name))

    w, h = colored_img.size

    gs_image = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            colored_pixel = colored_img.getpixel((x, y))

            gs_pixel = ()
            if(base in [0, 1, 2]):
                gs_pixel = (colored_pixel[base], colored_pixel[base], colored_pixel[base])
            elif(base == 4):
                ap = (colored_pixel[0] + colored_pixel[1] + colored_pixel[2])//3
                gs_pixel = (ap, ap, ap)
            else:
                ap = int(0.3*colored_pixel[0] + 0.59*colored_pixel[1] + 0.11*colored_pixel[2])//3
                gs_pixel = (ap, ap, ap)

            gs_image.putpixel((x, y), gs_pixel)
    
    gs_image.save(out_path("gs_" + str(base) + "_" + file_name))
    gs_image.show()


if(__name__ == "__main__"):
    grayscale("gato01.jpeg", 2)
