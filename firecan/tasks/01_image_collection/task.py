import image_collection
from common import fb_types
import tqdm


def main():
    for img_type in tqdm.tqdm(fb_types):
        starting_date = "20230607"
        image_collection.scrape_images(n=35, img_type=img_type, date_str=starting_date)

if __name__ == "__main__":
    main()