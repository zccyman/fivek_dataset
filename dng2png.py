import rawpy
import imageio
import glob
import tqdm

def convert(img_path):
    with rawpy.imread(img_path) as raw:
        image = raw.postprocess(use_camera_wb=True, half_size=False,
                            no_auto_bright=True, output_bps=16)
    img_path = img_path.replace("fivek/input", "fivek_png/input/a")
    img_path = img_path.replace(".dng", ".png")
    imageio.imsave(img_path, image)

if __name__== '__main__':
    images_list = glob.glob("/home/developer/zhangcc/myopendatasets/color_enhancement/fivek/input/*.dng")
    for image_path in images_list:
        convert(image_path)
        print(image_path)