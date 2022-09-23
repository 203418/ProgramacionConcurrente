import threading
from time import sleep

mutex = threading.Lock()

def crito(self, id):
    global x;
    x = x + id
    print("Hilo=>"+str(id) + "=>" + str(x))

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire()
        sleep(3-self.id)
        print("valor "+str(self.id))
        mutex.release()


hilos_mutex = [Hilo(1), Hilo(2), Hilo(3)]

x=1;

for h in hilos_mutex:
    h.start()