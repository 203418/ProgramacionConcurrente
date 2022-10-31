from threading import Thread, Condition
import time

class Producer(Thread):
    def __init__(self, condition, items):
        Thread.__init__(self)
        self.condition = condition
        self.items = items
        
    def produce(self):
        self.condition
        self. items
        
        self.condition.acquire()
        while len(self.items) == 10:
            self.condition.wait()
            print('Producer notify: items produced are: ', len(self.items))
            print('Producer notify: Stop the production')
        self.items.append(1)
        print('Producer Notify: total items produced are ', len(self.items))
        self.condition.notify()
        self.condition.release()
        
    def run(self):
        for i in range(20):
            time.sleep(5)
            self.produce()