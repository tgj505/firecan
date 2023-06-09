import pathlib


days_to_scrape = 35
maps_to_scrape = ['apt', 'ros', 'fdr']
fm3_types = ['tri', 'apt', 'fwih']
fb_types = ['hfi', 'tfc', 'sfc', 'fmc', 'cfb', 'ros', 'ft']
fw_types = ['fdr', 'fwi', 'ffmc', 'dmc', 'dc', 'isi', 'bui', 'dsr']
ROOT_PATH = pathlib.Path(__file__).absolute().parent.parent
DATA_PATH = ROOT_PATH / 'data'
PNG_PATH = DATA_PATH / 'raw_png'
GIF_PATH = DATA_PATH / 'gifs'
