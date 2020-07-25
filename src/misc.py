import time
import pyperclip
from src.trans.MTvendor import vendors as mtVendors
from src.pic2text import pic2text
from src.pic2latex import pic2latex
from src.trans.MTvendor import mt
import time
from src.trayer import trayer
# from plyer import notification


# from clipboard_cooker import cook_clipboard_pic


def vendor2engine(vendor):
    def trs(val="", from_language='en', to_language='zh'):
        if val == "":
            return ""
        return mt(val, vendor)
    return trs


def clipper(mode, n):  # c1r
    # try:

    def noti(a="0", title='Now Runnng at', tail=" mode"):
        n.send((title,
                a+tail,))

    action = tuple([pic2text, pic2latex]+[vendor2engine(i)
                                          for i in mtVendors])
    old = pyperclip.paste()
    try:
        pyperclip.copy("test")
        val = pyperclip.paste()
        ans = action[2](val)
        pyperclip.copy(ans)
        print(ans)
        noti("Initlized Successfully!", title="Info", tail="")
        pyperclip.copy(old)
    except:
        pyperclip.copy(old)
        noti("Initlization Failed!", title="Info", tail="")
    # dev = 1
    while True:
        if mode[1] == -1:
            old = pyperclip.paste()
        if mode[1] == 1:
            break
        if mode[1] == 0:
            val = pyperclip.paste()
            if old == val:
                continue
            if mode[2] == 0:
                if not(val != "pic" and mode[0] < 2):
                    ans = action[mode[0]](val)
                else:
                    ans = action[2](val)
            elif mode[2] == 1:
                if val == "pic":
                    dans = action[0](val)
                else:
                    dans = val
                if mode[0] < 2:
                    eng = 2
                else:
                    eng = mode[0]
                ans = action[eng](dans)
            pyperclip.copy(ans)
            print(ans)
            old = pyperclip.paste()
            if old == "pic":
                old = time.time()
# except:
    #     pass
