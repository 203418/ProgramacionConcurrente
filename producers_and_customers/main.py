import queue
import threading

from Producer import Producer
from Customer import Customer

# Creamos la cola
queue = queue.Queue(maxsize=10)
condition = threading.Condition()

PRODUCERS = 5 # Constante productores
CUSTOMERS = 10 #Constante consumidores

if __name__ == '__main__':
    producers = []
    custormers = []
    for i in range(PRODUCERS):
        producers.append(Producer(i, condition, queue))
    for i in range(CUSTOMERS):
        custormers.append(Customer(i, condition, queue))
    
    for p in producers:
        p.start()
    for c in custormers:
        c.start()