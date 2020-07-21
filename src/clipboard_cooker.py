import os
from PIL import ImageGrab


def cook_clipboard_pic(vistor):
    im = ImageGrab.grabclipboard()
    im.save('./temp.png', 'PNG')
    with open(r'./temp.png', "rb") as f:
        ans = vistor(f.read())
    os.remove('./temp.png')
    return ans
