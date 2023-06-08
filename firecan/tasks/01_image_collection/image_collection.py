import requests
import time
import datetime

from common import DATA_PATH
from PIL import Image

from io import BytesIO

cwfis_root = 'https://cwfis.cfs.nrcan.gc.ca'


fb_types = ['hfi', 'tfc', 'sfc', 'fmc', 'cfb', 'ros', 'ft']
fm3_types = ['tri']


def date_iterator(date_str: str) -> str:
    curr = datetime.date(int(date_str[0:4]), int(date_str[4:6]), int(date_str[6:]))
    prior = curr - datetime.timedelta(days=1)
    return prior.strftime(format="%Y%m%d")

def request_image_page(img_type: str, date_str: str):
    try:
        response = requests.get(f"{cwfis_root}/data/maps/fwi_fbp/{date_str[0:4]}/{img_type}{date_str}.png")
        response.raise_for_status()
    except requests.RequestException as e:
        raise e
    except Exception as e:
        raise e
    
    return response


def store_image(response: requests.Response, img_type: str, date_str: str):
    with Image.open(BytesIO(response.content)) as i:
        i.save(fp=DATA_PATH/ f"{img_type}_{date_str}.png")
    i.close()
    

def scrape_images(n: int=5, img_type: str='ft', date_str: str="20230607"):
    while n > 0:
        response = request_image_page(img_type=img_type, date_str=date_str)
        store_image(response=response, img_type=img_type, date_str=date_str)
        n-=1
        date_str = date_iterator(date_str=date_str)
        time.sleep(1.5)
    return n
