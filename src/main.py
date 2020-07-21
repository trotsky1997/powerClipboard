
from src.misc import trayer, clipper
from multiprocessing import Process, freeze_support, Array, Pipe
from src.trans.MTvendor import vendors as mtVendors
from time import sleep as sleep

ocr = 'OCR'
latex = "LaTeX"
ocrs = [ocr, latex]
ops = ocrs + mtVendors
menu_def = ['BLANK', ocrs+["Translate", mtVendors]+["---", "Mute", "Exit"]]

if __name__ == '__main__':
    freeze_support()
    mode = Array('i', range(2))
    mode[0] = 3
    mode[1] = 0

    c1 = Pipe()

    p2 = Process(target=clipper, args=(mode,))
    p1 = Process(target=trayer, args=(ops, mode, menu_def))
    p1.start()
    p2.start()
