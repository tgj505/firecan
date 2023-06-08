from common import fb_types
import tqdm
import animation


def main():
    for img_type in tqdm.tqdm(fb_types):
        animation.make_gif(img_type=img_type)

if __name__ == "__main__":
    main()