import keyboard

keyboard.add_hotkey('windows+a', print, args=('triggered', 'hotkey'))

keyboard.wait('esc')