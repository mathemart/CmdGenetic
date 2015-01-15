import sys
# To change this license heade , choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="michael"
__date__ ="$Dec 10, 2014 7:47:26 PM$"

import os
import time
import random 


class Letter:
    
    x, y, char, genome = 0, 0, '', {'speed' : 0, 'health' : 0, 'decay' : 0 }
    
    def __init__(self):
        self.x = random.randint(1,75)
        self.y = random.randint(1, 30)
        self.char = chr(random.randint(97, 123))
        self.speed = random.random() + 1
        self.health = random.randint(1, 5)
        self.decay = random.randint(0, 1)
        
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
        while True:
            self.update_display()
            self.random_walk()
            time.sleep(.1 * self.genome['speed'])
            os.system('clear')
  
 
letter = Letter()
print letter.genome['speed']
letter.run()