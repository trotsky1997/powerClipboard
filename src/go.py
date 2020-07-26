import threading
import time


class gos(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def go(func, args=()):
    g = gos(func, args)
    g.run()
    return g


def goretry(func, args=(), max_times=6):
    def work():
        n = 0
        while True:
            try:
                go(func, args)
                break
            except:
                n += 1
                time.sleep(0.1 * n)
                if n >= max_times:
                    break
    go(work)
