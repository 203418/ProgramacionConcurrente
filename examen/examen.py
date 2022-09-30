import threading
import time

mutex = threading.Lock()

chopsticks = [threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock(),threading.Lock(), threading.Lock(), threading.Lock(), threading.Lock()]


def liberar_chopstick(id):
    if id == len(chopsticks)-1:
        if "locked _thread.lock" in str(chopsticks[0]):  
            chopsticks[0].release()                       
    else:
        if "locked _thread.lock" in str(chopsticks[id+1]):  
            chopsticks[id+1].release()


def obtener_chopstick(id):
    result = 0
    if "unlocked _thread.lock" in str(chopsticks[id]):  
        chopsticks[id].acquire()
        if id == len(chopsticks)-1:
            chopsticks[0].release()
            if "unlocked _thread.lock" in str(chopsticks[0]): 
                chopsticks[0].acquire()                       
                result = 1
        else:
            if "unlocked _thread.lock" in str(chopsticks[id+1]):
                chopsticks[id+1].acquire()
                result = 1
    return result


def crito(id):
    ciclo = True
    while ciclo:
        eat = obtener_chopstick(id)
        time.sleep(0.5)
        if eat == 1: 
            print(f"\nPersona {str(id + 1)} esta comiendo")
            print(f"\nPersona {id+1} esta usando los palillos {id+1} y {(((id+1)%8)+1)}")
            time.sleep(5)
            print(f"\nPersona {str(id + 1)} dejo de comer y libero palillo  {(((id+1)%8)+1)}")
            liberar_chopstick(id)
            ciclo = False
        
        
                
class Persona(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

    def run(self):
        mutex.acquire(blocking = True, timeout = 50)
        crito(self.id)
        mutex.release()
        
        
if __name__=="__main__": 
    for i in range(8):
        p = Persona(i)
        p.start()
    