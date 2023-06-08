import image_collection
from common import fb_types
import tqdm


def main():
    for img_type in tqdm.tqdm(fb_types):
        starting_date = "20230601"
        image_collection.scrape_images(n=14, img_type=img_type, date_str=starting_date)

if __name__ == "__main__":
    main()