'''
Poor Man's Discord Nitro - A Python GUI for selecting and inserting local images

Author: David Chen
'''
import PySimpleGUI as sg
import pyautogui
import json
import pyperclip
from pathlib import Path
from time import sleep
from math import ceil


# CONFIGS
GUI_BG_COLOR = '#36393F'  # copied from discord colors
# top left corner of emote picker, (0, 0) is screen top left
# WINDOW_LOCATION = (200, 800)
# WINDOW_LOCATION = pyautogui.position()
NUM_COLS = 12  # max number of images per row in picker
NUM_FREQUENT = 12  # max number of images to show in the frequent section
SHOW_FREQUENTS = True  # show the frequents section at the top
# absolute paths necessary here if running the program globally
MAIN_PATH = Path('/home/dchen327/coding/projects/pingmote/')
# IMAGE_PATH = MAIN_PATH / 'assets' / 'resized'
IMAGE_PATH = MAIN_PATH / 'assets' / 'resized'
AUTO_PASTE = True  # if True, automatically pastes the image after selection
# if True and AUTO_PASTE is True, hits enter after pasting (useful in Discord)
AUTO_ENTER = True
# if pasting or enter isn't working, add a short delay (in seconds)
SLEEP_TIME = 0


class PingMote():

    def __init__(self):
        # Load frequencies from json for frequents section
        self.frequencies = self.load_frequencies()
        self.frequents = self.get_frequents(self.frequencies)

        # Load links and file paths
        self.filename_to_link = self.load_links()

        # GUI setup
        self.setup_gui()
        self.layout_gui()
        self.create_window_gui()

    def setup_gui(self):
        sg.theme('LightBrown1')  # Use this as base theme
        # Set location for where the window opens, (0, 0) is top left
        sg.SetOptions(button_color=(GUI_BG_COLOR, GUI_BG_COLOR), background_color=GUI_BG_COLOR,
                      text_element_background_color=GUI_BG_COLOR, text_color='white', border_width=0, window_location=self.find_window_location())

    def layout_gui(self):
        """ Layout GUI with PySimpleGui """
        self.layout = []
        frequents_section = []
        main_section = []
        idx = 0
        # add images to self.layout
        for img in sorted(IMAGE_PATH.iterdir()):
            if img.name in self.frequents:  # don't show same image in both sections
                frequents_section.append(
                    sg.Button('', key=img.name, image_filename=img))
            else:
                main_section.append(
                    sg.Button('', key=img.name, image_filename=img))
        if SHOW_FREQUENTS:
            self.layout += self.list_to_table(
                frequents_section)
            self.layout.append([sg.HorizontalSeparator()])
        self.layout += self.list_to_table(main_section)

    def create_window_gui(self):
        """ Create the window from layout """
        window = sg.Window('Emote Picker', self.layout)
        # event loop to process "events" and get the "values" of the inputs
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED:  # X clicked
                break
            window.close()
            self.on_select(event)

    def on_select(self, event):
        """ Copy the selected image's link to clipboard and update frequencies """
        self.copy_to_clipboard(event)  # copy clicked image to clipboard

        if AUTO_PASTE:
            # wait a bit for copy operation before pasting
            sleep(SLEEP_TIME)
            # paste
            pyautogui.hotkey('ctrl', 'v')
            if AUTO_ENTER:
                sleep(SLEEP_TIME)
                pyautogui.press('enter')  # hit enter

        self.update_frequencies(event)

    def update_frequencies(self, filename):
        """ Increment chosen image's counter in frequencies.json """
        if filename not in self.frequencies:
            self.frequencies[filename] = 0
        self.frequencies[filename] += 1
        self.write_frequencies(self.frequencies)

    def find_window_location(self):
        """ Open the window near where the mouse currently is 
        """
        mouse_x, mouse_y = pyautogui.position()
        # open window with the mouse cursor somewhere in the middle, near top left (since top left is most frequent)
        return (mouse_x - 125, mouse_y - 60)

    def load_links(self):
        """ Load image links from links.txt """
        with open(MAIN_PATH / 'links.txt') as f:
            links = f.read().splitlines()
            return {link.rsplit('/', 1)[-1]: link for link in links}

    def load_frequencies(self):
        """ Load the frequencies dictionary from frequencies.json """
        with open(MAIN_PATH / 'frequencies.json', 'r') as f:
            return json.load(f)

    def write_frequencies(self, frequencies):
        """ Write new frequencies to frequencies.json """
        with open(MAIN_PATH / 'frequencies.json', 'w') as f:
            json.dump(frequencies, f)

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
        return [a[i*num_cols:i*num_cols+num_cols] for i in range(ceil(len(a) / num_cols))]

    def copy_to_clipboard(self, idx):
        """ Given an an image idx, copy the image link to clipboard """
        pyperclip.copy(self.links[idx])


if __name__ == '__main__':
    pingmote = PingMote()
