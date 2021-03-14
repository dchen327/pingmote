from pathlib import Path

""" Hotkeys """
SHORTCUT = 'ctrl+q'
KILL_SHORTCUT = 'alt+shift+k'

""" Emote Picker """
NUM_COLS = 12  # max number of images per row in picker
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
SHOW_FREQUENTS = True  # show frequents section (disabling removes hide button)
SLEEP_TIME = 0  # add delay if pasting/enter not working
PRESERVE_CLIPBOARD = False  # avoids copying link to clipboard (unreliable)
CUSTOM_HOTKEY_HANDLER = True  # workaround for alt+tab issues
