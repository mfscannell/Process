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
    rt = RemoteTerminal(4)

    def test_init(self):
        status = Status(self.rt.getAddress())
        self.assertTrue(isinstance(status, Status))
    
    def test_getTerminalAddress(self):
        status = Status(self.rt.getAddress())
        self.assertEqual(status.getTerminalAddress(), 4,
                         "Not assigning address correctly.")
    
    def test_setServiceRequest(self):
        status = Status(self.rt.getAddress())
        self.assertEqual(status.setServiceRequest(), False,
                         "Logic is incorrect.")
    
    def test_isServiceRequest(self):
        status = Status(self.rt.getAddress())
        status.setServiceRequest()
        self.assertEqual(status.isServiceRequested(), True,
                         "Logic is incorrect or setting service request is incorrect.")
    
    def test_setMessageError(self):
        status = Status(self.rt.getAddress())
        self.assertEqual(status.setMessageError(), False, 
                         "Variable assigned incorrectly. Check logic.")
    
    def test_isMessageError(self):
        status = Status(self.rt.getAddress())
        status.setMessageError()
        self.assertEqual(status.isMessageError(), True, 
                         "Variable assigned incorrectly. Check logic.")
    
    def test_setBusy(self):
        status = Status(self.rt.getAddress())
        self.assertEqual(status.setBusy(), False, 
                         "Variable assigned incorrectly. Check logic.")
    
    def test_isBusy(self):
        status = Status(self.rt.getAddress())
        status.setBusy()
        self.assertTrue(status.isBusy(), 
                        "Variable assigned incorrectly. Check logic.")
        
