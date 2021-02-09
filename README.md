# PingMote
Poor Man's Discord Nitro - A Python GUI for selecting and inserting local images
# Getting Started
Clone this repo: `git clone https://github.com/dchen327/pingmote.git` or download the code as a zip and extract. Change into the pingmote directory and run `pingmote.py`.
# Usage
Running `python3 pingmote.py` will bring up the emote picker, closing when you pick an image.

I recommend binding this python command to a global keyboard shortcut (in GNOME: keyboard shortcuts > custom shortcuts > `python3 /abs/path/to/pingmote.py`)

In Windows, this can be done with AutoHotKey, and on Mac there's probably something that'll work too (maybe Automator?)
# Demo
![ezgif com-gif-maker](https://user-images.githubusercontent.com/37674516/107125905-81540c80-687a-11eb-9def-b4e51f2b9d32.gif)

# Configs
- Set `WINDOW_LOCATION` to where you want the top left corner of the emote picker to come up
- Set `IMAGE_PATH` to the path where your resized images are stored (use an absolute path if you want to run this globally)
- Set `AUTO_PASTE` if you want to automatically paste after selecting
- Set `AUTO_ENTER` if you want to automatically hit enter after pasting
- Check the top of `pingmote.py` for a couple additional configs

# Adding Your Own Emotes
- Drop image files in the `original` folder, then run `image_resizer.py` which will resize all the images (ignoring gifs) and drop them in the `resized` folder
- Unfortunately, `image_resizer.py` is currently unable to resize gifs, so a website like [this](https://www.iloveimg.com/resize-image/resize-gif) is useful (although you can only resize like 12 max at a time). After downloading the resized gifs, extract them to the `original` folder in assets, then run `image_resizer.py` to create the resized folder while ignoring gifs
- Here are some good emote sources for both images/gifs (right click save image): [discordmojis.com](https://discordmojis.com/), [emoji.gg](https://emoji.gg/)

# Dependencies
These can be installed with `pip3 install -r requirements.txt`

PySimpleGUI (to display the image picker GUI)
PyAutoGUI (getting mouse position and keyboard commands (xdotool no longer needed!))
PIL (for running `image_resizer.py`)

## For Mac:
There seem to be some weird Mac GUI errors with Tkinter (testing soon)

# Additional Notes
- Since this program relies on pasting resized images as emotes, we can't use inline emotes or reacts.
- Images have slight padding in discord, so they don't look *exactly* the same as regular emotes

# TODOs
- Fix mac stuff (GUIs are super weird on mac)
- Record a new demo vid (with favorites bar)

# Reasons you should still buy Discord Nitro
- Support Discord!
- Inline emotes/gifs, keyboard shortcuts by name (ex: :emote_name:)
- React with emotes

# Contributors
David Chen (dchen327)

Luke Tong (Mac/Windows GUI + clipboard testing)