from common import DATA_PATH
from PIL import Image
import glob


def make_gif(img_type: str):
    # from here: https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/
    frames = [Image.open(image) for image in sorted(glob.glob(f"{DATA_PATH}/{img_type}*.png"))]
    frame_one = frames[0]
    frame_one.save(f"{img_type}.gif", format="GIF", append_images=frames,
               save_all=True, duration=250, loop=0)

    
