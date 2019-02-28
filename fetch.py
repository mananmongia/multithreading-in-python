import threading
from time import sleep

class Manan(threading.Thread):

    def __init__(self, name):
        super(Manan, self).__init__()
        self._stop_event = threading.Event()
        self.name = name

    def kill(self):
        self._stop_event.set()

    def run(self):
         while not self._stop_event.is_set():
            print(self.name)
            sleep(1)


class Mongia(threading.Thread):

    def __init__(self,name):
        super(Mongia, self).__init__()
        self._stop_event = threading.Event()
        self.name = name

    def kill(self):
        self._stop_event.set()

    def run(self):
         while not self._stop_event.is_set():
            print(self.name)
            sleep(1)


t1 = Manan('Manan')
t2 = Mongia('Mongia')

t1.start()
sleep(0.2)
t2.start()

sleep(3)
t1.kill()
t1.join()
sleep(3)
t2.kill()
