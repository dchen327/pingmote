'''
Poor Man's Discord Nitro - A Python GUI for selecting and inserting local images

Author: David Chen
'''
import PySimpleGUI as sg
import pyautogui
import subprocess
import json
from pathlib import Path
from time import sleep


# CONFIGS
GUI_BG_COLOR = '#36393F'  # copied from discord colors
# top left corner of emote picker, (0, 0) is screen top left
# WINDOW_LOCATION = (200, 800)
# WINDOW_LOCATION = pyautogui.position()
NUM_COLS = 12  # max number of images per row in picker
NUM_FREQUENT = 12  # max number of images to show in the frequent section
# absolute paths necessary here if running the program globally
MAIN_PATH = Path('/home/dchen327/coding/projects/pingmote/')
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
        curr_row = []
        # layout the frequents section (start idx at 1 for row checking)
        for idx, img in enumerate(self.frequents, start=1):
            curr_row.append(
                sg.Button('', key=IMAGE_PATH / img, image_filename=IMAGE_PATH / img, image_subsample=1))
            if idx % NUM_COLS == 0:  # start new row
                self.layout.append(curr_row)
                curr_row = []
        self.layout.append(curr_row)

        self.layout.append([sg.HorizontalSeparator()])

        # layout the main section
        curr_row = []
        idx = 0
        for img in IMAGE_PATH.iterdir():  # add images to self.layout
            if img.name in self.frequents:  # don't show same image in both sections
                continue
            idx += 1

            curr_row.append(
                sg.Button('', key=img, image_filename=img, image_subsample=1))
            if idx % NUM_COLS == 0:  # start new row
                self.layout.append(curr_row)
                curr_row = []
        self.layout.append(curr_row)

    def create_window_gui(self):
        """ Create the window from layout """
        window = sg.Window('Emote Picker', self.layout)
        # event loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:  # X clicked
                break
            window.close()
            self.copy_to_clipboard(event)  # copy clicked image to clipboard

            if AUTO_PASTE:
                # wait a bit for copy operation before pasting
                sleep(SLEEP_TIME)
                pyautogui.hotkey('ctrl', 'v')  # paste
                if AUTO_ENTER:
                    sleep(SLEEP_TIME)
                    pyautogui.press('enter')  # hit enter
            # increment count for chosen image
            if event.name not in self.frequencies:
                self.frequencies[event.name] = 0
            self.frequencies[event.name] += 1
            self.write_frequencies(self.frequencies)

    def find_window_location(self):
        """ Open the window near where the mouse currently is 
            TODO: Add checking to ensure window is on screen
        """
        mouse_x, mouse_y = pyautogui.position()
        # open window with the mouse cursor somewhere in the middle, near top left (since top left is most frequent)
        return (mouse_x - 125, mouse_y - 60)

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
        return [img for img, freq in desc_frequencies[:NUM_FREQUENT]]

    def copy_to_clipboard(self, img_path):
        """ Given an an image path, copy the image to clipboard """
        command = f'xclip -sel clip -t image/png {img_path.absolute()}'
        subprocess.run(command.split())


if __name__ == '__main__':
    pingmote = PingMote()
