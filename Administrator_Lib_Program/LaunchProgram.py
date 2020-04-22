from GUI import menu
from pathlib import Path
# Easy way to launch the program
ICONPATH = Path.cwd().parent / 'icons' / 'icon.ico'
MAINICON = Path.cwd().parent / 'icons' / 'mag.ico'
DATAPATH = Path.cwd().parent / 'library_database.db'
MENU = menu(str(MAINICON), str(ICONPATH), str(DATAPATH))
MENU.mainMenu()
