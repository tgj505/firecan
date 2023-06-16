import pathlib


days_to_scrape = 46
fm3_types = ["tri", "apt", "fwih"]
fb_types = ["hfi", "tfc", "sfc", "fmc", "cfb", "ros", "ft"]
fw_types = ["fdr", "fwi", "ffmc", "dmc", "dc", "isi", "bui", "dsr"]
w_types = ["temp", "ws", "adi", "zh", "stab", "precip", "rh", "umix", "vi"]
maps_to_scrape = fm3_types+fb_types+fw_types+w_types
ROOT_PATH = pathlib.Path(__file__).absolute().parent.parent
DATA_PATH = ROOT_PATH / "data"
PNG_PATH = DATA_PATH / "raw_png"
GIF_PATH = DATA_PATH / "gifs"
