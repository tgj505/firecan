import requests
import time
import datetime
from io import BytesIO

from PIL import Image

from common import PNG_PATH

cwfis_root = 'https://cwfis.cfs.nrcan.gc.ca'

def date_iterator(date_str: str) -> str:
    curr = datetime.date(int(date_str[:4]), int(date_str[4:6]), int(date_str[6:]))
    prior = curr - datetime.timedelta(days=1)
    return prior.strftime(format="%Y%m%d")

def check_image_existence(img_type: str, date_str: str) -> bool:
    try:
        with open(PNG_PATH/ f"{img_type}_{date_str}.png") as f:
            return True
    except FileNotFoundError:
        return False

def request_image_page(img_type: str, date_str: str) -> requests.Response:
    if img_type == 'tri':
        url = f"{cwfis_root}/data/maps/fireM3/{date_str[0:4]}/{img_type}{date_str}.png"
    else:
        url = f"{cwfis_root}/data/maps/fwi_fbp/{date_str[0:4]}/{img_type}{date_str}.png"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        raise e
    except requests.exceptions.HTTPError as e:
        print('httpError')
        raise e
    except Exception as e:
        raise e


def store_image(response: requests.Response, img_type: str, date_str: str):
    with Image.open(BytesIO(response.content)) as i:
        i.save(fp=PNG_PATH/ f"{img_type}_{date_str}.png")
    

def scrape_images(n: int=5, img_type: str='ft', date_str: str="20230607"):
    while n > 0:
        if check_image_existence(img_type=img_type, date_str=date_str) is True:
            pass
        else:
            response = request_image_page(img_type=img_type, date_str=date_str)
            store_image(response=response, img_type=img_type, date_str=date_str)
            time.sleep(1.5)
        n-=1
        date_str = date_iterator(date_str=date_str)
        
    return n
