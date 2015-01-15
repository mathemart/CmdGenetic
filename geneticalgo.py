# To change this license heade , choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="michael"
__date__ ="$Dec 10, 2014 7:47:26 PM$"

import os
import time
import random 


class Letter:
    
    x, y, char, genome = 0, 0, '', {'speed' : 0.0, 'health' : 0, 'decay' : 0 }
    
    def __init__(self):
        self.x = random.randint(1,75)
        self.y = random.randint(1, 30)
        self.char = chr(random.randint(97, 122))
        self.genome['speed'] = 1 + random.random()
        self.genome['health'] = random.randint(1, 5)
        self.genome['decay'] = random.randint(0, 1)  
         
        
    def update_display(self):
        y_disp = self.y * '\n'
        x_disp = self.x * ' '
        y_remainder = (30 - self.y) * '\n'
        letter = y_disp + x_disp + self.char + y_remainder
        print letter
        
    def random_walk(self):
        x_mov = random.choice([-1, 0, 1])
        y_mov = random.choice([-1, 0, 1])
        self.x += x_mov 
        self.y += y_mov
    
    def run(self):
        for p in range(4):
            rate = .2 * self.genome['speed']
            self.update_display()
            self.random_walk()
            time.sleep(rate)
            os.system('clear')
                   
        

class Poison(Letter):
    
    speed = 0
    
    def __init__(self):
        Letter.__init__(self)
        
    
    def collide(self):
        star = '*'
        y_disp = self.y * '\n'
        x_disp = self.x * ' '
        y_remainder = (30 - self.y) * '\n'
        stellar = y_disp + x_disp + star + y_remainder
        print Letter.y, self.y, Letter.x, self.x
        print stellar
        
    def random_walk(self):
        return Letter.random_walk(self)
    
        

letter = Letter()
poison = Poison()
#print letter.genome['speed']
#letter.run()
