from common import maps_to_scrape
import tqdm
import animation


def main():
    for img_type in tqdm.tqdm(maps_to_scrape):
        animation.make_gif(img_type=img_type)


if __name__ == "__main__":
    main()
