# pingmote
A cross-platform Python global emote picker to quickly insert custom images/gifs 

Motivation: *Poor Man's Discord Nitro*


# Demo
![pingmote demo](https://user-images.githubusercontent.com/37674516/113481499-eafe2a80-9467-11eb-886c-3bd7981f1add.gif)


# How It Works
- Since Discord autoembeds images, we can paste in links to custom emotes
- The emote picker is written in Python with [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI), with global hotkeys for activation (using [keyboard](https://github.com/boppreh/keyboard))

# Getting Started
- Clone this repo: `git clone https://github.com/dchen327/pingmote.git` or download as a zip and extract
- Change into the pingmote directory (make sure you can see `pingmote.py`)
- Run `pip install -r requirements.txt` to install dependencies (`pip3` if needed)

# Usage
- Running `python3 pingmote.py` (Mac and Linux: `sudo python3 pingmote.py`) starts the script, and when you hit the hotkey at the top of `config.py` (default `ctrl+q`), the emote picker will show up, allowing you to click an emote to insert
- Hit the hotkey again to toggle the GUI, and drag the GUI somewhere convenient

# Configs
- Check `config.py` for configs

# Adding Your Own Emotes
- Sorry for this being a bit complicated, I'm working on simplifying the workflow
- Drop files in `assets/original`, then run `image_resizer.py` which will resize all the images (ignoring gifs) and drop them in `assets/resized`
- Gif resizing (disabled by default) requires `gifsicle`, but a website like [ezgif](https://ezgif.com/resize) also works
- Resize gifs to 64x64 and drop them in `assets/original` (they'll be ignored when the resizer is run)
- Upload files from `assets/resized` to an image hoster (I like [postimages](https://postimages.org/)). Copy the direct image links (ending in file extension) and paste in `links.txt`
- A simpler alternative using GitHub: fork this repo and push your images, then drop your forked repo's URL in config.py (GITHUB_URL). This method doesn't require alternate hosting or `links.txt`
- Note: Imgur doesn't work currently, since Imgur links don't contain the original filename
- Some emote sources (right click > save image): [discordmojis.com](https://discordmojis.com/), [emoji.gg](https://emoji.gg/), [discord.st](https://discord.st/emojis/)

# Notes
- Since this program relies on autoembedding, we can't use inline emotes or reacts
- Pretty much only Discord works (Facebook Messenger and Slack make embeds ugly)
- On Windows, renaming the file extension to `pingmote.pyw` allows for running the script in the background, and then it can be dropped into shell:startup
- Windows should work out of the box, Mac and Linux may require jumping through some hoops
- The Apple M1 chip is currently unsupported (bus error)
- On Linux, if you get the error `KeyError: 'XDG_SESSION_TYPE'`, set the environment variable by running
  > `sudo XDG_SESSION_TYPE=x11 python3 pingmote.py`

# TODOs
- Better ordering of emotes (categorization, etc.)
- Simplify install process
- Simplify the process for adding new emotes
- Emote deletion in GUI
- Ensure gif thumbnail isn't blank (not fully sure how to do this)
- Search emotes by keyword (would require files to be named, since most of my files now are just a bunch of numbers)

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
- Shifted configs to separate file

# License
[MIT License](https://github.com/dchen327/pingmote/blob/master/LICENSE.md)