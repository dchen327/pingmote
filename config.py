"""

"""
from pathlib import Path
import platform

""" Hotkeys """
SHORTCUT = 'ctrl+q' if platform.system() != 'Darwin' else 'command+3'
KILL_SHORTCUT = 'alt+shift+k' if platform.system() != 'Darwin' else 'command+4'

""" Emote Picker """
NUM_COLS = 12  # max number of images per row in picker
SHOW_FREQUENTS = True  # show the frequents section at the top
NUM_FREQUENT = 12  # max number of images to show in the frequent section
SHOW_LABELS = True  # show section labels (frequents, static, gifs)
SEPARATE_GIFS = True  # separate static emojis and gifs into different sections
WINDOW_LOCATION = (100, 100)  # initial position of GUI (before dragging)
GUI_BG_COLOR = '#36393F'  # background color (copied from discord colors)

""" Functionality """
AUTO_PASTE = True  # automatically paste the image after selection
AUTO_ENTER = True  # hit enter after pasting (useful in Discord)

""" Paths """
MAIN_PATH = Path(__file__).parent  # directory with pingmote.py
IMAGE_PATH = MAIN_PATH / 'assets' / 'resized'  # resized emotes

""" Experimental """
SLEEP_TIME = 0  # add delay if pasting/enter not working
# paste by inserting rather than copy paste, can be unreliable
PRESERVE_CLIPBOARD = False
CUSTOM_HOTKEY_HANDLER = False  # workaround for alt+tab issues
