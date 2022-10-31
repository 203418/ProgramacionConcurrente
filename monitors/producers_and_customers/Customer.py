from threading import Thread, Condition
import time


class Consumer(Thread):
    def __init__(self, condition, items):
        Thread.__init__(self)
        self.condition = condition
        self.items = items
        
    def consume(self):
        self.condition
        self.items
        
        self.condition.acquire() == 0
        while len(self.items) == 0:
            self.condition.wait()
            print('Consumer notify: no item consume')
        self.items.pop()
        print('Consumer notify: consumed 1 item')
        print('Consumer notify: items to consumer are ', len(self.items))
        self.condition.notify()
        self.condition.release()
        
    def run(self):
        for i in range(20):
            time.sleep(10)
            self.consume()