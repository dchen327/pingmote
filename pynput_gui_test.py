import PySimpleGUI as sg
import threading
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyController


SHORTCUT = '<alt>+w'  # wrap special keys with <> like <ctrl>
# on some operating systems, there might be issues with stuff not closing properly
KILL_SHORTCUT = '<ctrl>+<alt>+k'

class PynputGUITest:
    def __init__(self):
        thread2 = threading.Thread(target=self.setup_pynput)
        thread2.start()

    def setup_pynput(self):
            """ Create mouse and keyboard controllers, setup hotkeys """
            self.keyboard = KeyController()
            with keyboard.GlobalHotKeys({
                SHORTCUT: self.on_activate,
                KILL_SHORTCUT: self.kill_all,
            }) as h:
                h.join()

    def on_activate(self):
        """ When hotkey is activated, layout a new GUI and show it """
        print('gui activated')
        self.show_gui()

    def kill_all(self):
        """ Kill the script in case it's frozen or buggy """
        print('kill all')
        quit()

    def show_gui(self):
        layout = [[sg.Output(size=(60,10))],
            [sg.Button('Go'), sg.Button('Nothing'), sg.Button('Exit')]  ]

        window = sg.Window('Window Title', layout)

        while True:             # Event Loop
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Go':
                print('About to go to call my long function')
            elif event == '-THREAD DONE-':
                print('Your long operation completed')
            else:
                print(event, values)
        window.close()

if __name__ == '__main__':
    pynput_gui_test = PynputGUITest()