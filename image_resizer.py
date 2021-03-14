'''
A helper program to resize provided images into the same size
ex) 64x64 for Discord

* PIL is required

Author: David Chen
'''
import shutil
import os
import json
import subprocess
from config import RESIZE_GIFS
from PIL import Image
from pathlib import Path

asset_path = Path(__file__).parent / 'assets'
orig_path, resized_path = asset_path / 'original', asset_path / 'resized'
new_size = (64, 64)


def resize_gif(gif_path, save_path):
    """ Resize a gif using the command line utility `gifsicle` """
    cmd = 'gifsicle --resize 64x64 --colors 256 -i {} > {}'.format(
        str(gif_path), str(save_path))
    subprocess.run(cmd, shell=True)  # run as string with > (shell = True)


def sanitize_name(name):
    """ Remove special and uppercase characters for consistent file upload name preservation """
    replace_chars = ['_', '-', ' ']
    for c in replace_chars:
        name = name.replace(c, '')  # remove these chars
    return name.lower()


def load_frequencies():
    """ Load the frequencies dictionary from frequencies.json """
    with open(asset_path / 'frequencies.json', 'r') as f:
        return json.load(f)


def write_frequencies(frequencies):
    """ Write new frequencies to frequencies.json """
    with open(asset_path / 'frequencies.json', 'w') as f:
        json.dump(frequencies, f, indent=4)


def clean_frequencies():
    """ Clean frequencies.json on file changes """
    frequencies = load_frequencies()
    filenames = {img_path.name for img_path in resized_path.iterdir()}
    for file in list(frequencies):
        if file not in filenames:
            del frequencies[file]  # remove key, file not present
    write_frequencies(frequencies)


def update_resized_files():
    """ Resize new files and remove deleted files """
    orig_filenames = {sanitize_name(img_path.name)
                      for img_path in orig_path.iterdir()}
    resized_filenames = {img_path.name for img_path in resized_path.iterdir()}
    for img_path in orig_path.iterdir():  # check for new images
        if img_path.suffix not in ['.png', '.gif', '.jpg', '.jpeg']:
            # delete other files (e.g. weird Zone.Identifiers)
            os.remove(img_path)
            continue
        if sanitize_name(img_path.name) not in resized_filenames:  # new image
            # clean up file name for upload
            save_path = resized_path / sanitize_name(img_path.name)
            if img_path.suffix == '.gif':  # gifs
                if RESIZE_GIFS:  # resize with gifsicle
                    resize_gif(img_path, save_path)
                else:  # copy gif to resized (assume already resized)
                    shutil.copyfile(img_path, save_path)
            else:
                img = Image.open(img_path)
                img_resized = img.resize(new_size, Image.ANTIALIAS)
                img_resized.save(save_path)

    for img_path in resized_path.iterdir():  # remove deleted images
        if img_path.name not in orig_filenames:  # original image deleted
            os.remove(img_path)


update_resized_files()
clean_frequencies()
