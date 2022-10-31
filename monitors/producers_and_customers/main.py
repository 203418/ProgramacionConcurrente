from threading import Condition
from Producer import Producer
from Customer import Consumer

items = []
condition = Condition()

if __name__ == '__main__':
    producer = Producer(condition, items)
    consumer = Consumer(condition, items)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()