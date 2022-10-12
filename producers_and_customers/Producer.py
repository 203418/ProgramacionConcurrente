from asyncio import Condition
import random
import threading
import time


class Producer(threading.Thread):
    def __init__(self, id, condition, queue):
        threading.Thread.__init__(self)
        self.id = id
        self.condition = condition
        self.queue = queue

    def run(self):
        while True:
            if self.condition.acquire():
                if self.queue.full():
                    self.condition.wait()
                else:
                    item = random.randint(0, 100)
                    self.queue.put(item)
                    print(f"Producer {self.id} produced {item}")
                    self.condition.notify()
                    self.condition.release()
                    time.sleep(3)