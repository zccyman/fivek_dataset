import cv2

import imageio
import glob
import tqdm

def convert(img_path):
    image = cv2.imread(img_path)
    img_path = img_path.replace("fivek/output", "fivek_png/output/a")
    img_path = img_path.replace(".tif", ".png")
    cv2.imwrite(img_path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

if __name__== '__main__':
    images_list = glob.glob("/home/developer/zhangcc/myopendatasets/color_enhancement/fivek/output/*.tif")
    for image_path in images_list:
        convert(image_path)
        print(image_path)