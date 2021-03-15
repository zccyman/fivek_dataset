import cv2
import os

import imageio
import glob
import tqdm

def tif2png(img_path):
    # image = cv2.imread(img_path)
    output_path = img_path.replace("fivek/output", "fivek_png/output/a")
    output_path = output_path.replace(".tif", ".png")
    # cv2.imwrite(output_path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    os.system(f"convert -profile sRGB_v4_ICC_preference.icc {img_path} {output_path}")
    print(output_path)

if __name__== '__main__':
    images_list = glob.glob("/home/developer/zhangcc/myopendatasets/color_enhancement/fivek/output/*.tif")
    for image_path in images_list:
        tif2png(image_path)
