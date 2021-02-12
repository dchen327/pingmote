import PySimpleGUI as sg
from copy import deepcopy
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Controller as MouseController
from time import time

SHORTCUT = '<alt>+q'  # wrap special keys with <> like <ctrl>
# on some operating systems, there might be issues with stuff not closing properly
KILL_SHORTCUT = '<ctrl>+<alt>+k'


class GUITest:

    def __init__(self):
        sg.theme('DarkAmber')   # Add a touch of color
        # All the stuff inside your window.
        self.layout = [[sg.Text('Some text on Row 1')],
                       [sg.Button('Ok'), sg.Button('Cancel')]]

    def create_window_gui(self):
        # Create the Window
        window = sg.Window('Window Title', self.layout)
        # Event Loop to process "events" and get the "values" of the inputs
        event, _ = window.read()
        print('Event:', event)

        window.close()


class GUITestWithKB:
    def __init__(self):
        sg.theme('DarkAmber')   # Add a touch of color
        self.layout = [[sg.Text('Some text on Row 1')],
                       [sg.Button('Ok'), sg.Button('Cancel')]]

    def create_window_gui(self):
        # Create the Window
        window = sg.Window('Window Title', deepcopy(self.layout))
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, _ = window.read(timeout=100)
            if event == sg.WIN_CLOSED:
                break  # the use has closed the window
            if event == sg.TIMEOUT_KEY:
                continue
            print(event)
            window.close()

        window.close()

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
        self.create_window_gui()

    def kill_all(self):
        """ Kill the script in case it's frozen or buggy """
        quit()


if __name__ == '__main__':
    # guitest = GUITest()
    # guitest.create_window_gui()
    guitest2 = GUITestWithKB()
    guitest2.setup_pynput()
