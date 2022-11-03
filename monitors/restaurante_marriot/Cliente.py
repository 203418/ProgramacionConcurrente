from random import randint
from time import sleep
from threading import Condition, Thread

class Client(Thread):
    def __init__(self, name, recepcionista, mesero, tables, order):
        Thread.__init__(self)
        self.name = name
        self.sentado = False
        self.recepcionista = recepcionista
        self.mesero = mesero
        self.tables = tables
        self.comer = False
        self.order = order
        self.condition = Condition()
        
        
    def requestServiceToRecepcionist(self):
        self.sentado = self.recepcionista.attend(self.name, 0)
        
    def receiveFood(self):
        print(f"-Mesero: llevando la comida al cliente {self.name}")
        self.comer = self.mesero.llevarComida
    
    def eating(self):
        print(f"--Yo {self.name} estoy comiendo--")
        sleep(randint(1, 10))
        print(f"--Yo {self.name} he terminado de comer y me voy--")
        self.tables.remove(self.name)
            
    def run(self):
        print(f"--Yo {self.name} he llegado al restaurant, atiendeme! --")
        self.requestServiceToRecepcionist()
        while self.sentado == False:
                self.sentado = self.recepcionista.atenderCola(self.name)
        if (self.sentado == True):
            print(f"--Yo {self.name} sentado y esperando a un mesero --")
            self.mesero.attend(self.name)
            while(self.comer == False):
                if self.order[1] == True:
                    self.receiveFood()
                self.condition.acquire()
                if (self.comer == True):
                    self.condition.notify()
                    self.condition.release()
            if self.comer:
                self.eating()