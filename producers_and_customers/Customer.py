import threading
import time


class Customer(threading.Thread):
    def __init__(self, id, condition, queue):
        threading.Thread.__init__(self)
        self.id = id
        self.condition = condition
        self.queue = queue

    def run(self):
        while True:
            if self.condition.acquire():
                if self.queue.empty():
                    self.condition.wait()
                else:
                    item = self.queue.get()
                    print(f"Consumer {self.id} consumed {item}")
                    self.condition.notify()
                    self.condition.release()
                    time.sleep(3)