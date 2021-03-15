import os

import rawpy
import imageio
import glob
import tqdm

import numpy as np
from PIL import Image

def dng2tiff(img_path):
    # with rawpy.imread(img_path) as raw:
    #     image = raw.postprocess(use_camera_wb=True, half_size=False,
    #                         no_auto_bright=True, output_bps=16)
    # output_path = img_path.replace("fivek/input", "fivek_png/input/a")
    # output_path = output_path.replace(".dng", ".png")
    # imageio.imsave(output_path, image)
    os.system(f"dcraw -o 2 -6 -T {img_path}")
    print(img_path)

def tiff2png(img_path):
    output_path = img_path.replace("fivek/input", "fivek_png/input/a")
    output_path = output_path.replace(".tiff", ".png")
    os.system(f"convert -profile sRGB_v4_ICC_preference.icc {img_path} {output_path}")
    print(output_path)

if __name__== '__main__':
    images_list = glob.glob("/home/developer/zhangcc/myopendatasets/color_enhancement/fivek/input/*.dng")
    for image_path in images_list:
        dng2tiff(image_path)

    images_list = glob.glob("/home/developer/zhangcc/myopendatasets/color_enhancement/fivek/input/*.tiff")
    for image_path in images_list:
        tiff2png(image_path)
