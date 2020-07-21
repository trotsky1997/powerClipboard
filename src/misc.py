import time
import pyperclip
from src.trans.MTvendor import vendors as mtVendors
from src.pic2text import pic2text
from src.pic2latex import pic2latex
from src.trans.MTvendor import mt
import PySimpleGUIWx as sg
import time
from PIL import ImageGrab

# from clipboard_cooker import cook_clipboard_pic


def vendor2engine(vendor):
    def trs(val="", from_language='en', to_language='zh'):
        if val == "":
            return ""
        return mt(val, vendor)
    return trs


# def clipboard_observer(c1=None, mode=None):  # c1l
#     history = [None, None]
#     while True:
#         time.sleep(0.3)
#         if mode[1] == -1:
#             continue
#         if mode[1] == 1:
#             c1.send("DIE!")
#             break
#         now = pyperclip.paste()
#         c1.send(now)


def trayer(ops, mode, menu_def):
    ops_dict = {ix: i for i, ix in enumerate(ops)}
    tray = sg.SystemTray(menu=menu_def)
    tray.show_message("Notice", "Initiated Successfully!")
    old = "-1"
    while True:
        menu_item = tray.Read()
        if menu_item in ['__MESSAGE_CLICKED__', '__DOUBLE_CLICKED__']:
            continue
        if menu_item != old:
            if menu_item != "Mute":
                mode[1] = 0
            tray.show_message("Mode running at", menu_item)
            old = menu_item
        if menu_item == "Exit":
            mode[1] = 1
            break
        if menu_item == "Mute":
            mode[1] = -1
            continue
        if mode[1] == 0:
            mode[0] = ops_dict[menu_item]
            print(menu_item)


def clipper(mode,):  # c1r

    action = tuple([pic2text, pic2latex]+[vendor2engine(i) for i in mtVendors])
    old = pyperclip.paste()
    while True:
        time.sleep(0.4)
        if mode[1] == -1:
            old = pyperclip.paste()
        if mode[1] == 1:
            break
        if mode[1] == 0:
            val = pyperclip.paste()
            if old == val:
                continue
            ans = action[mode[0]](val)
            pyperclip.copy(ans)
            old = pyperclip.paste()
