# pingmote
A cross-platform Python global emote picker to quickly insert custom images/gifs 

Motivation: *Poor Man's Discord Nitro*


# Demo
![pingmote demo](https://user-images.githubusercontent.com/37674516/107857226-1e72f000-6dfb-11eb-8a9a-e938368b65bc.gif)

# How It Works
All images/gifs (properly sized) are stored in `assets/resized`. These images are shown in the GUI, and clicking on them copies the corresponding URL to clipboard (with options to auto-paste). The URLs are stored in `links.txt`.

# Getting Started
- Clone this repo: `git clone https://github.com/dchen327/pingmote.git` or download the code as a zip and extract
- Change into the pingmote directory (make sure you can see `pingmote.py`)
- Run `pip install -r requirements.txt` to install all necessary dependencies (use `pip3` if needed)

# Usage
Running `python pingmote.py` (or `python3 pingmote.py`) will start the script, and when you hit the shortcut specified at the top of `pingmote.py` (default `<alt>+w`), the emote picker will show up, allowing you to click and pick an emote to insert.

# Adding Your Own Emotes
- Sorry for this being a bit complicated, I'm working on simplifying the workflow
- Drop image files in the `original` folder, then run `image_resizer.py` which will resize all the images (ignoring gifs) and drop them in the `resized` folder
- Unfortunately, `image_resizer.py` is currently unable to resize gifs, so a website like [this](https://www.iloveimg.com/resize-image/resize-gif) is useful (although you can only resize like 12 max at a time). After downloading the resized gifs (64x64), extract them to the `original` folder in assets, then run `image_resizer.py` to create the resized folder while ignoring gifs
- Upload all files to an image hoster (I like [postimages](https://postimages.org/)). Copy all the direct image links (ending in the file extension) and paste them in `links.txt`
- Imgur will not work in the current implementation, since imgur links do not contain the original filename
- Here are some good emote sources (right click save image): [discordmojis.com](https://discordmojis.com/), [emoji.gg](https://emoji.gg/)

# Configs
- Check the top of `pingmote.py` for configs

# Dependencies
These can be installed with `pip install -r requirements.txt`

- PySimpleGUI (to display the image picker GUI)
- pynput (getting mouse position and keyboard commands)
- pyperclip (copy pasting)
- PIL (for running `image_resizer.py`)

## For Mac:
There seems to be some weird Mac GUI errors with Tkinter (testing soon)

# Notes
- Since this program relies on pasting image/gif URLs as emotes, we can't use inline emotes or reacts.
- Images have slight padding in discord, so they don't look *exactly* the same as regular emotes
- Pretty much only Discord works (Facebook Messenger and Slack don't)
- In addition, Facebook and Slack don't look good when images are directly pasted in either

# TODOs
- Testing on Mac (current issue: pynput permissions and ctrl/alt detection broken, GUI seems fine on Python 3.9)
- Testing on Windows (current issue: pynput being inconsistent, might be because of threading and GUI conflicts)
- Better ordering of emotes (categorization, etc.)
- Simplify the process for adding new emotes
- Gif resizing? (idk PIL isn't very good for this)
- Ensure gif thumbnail isn't blank (not fully sure how to do this)
- Search emotes by keyword (would require files to be named, since most of my files now are just a bunch of numbers)
- Some hybrid mode for linux/mac that pastes local images and uses hosted gif links
- Non-destructive pasting (store clipboard contents)

# Reasons you should still buy Discord Nitro
- Support Discord!
- Inline emotes/gifs, keyboard shortcuts by name (ex: :emote_name:)
- React with emotes
- Other nitro benefits!

# Acknowledgements
- Thanks to [Luke Tong](https://github.com/luke-rt) for cross-platform GUI and clipboard testing
- Thanks to [Stephane Morel](https://github.com/SoAsEr) for Windows testing
- Thanks to [Brazil-0034](https://github.com/Brazil-0034) for adding support for non-destructive pasting

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

# License
[MIT License](https://github.com/dchen327/pingmote/blob/master/LICENSE.md)