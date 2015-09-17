'''
Created on Mar 30, 2014

@author: 
'''
import unittest
from CA04.prod.bus import Bus
from CA04.prod.status import Status
from CA04.prod.data import Data
from CA04.prod.command import Command
from CA04.prod.remoteterminal import RemoteTerminal

class Test(unittest.TestCase):
    
    

    def test_init(self):
        #Happy Case
        rt = RemoteTerminal(4)
        self.assertTrue(isinstance(rt, RemoteTerminal),
                        "Object is not of instance RemoteTerminal")
        
        self.assertRaises(ValueError, RemoteTerminal, 'a')
    
    def test_getAddress(self):
        rt = RemoteTerminal(4)
        self.assertEqual(rt.getAddress(), 4,
                         "Not Assigning address correctly.")
    
    def test_readBus(self):
        #Happy Case
        rt = RemoteTerminal(4)
        data = Data(1)
        bus = Bus()
        bus.writeBus(data)
        bus2 = rt.readBus(bus)
        self.assertTrue(isinstance(bus2, Bus), 
                        "Not assigning")
        
        #Sad Case
        self.assertRaises(ValueError, rt.readBus, 'a')
        
        


