import keyboard
import chime

hotkeys = {
    "alt+w": "explorer.exe",
}


def customHotkey(event):
    for hotkeys__key, hotkeys__value in hotkeys.items():
        pressed = all(
            keyboard.is_pressed(split__value) != False
            for split__value in hotkeys__key.split('+')
        )

        if pressed:
            # do some actions
            print(pressed, hotkeys__value)
            chime.success()


keyboard.hook(customHotkey)
keyboard.wait('esc')
