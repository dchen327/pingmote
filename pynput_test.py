from pynput import keyboard

SHORTCUT = '<alt>+f'


def on_activate():
    print('command pressed')


with keyboard.GlobalHotKeys({SHORTCUT: on_activate}) as h:
    h.join()
