# pingmote
A cross-platform Python global emote picker to quickly insert custom emotes and gifs *(Poor Man's Discord Nitro)*


# Demo
![ezgif com-gif-maker](https://user-images.githubusercontent.com/37674516/107125905-81540c80-687a-11eb-9def-b4e51f2b9d32.gif)

# How It Works
All images/gifs (properly sized) are stored in `assets/resized`. These images are shown in the GUI, and clicking on them copies the corresponding URL to clipboard (with options to auto-paste). The URLs are stored in `links.txt`, and filenames are in alphabetical order for now.

# Getting Started
- Clone this repo: `git clone https://github.com/dchen327/pingmote.git` or download the code as a zip and extract
- Change into the pingmote directory (make sure you can see `pingmote.py`)
- Run `pip3 install -r requirements.txt` to install all necessary dependencies

# Usage
Running `python3 pingmote.py` will start the script, and when you hit the shortcut specified at the top of `pingmote.py` (default `<alt>+w`), the emote picker will show up, allowing you to click and pick an emote to insert.

# Adding Your Own Emotes
- Sorry for this being a bit complicated, I'm working on simplifying the workflow
- Drop image files in the `original` folder, then run `image_resizer.py` which will resize all the images (ignoring gifs) and drop them in the `resized` folder
- Unfortunately, `image_resizer.py` is currently unable to resize gifs, so a website like [this](https://www.iloveimg.com/resize-image/resize-gif) is useful (although you can only resize like 12 max at a time). After downloading the resized gifs (64x64), extract them to the `original` folder in assets, then run `image_resizer.py` to create the resized folder while ignoring gifs
- Upload all files to an image hoster (I like [postimages](https://postimages.org/)). Copy all the direct image links (ending in the file extension) and paste them in `links.txt`
- Here are some good emote sources (right click save image): [discordmojis.com](https://discordmojis.com/), [emoji.gg](https://emoji.gg/)

# Configs
- Check the top of `pingmote.py` for configs

# Dependencies
These can be installed with `pip3 install -r requirements.txt`

- PySimpleGUI (to display the image picker GUI)
- pynput (getting mouse position and keyboard commands)
- pyperclip (copy pasting)
- PIL (for running `image_resizer.py`)

## For Mac:
There seems to be some weird Mac GUI errors with Tkinter (testing soon)

# Additional Notes
- Since this program relies on pasting image/gif URLs as emotes, we can't use inline emotes or reacts.
- Images have slight padding in discord, so they don't look *exactly* the same as regular emotes
- Websites that don't automembed image links won't work (ex: Facebook Messenger)

# TODOs
- Fix mac stuff (GUIs are super weird on mac)
- Record a new demo vid (with favorites bar)
- Better ordering of emotes (categorization, etc.)
- Simplify the process for adding new emotes
- Gif resizing? (idk PIL isn't very good for this)
- Ensure gif thumbnail isn't blank (not fully sure how to do this)
- Search emotes by keyword (would require files to be named, since most of my files now are just a bunch of numbers)
- Some hybrid mode for linux/mac that pastes local images and uses hosted gif links

# Reasons you should still buy Discord Nitro
- Support Discord!
- Inline emotes/gifs, keyboard shortcuts by name (ex: :emote_name:)
- React with emotes
- Other nitro benefits!

# Contributors
- [David Chen](https://github.com/dchen327) (Core Developer)
- [Luke Tong](https://github.com/luke-rt) (Mac/Windows GUI + clipboard testing)
- [Stephane Morel](https://github.com/SoAsEr) (Windows testing)

# Progress Timeline
- Initial method (50 lines): `xclip` for copying local images, `xdotool` for pasting and keyboard commands
- Switched to PyAutoGUI for keyboard simulation, `xdotool` no longer needed
- Wrote `image_resizer.py` for locally resizing images
- Uploaded images to postimages; simplified copy pasting of links only and not image data (removed all subprocess calls)
- Added frequents section for favorite emotes
- Added feature to open the GUI near the mouse cursor
- Cleaned up links for better file to link mapping
- Switched to `pynput` for cross-platform global hotkey mapping, fully removed PyAutoGUI dependencies
- Added section labels and ability to separate images and gifs