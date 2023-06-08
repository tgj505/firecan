import image_collection
import tqdm


def main():
    for img_type in tqdm.tqdm(image_collection.fb_types):
        starting_date = "20230607"
        image_collection.scrape_images(n=7, img_type=img_type, date_str=starting_date)

if __name__ == "__main__":
    main()