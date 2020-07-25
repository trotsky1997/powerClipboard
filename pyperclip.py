import win32clipboard as wc
import win32con
import time


def paste():
    # try:
    #     wc.CloseClipboard()
    # except:
    #     pass
    while True:
        try:
            wc.OpenClipboard()
            break
        except:
            time.sleep(0.1)
    # # 尝试将剪切板内容读取为Unicode文本
    try:
        txt = wc.GetClipboardData(win32con.CF_UNICODETEXT)  # 用unicode读
    except:
        txt = "pic"
    # 关闭剪切板
    wc.CloseClipboard()
    return txt
    # except:
    #     try:
    #         wc.CloseClipboard()
    #     except:
    #         pass


def copy(txt):
    txt = str(txt)
    # try:
    #     wc.CloseClipboard()
    # except:
    #     pass
    while True:
        try:
            wc.OpenClipboard()
            break
        except:
            time.sleep(0.1)
    wc.EmptyClipboard()
    # 尝试将剪切板内容读取为Unicode文本
    # print(txt)
    wc.SetClipboardData(win32con.CF_TEXT, txt.encode('gbk'))  # 转为gbk再发给粘贴板
    # 关闭剪切板
    wc.CloseClipboard()

    # except:
    #     try:
    #         wc.CloseClipboard()
    #     except:
    #         pass


# print(paste())
# copy(time.time())
# print(paste())
