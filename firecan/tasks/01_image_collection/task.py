import image_collection
from common import fb_types, fm3_types
import tqdm
import datetime


def main():
    for img_type in tqdm.tqdm(fb_types+fm3_types):
        image_collection.scrape_images(n=35, img_type=img_type, date_str=datetime.datetime.today().strftime('%Y%m%d'))

if __name__ == "__main__":
    main()