'''
pingmote: a cross-platform Python global emote picker to quickly insert custom images/gifs

Author: David Chen
'''
import PySimpleGUI as sg
import json
import pyperclip
from pathlib import Path
from time import sleep
from math import ceil
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Controller as MouseController


# CONFIGS

SHORTCUT = '<alt>+w'  # wrap special keys with <> like <ctrl>
# on some operating systems, there might be issues with stuff not closing properly
KILL_SHORTCUT = '<ctrl>+<alt>+k'
# if running globally, use an absolute path, otherwise use .
# MAIN_PATH = Path('/home/dchen327/coding/projects/pingmote/')
MAIN_PATH = Path('.')
IMAGE_PATH = MAIN_PATH / 'assets' / 'resized'
NUM_COLS = 12  # max number of images per row in picker
SHOW_FREQUENTS = True  # show the frequents section at the top
NUM_FREQUENT = 12  # max number of images to show in the frequent section
SHOW_LABELS = True  # show section labels (frequents, static, gifs)
SEPARATE_GIFS = True  # separate static emojis and gifs into different sections

AUTO_PASTE = True  # if True, automatically pastes the image after selection
# if True and AUTO_PASTE is True, hits enter after pasting (useful in Discord)
AUTO_ENTER = True
# if True and AUTO_PASTE is True, will paste without affecting clipboard
# NOTE: this pastes with pynput and can be unreliable; SLEEP_TIME might need to be set
# or else the beginning of the URL might get cut off
PRESERVE_CLIPBOARD = False

# ADDITIONAL CONFIGS

# top left corner of emote picker, (0, 0) is screen top left
WINDOW_LOCATION = None  # if set to None, will open the GUI near the mouse cursor
# if pasting or enter isn't working, add a short delay (in seconds)
SLEEP_TIME = 0
GUI_BG_COLOR = '#36393F'  # copied from discord colors


class PingMote():

    def __init__(self):
        # Load frequencies from json for frequents section
        self.frequencies = self.load_frequencies()
        self.frequents = self.get_frequents(self.frequencies)

        # Load links and file paths
        self.filename_to_link = self.load_links()

        # Setup
        self.setup_gui()
        self.setup_pynput()

    def setup_gui(self):
        sg.theme('LightBrown1')  # Use this as base theme
        # Set location for where the window opens, (0, 0) is top left
        sg.SetOptions(button_color=(GUI_BG_COLOR, GUI_BG_COLOR), background_color=GUI_BG_COLOR,
                      text_element_background_color=GUI_BG_COLOR, text_color='white', border_width=0)

    def layout_gui(self):
        """ Layout GUI with PySimpleGui """
        self.layout = []
        if SHOW_FREQUENTS:
            if SHOW_LABELS:
                self.layout.append([sg.Text('Frequently Used')])
            self.layout += self.layout_frequents_section()
            self.layout.append([sg.HorizontalSeparator()])
        self.layout += self.layout_main_section()

    def layout_frequents_section(self):
        """ Return a list of frequent emotes """
        return self.list_to_table([
            sg.Button('', key=img_name, image_filename=IMAGE_PATH / img_name)
            for img_name in self.frequents
        ])

    def layout_main_section(self):
        """ Return a list of main section emotes.
        If SEPARATE_GIFS is True, split into static and emoji sections
        """
        main_section = []
        statics, gifs = [], []
        for img in sorted(IMAGE_PATH.iterdir()):
            if SHOW_FREQUENTS and img.name in self.frequents:  # don't show same image in both sections
                continue
            button = sg.Button('', key=img.name, image_filename=img)
            if SEPARATE_GIFS:
                if img.suffix == '.png':
                    statics.append(button)
                else:  # gif
                    gifs.append(button)
            else:
                main_section.append(button)
        if SEPARATE_GIFS:
            combined = []
            if SHOW_LABELS:
                combined.append([sg.Text('Static')])
            combined += self.list_to_table(statics)
            if SHOW_LABELS:
                combined.append([sg.Text('GIFs')])
            combined += self.list_to_table(gifs)
            return combined

        return self.list_to_table(main_section)

    def create_window_gui(self):
        """ Create the window from layout """
        # single line one-shot GUI, no loop needed
        event, _ = sg.Window('Emote Picker', self.layout,
                             location=self.find_window_location()).read(close=True)
        if event is not None and event != sg.WINDOW_CLOSED:
            self.on_select(event)

    def on_select(self, event):
        """ Paste selected image non-destructively (if auto paste is True) """

        if AUTO_PASTE:
            if PRESERVE_CLIPBOARD:  # write text with pynput
                self.paste_selection(event)
            else:  # copy to clipboard then paste
                self.copy_to_clipboard(event)
                self.paste_link()
            if AUTO_ENTER:
                self.keyboard_enter()
        else:
            self.copy_to_clipboard(event)

        self.update_frequencies(event)  # update count for chosen image

    def copy_to_clipboard(self, filename):
        """ Given an an image, copy the image link to clipboard """
        pyperclip.copy(self.filename_to_link[filename])

    def paste_selection(self, filename):
        self.keyboard.type(self.filename_to_link[filename])

    def paste_link(self):
        """ Press ctrl + v to paste """
        sleep(SLEEP_TIME)  # wait a bit if needed
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        self.keyboard.release('v')
        self.keyboard.release(Key.ctrl)

    def keyboard_enter(self):
        """ Hit enter on keyboard to send pasted link """
        sleep(SLEEP_TIME)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def update_frequencies(self, filename):
        """ Increment chosen image's counter in frequencies.json """
        if filename not in self.frequencies:
            self.frequencies[filename] = 0
        self.frequencies[filename] += 1
        self.write_frequencies(self.frequencies)
        self.frequents = self.get_frequents(
            self.frequencies)  # update frequents list

    def find_window_location(self):
        """ Open the window near where the mouse currently is """
        if WINDOW_LOCATION:  # use user provided location
            return WINDOW_LOCATION
        mouse_x, mouse_y = self.mouse.position
        # open window with the mouse cursor somewhere in the middle, near top left (since top left is most frequent)
        return (mouse_x - 400, mouse_y - 300)

    def load_links(self):
        """ Load image links from links.txt """
        with open(MAIN_PATH / 'assets' / 'links.txt') as f:
            links = f.read().splitlines()
            return {link.rsplit('/', 1)[-1]: link for link in links}

    def load_frequencies(self):
        """ Load the frequencies dictionary from frequencies.json """
        with open(MAIN_PATH / 'assets' / 'frequencies.json', 'r') as f:
            return json.load(f)

    def write_frequencies(self, frequencies):
        """ Write new frequencies to frequencies.json """
        with open(MAIN_PATH / 'assets' / 'frequencies.json', 'w') as f:
            json.dump(frequencies, f, indent=4)

    def get_frequents(self, frequencies):
        """ Get the images used most frequently """
        # sort in descending order by frequency
        desc_frequencies = sorted(
            frequencies.items(), key=lambda x: x[-1], reverse=True)
        return [img for img, _ in desc_frequencies[:NUM_FREQUENT]]

    def list_to_table(self, a, num_cols=NUM_COLS):
        """ Given a list a, convert it to rows and columns
            ex) a = [1, 2, 3, 4, 5], num_cols = 2
            returns: [[1, 2], [3, 4], [5]]
            """
        return [a[i * num_cols:i * num_cols + num_cols] for i in range(ceil(len(a) / num_cols))]

    def setup_pynput(self):
        """ Create mouse and keyboard controllers, setup hotkeys """
        self.keyboard = KeyController()
        self.mouse = MouseController()
        with keyboard.GlobalHotKeys({
            SHORTCUT: self.on_activate,
            KILL_SHORTCUT: self.kill_all,
        }) as h:
            h.join()

    def on_activate(self):
        """ When hotkey is activated, layout a new GUI and show it """
        self.layout_gui()
        self.create_window_gui()

    def kill_all(self):
        """ Kill the script in case it's frozen or buggy """
        quit()


if __name__ == '__main__':
    pingmote = PingMote()
