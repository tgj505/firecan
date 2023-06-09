import datetime
import random
import requests
import time

from io import BytesIO

from PIL import Image

from common import PNG_PATH, fm3_types

cwfis_root = "https://cwfis.cfs.nrcan.gc.ca"


def date_iterator(date_str: str) -> str:
    curr = datetime.date(int(date_str[:4]), int(date_str[4:6]), int(date_str[6:]))
    prior = curr - datetime.timedelta(days=1)
    return prior.strftime(format="%Y%m%d")


def check_image_existence(img_type: str, date_str: str) -> bool:
    try:
        with open(PNG_PATH / f"{img_type}_{date_str}.png") as f:
            return True
    except FileNotFoundError:
        return False


def request_image_page(img_type: str, date_str: str) -> requests.Response:
    if img_type in fm3_types:
        url = f"{cwfis_root}/data/maps/fireM3/{date_str[0:4]}/{img_type}{date_str}.png"
    elif img_type in ["zh","stab", "umix", "vi", "adi"]:
        url = f"{cwfis_root}/data/maps/fwi_fbp/{date_str[0:4]}/{img_type}{date_str}.png"
    else:
        url = f"{cwfis_root}/data/maps/fwi_fbp/{date_str[0:4]}/sf/{img_type}{date_str}.png"
    try:
        response = requests.request(method="GET", url=url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        raise e
    except Exception as e:
        raise e


def store_image(response: requests.Response, img_type: str, date_str: str):
    with Image.open(BytesIO(response.content)) as i:
        i.save(fp=PNG_PATH / f"{img_type}_{date_str}.png")


def scrape_images(n: int, img_type: str, date_str: str):
    while n > 0:
        if check_image_existence(img_type=img_type, date_str=date_str) is True:
            pass
        else:
            try:
                response = request_image_page(img_type=img_type, date_str=date_str)
                store_image(response=response, img_type=img_type, date_str=date_str)
            except Exception as e:
                print(f"Can't scrape {img_type} for {date_str}:{e}")

            time.sleep(random.uniform(1, 2))
        n -= 1
        date_str = date_iterator(date_str=date_str)

    return n
