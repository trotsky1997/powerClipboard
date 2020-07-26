from src.notification import WindowsBalloonTip
from src.misc import clipper
from src.trayer import trayer
from multiprocessing import Process, freeze_support, Array
from src.trans.MTvendor import vendors as mtVendors
from time import sleep as sleep
import win32clipboard
ocr = 'OCR'
latex = "LaTeX"
ocrs = [ocr, latex]
ops = ocrs + mtVendors


dev = 1

if __name__ == '__main__':

    freeze_support()
    mode = Array('i', range(4))
    mode[0] = 2  # function mode
    mode[1] = 0  # listening mode
    mode[2] = 0  # OCR and translate mode
    mode[3] = 0  # No notification mode

    clipper = Process(target=clipper, args=(mode,))
    tray = trayer(ops, mode)
    # observer = Process(target=clipboard_observer, args=(c1l, mode))
    clipper.start()

    while True:
        if mode[1] == 1:
            clipper.kill()
            tray.shutdown()
            break
        # print("!!!!1")
    #     else:
    #         if clipper.is_alive != True:
    #             clipper.start()
    #         if trayyer.is_alive != True:
    #             trayyer.start()
    #     sleep(0.1)
    # try:
    #     win32clipboard.CloseClipboard()
    # except:
    #     pass
    # observer.start()
