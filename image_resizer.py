'''
A helper program to resize provided images into the same size
ex) 64x64 for Discord

* PIL is required

Author: David Chen
'''
import shutil
import os
import json
from PIL import Image
from pathlib import Path

asset_path = Path(__file__).parent / 'assets'
orig_path = asset_path / 'original'
resized_path = asset_path / 'resized'
new_size = (64, 64)


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


shutil.rmtree(resized_path)  # clear previous files
os.mkdir(resized_path)  # re-add resized directory
for img_path in orig_path.iterdir():
    # replace underscores with dashes since postimages uses dashes only
    save_path = resized_path / sanitize_name(img_path.name)
    if img_path.suffix == '.gif':  # don't try and resize gifs, just copy them directly
        shutil.copyfile(img_path, save_path)
    else:
        img = Image.open(img_path)
        img_resized = img.resize(new_size, Image.ANTIALIAS)
        img_resized.save(save_path)

clean_frequencies()
