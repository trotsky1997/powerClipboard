import win32clipboard as wc
import win32con
import time
from src.go import goretry, go

max_times = 4


def reg(txt):
    txt = str(txt).strip()
    # 字符串按行分割
    txt = txt.splitlines()
    n = len(txt)
    # 用空格拼接每行
    txt = ' '.join(txt)
    # 将所有长度大于1的空白符转为1个空格
    txt = ' '.join(txt.split())
    return txt


def paste(re=0):
    # try:
    #     wc.CloseClipboard()
    # except:
    #     pass
    txt = ""

    def work():
        nonlocal txt
        wc.OpenClipboard()
        # # 尝试将剪切板内容读取为Unicode文本
        try:
            txt = wc.GetClipboardData(win32con.CF_UNICODETEXT)  # 用unicode读
            # go(reg)
        except:
            raise("cannot do it")
        wc.CloseClipboard()

    goretry(work)

    # #print(txt)
    if re == 1:
        txt = reg(txt)
    return txt
    # except:
    #     try:
    #         wc.CloseClipboard()
    #     except:
    #         pass


def copy(txt, re=0):
    txt = str(txt)

    if re == 1:
        txt = reg(txt)

    def work():
        nonlocal txt
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_TEXT, txt.encode('gbk'))  # 转为gbk再发给粘贴板
        wc.CloseClipboard()

    # go(reg)
    goretry(work)

    # except:
    #     try:
    #         wc.CloseClipboard()
    #     except:
    #         pass


# #print(paste())
# copy(time.time())
# #print(paste())
