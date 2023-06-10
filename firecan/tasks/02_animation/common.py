import sys
from pathlib import Path

# Get the absolute path of the repo
project_path = Path(__file__).absolute().parent.parent.parent
sys.path.insert(0, str(project_path))

# and import all necessary configuration
from config.config import *
