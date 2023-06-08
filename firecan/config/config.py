import pathlib


fb_types = ['hfi', 'tfc', 'sfc', 'fmc', 'cfb', 'ros', 'ft', 'tri']
ROOT_PATH = pathlib.Path(__file__).absolute().parent.parent
DATA_PATH = ROOT_PATH / 'data'
PNG_PATH = DATA_PATH / 'raw_png'
GIF_PATH = DATA_PATH / 'gifs'
