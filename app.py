from src.notification import WindowsBalloonTip
from src.misc import clipper
from src.trayer import trayer
from multiprocessing import Process, freeze_support, Array, Pipe
from src.trans.MTvendor import vendors as mtVendors
from time import sleep as sleep
from src.go import go

try:
    ocr = 'OCR'
    latex = "LaTeX"
    ocrs = [ocr, latex]
    ops = ocrs + mtVendors

    if __name__ == '__main__':

        freeze_support()
        mode = Array('i', range(4))
        mode[0] = 2  # function mode
        mode[1] = 0  # listening mode
        mode[2] = 0  # OCR and translate mode
        mode[3] = 0  # No notification mode

        n1, n2 = Pipe()

        clipper = Process(target=clipper, args=(mode, n2))
        tray = trayer(ops, mode, n2)
        # observer = Process(target=clipboard_observer, args=(c1l, mode))
        clipper.start()

        def sub():
            nowNotice = None
            while True:
                if mode[1] == 1:
                    clipper.kill()
                    tray.shutdown()
                    if nowNotice != None:
                        nowNotice.kill()
                    break
                title, msg = n1.recv()
                if nowNotice != None:
                    nowNotice.kill()
                nowNotice = Process(target=WindowsBalloonTip,
                                    args=(msg, title)).start()
        go(sub)
except:
    pass
