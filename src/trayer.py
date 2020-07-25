from infi.systray import SysTrayIcon


def trayer(ops, mode, n):
    # try:

    def notify(a="0", title='Now Runnng at', tail=" mode"):
        n.send((title,
                a+tail))

    def noti(a):
        if mode[3] == 0:
            try:
                notify(a)
            except:
                pass

    def caller(a):
        def calling(sysTrayIcon, a=a):
            if 0 <= a < len(ops):
                mode[0] = a
                if mode[1] == -1:
                    mode[1] = 0
                if a < 2 and mode[2] == 1:
                    mode[2] = 0
                    noti("OCR only")
                else:
                    if mode[2] != 1:
                        noti(ops[a])
            elif a == len(ops):
                if mode[2] == 1:
                    noti("Translate only")
                    mode[2] = 0
                elif mode[2] == 0:
                    noti("OCR&Translate")
                    mode[2] = 1
            elif a == len(ops) + 1:
                mode[1] = -1
                noti("Listening Paused")
            elif a == len(ops) + 2:
                mode[3] = (mode[3] + 1) % 2
            elif a == -1:
                mode[1] = 1
                n.send(("Info", "Exiting"))

            print(mode[0], mode[1])

        return calling
    menu = ()
    trans = ()
    for i, ix in enumerate(ops):
        now = (ix, None, caller(i))
        if i <= 1:
            menu += (now,)
        else:
            trans += (now,)
    menu += (("Translate", None, trans,), ("OCR&Translate", None, caller(i + 1)),
             ("Pause", None, caller(i + 2)), ("Disable Notify", None, caller(i + 3)))

    hover_text = "PowerClipboard"

    tray = SysTrayIcon("main.ico", hover_text,
                       menu_options=menu, on_quit=caller(-1), default_menu_index=1)
    # noti("!!!!")
    tray.start()
    return tray
    # except:
    #     trayer(ops, mode)
