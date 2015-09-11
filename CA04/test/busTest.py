'''
Created on Mar 27, 2014

@author: chanpod
'''
import unittest
from CA04.prod.bus import Bus
from CA04.prod.status import Status
from CA04.prod.data import Data
from CA04.prod.command import Command

class BusTest(unittest.TestCase):

    def test_bus(self):
        bus = Bus()
        self.assertTrue(isinstance(bus, Bus), "bus is not an instance of Bus")
        
    def test_writeBus(self):
        #Happy Case
        bus = Bus()
        status = Status(5)
        self.assertEquals(bus.writeBus(status), 1, 
                          "Not returning the correct number of items in bus.")
        
        
        #Sad Case
        self.assertRaises(ValueError, bus.writeBus, 'a')       
        
        
    
    def test_readBus(self):
        #Happy Case
        bus = Bus()
        status = Status(5)
        bus.writeBus(status)
        word = bus.readBus()
        
        self.assertTrue(isinstance(word, (Status, Command, Data)), 
                        "Word is not an instance of Bus, Command, or Data.")
        
        #Sad Case
        self.assertRaises(ValueError, bus.readBus)


