# pingmote
A cross-platform Python global emote picker to quickly insert custom images/gifs 

Motivation: *Poor Man's Discord Nitro*


# Demo
![pingmote demo](https://user-images.githubusercontent.com/37674516/107857226-1e72f000-6dfb-11eb-8a9a-e938368b65bc.gif)

# How It Works
- Since Discord autoembeds images, we can paste in links to custom emotes
- The emote picker GUI is written in Python, with global hotkeys for activation

# Getting Started
- Clone this repo: `git clone https://github.com/dchen327/pingmote.git` or download as a zip and extract
- Change into the pingmote directory (make sure you can see `pingmote.py`)
- Run `pip install -r requirements.txt` to install dependencies (`pip3` if needed)

# Usage
- Running `python pingmote.py` (or `python3 pingmote.py`) will start the script, and when you hit the hotkey at the top of `config.py` (default `ctrl+q`, `command+3` for Mac), the emote picker will show up, allowing you to click an emote to insert
- Hit the hotkey again to toggle the GUI, and drag the GUI somewhere convenient

# Configs
- Check `config.py` for configs

# Adding Your Own Emotes
- Sorry for this being a bit complicated, I'm working on simplifying the workflow
- Drop image files in the `original` folder, then run `image_resizer.py` which will resize all the images (ignoring gifs) and drop them in the `resized` folder
- Unfortunately, `image_resizer.py` is currently unable to resize gifs, so a website like [this](https://www.iloveimg.com/resize-image/resize-gif) is useful. Download and extract the resized gifs (64x64) to `assets/original`, then run `image_resizer.py`
- Upload files from `assets/resized` to an image hoster (I like [postimages](https://postimages.org/)). Copy the direct image links (ending in file extension) and paste in `links.txt`
- Note: Imgur doesn't work currently, since Imgur links don't contain the original filename
- Some emote sources (right click save image): [discordmojis.com](https://discordmojis.com/), [emoji.gg](https://emoji.gg/), [discord.st](https://discord.st/emojis/)

# Notes
- Since this program pastes image/gif URLs as emotes, we can't use inline emotes or reacts
- Pretty much only Discord works (Facebook Messenger and Slack don't autoembed)

# Mac
- The script must be run as root: `sudo python pingmote.py`
- It seems only keyboard shortcuts with `command` like `command+e` are picked up, since scan codes are jumbled

# TODOs
- Better ordering of emotes (categorization, etc.)
- Simplify the process for adding new emotes
- Gif resizing? (idk PIL isn't very good for this)
- Ensure gif thumbnail isn't blank (not fully sure how to do this)
- Search emotes by keyword (would require files to be named, since most of my files now are just a bunch of numbers)
- Emote deletion

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
- Switched to `keyboard` from `pynput` to fix hotkey blocking behavior (after 3 weeks of zero progress)
- Cleaned up `image_resizer.py`

# License
[MIT License](https://github.com/dchen327/pingmote/blob/master/LICENSE.md)