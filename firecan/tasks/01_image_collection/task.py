import image_collection
from common import maps_to_scrape, days_to_scrape
import tqdm
import datetime


def main():
    for img_type in tqdm.tqdm(maps_to_scrape):
        image_collection.scrape_images(
            n=days_to_scrape,
            img_type=img_type,
            date_str=datetime.datetime.today().strftime("%Y%m%d"),
        )


if __name__ == "__main__":
    main()
