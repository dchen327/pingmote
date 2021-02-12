'''
A helper program to resize provided images into the same size
ex) 64x64 for Discord

* PIL is required

Author: David Chen
'''
import shutil
import os
from PIL import Image
from pathlib import Path

orig_path = Path('./assets/original')
resized_path = Path('./assets/resized')
new_size = (64, 64)


def sanitize_name(name):
    """ Remove special and uppercase characters for consistent file upload name preservation """
    replace_chars = ['_', '-', ' ']
    for c in replace_chars:
        name = name.replace(c, '')  # remove these chars
    return name.lower()


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
