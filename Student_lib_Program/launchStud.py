from main import Mainclass
from pathlib import Path
from os import path

iconpath = Path.cwd() / 'icons' / 'mag.ico'
datapath = Path.cwd() / 'library_database.db'
if path.exists(iconpath) and path.exists(datapath):
    run = Mainclass(iconpath, datapath)
    run.searchMenu()