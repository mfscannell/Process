'''
Created on Mar 27, 2014
LOC: 18
@author: 
'''

from command import Command
from data import Data
from status import Status

class Bus(object):
    FIRSTINDEX = 0
    bus = []    
    
    def writeBus(self, wordIn = None):        
        try:
            if(wordIn == None):
                raise ValueError
            else:
                if(isinstance(wordIn, (Command, Data, Status))):
                    self.bus.append(wordIn)
                    return len(self.bus)
                else:
                    raise ValueError
        except ValueError:
            print("Bus.writeBus:  word invalid or ommited.")
            raise ValueError
    
    def readBus(self):
      
        try:
            if(len(self.bus) != 0):                
                word = self.bus.pop()
            else:
                raise ValueError
        except ValueError:
            print("Bus is empty. Nothing to read.")
            raise ValueError   
        return word
