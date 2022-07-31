from audioop import avg
from functools import reduce
from PIL import Image 
from utils import in_path, out_path
from GrayScale import grayscale

def borderfilter(file_name:str, slope: int) -> Image.Image:
    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)

    ori_img = Image.open(in_path(file_name))
    ori_img_gs = grayscale(file_name, 3)

    w, h = ori_img.size

    flt_img = Image.new("RGB", (w, h))

    for x in range(0,10):
        for y in range(0,10):

            color = WHITE
            if(x > 0):
                pxl = ori_img_gs.getpixel((x,y))
                lft = ori_img_gs.getpixel((x - 1,y))

                print(pxl)

                if(pxl[0] > lft[0] + slope):
                    color = BLACK
                
            flt_img.putpixel((x, y), color)
    
    return flt_img


if(__name__ == "__main__"):
    
    img = borderfilter("gato01.jpeg", 5)
    img.show()