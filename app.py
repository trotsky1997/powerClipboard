dev = 0
try:
    from src.main import *

    if __name__ == '__main__':
        freeze_support()
        mode = Array('i', range(2))
        mode[0] = 2
        mode[1] = 0

        # c1l, c1r = Pipe()
        clipper = Process(target=clipper, args=(mode,))
        trayyer = Process(target=trayer, args=(ops, mode, menu_def))
        # observer = Process(target=clipboard_observer, args=(c1l, mode))
        clipper.start()
        trayyer.start()
        sleep(1)
        while True:
            if mode[1] == 1:
                clipper.stop()
                trayyer.stop()
                break
            else:
                if clipper.is_alive != True:
                    clipper.start()
                if trayyer.is_alive != True:
                    trayyer.start()
        # observer.start()
except Exception as e:
    if dev == 1:
        print(e)
