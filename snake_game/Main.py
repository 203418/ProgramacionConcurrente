import random
from tkinter import messagebox
import tkinter
import pygame
from Cube import cube
from threading import Thread

from Snake import snake

class Main(Thread):
    def __init__(self):
        Thread.__init__(self)
        pygame.init()

    def redrawWindow(self, surface):
        global rows, width, s, snack
        surface.fill((0,0,0))
        s.draw(surface)
        snack.draw(surface)
        # drawGrid(width,rows, surface)  
        pygame.display.update()
    
    
    def randomSnack(self, rows, item):
    
        positions = item.body
    
        while True:
            x = random.randrange(rows)
            y = random.randrange(rows)
            if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                continue
            else:
                break
    
        return (x,y)
    
    
    def message_box(self, subject, content):
        root = tkinter.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass
    
    
    def run(self):
            self.mainMenu()
        
    def mainMenu(self):
        count = 3;
        global width, rows, s, snack
        finalScore = 0
        width = 500
        rows = 20
        win = pygame.display.set_mode((width, width))
        s = snake((255,0,0), (10,10))
        snack = cube(self.randomSnack(rows, s), color=(0,255,0))
        flag = True

    
        clock = pygame.time.Clock()
        
        
        while flag:
            pygame.time.delay(50)
            clock.tick(10)
            s.move()
            if s.body[0].pos == snack.pos:
                s.addCube()
                snack = cube(self.randomSnack(rows, s), color=(0,255,0))
        
            redFlag = False
        
            for x in range(len(s.body)):
                if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                    redFlag = True
                    pass
                
            if redFlag == True:
                finalScore += len(s.body)
                print('Score: ', finalScore)
                self.message_box('Perdiste', 'Perdiste, te quedan: ' + str(count-1) + " vidas")
                s.reset((10,10))
                count-=1
                
            if(count == 0):
                self.message_box('Tu Puntaje es: ', str(finalScore))
                break
                
            self.redrawWindow(win)
    
        pass

if __name__ == '__main__':
    main = Main()
    main.start()