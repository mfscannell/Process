'''
Created on Mar 30, 2014

@author: chanpod
'''
import unittest
from CA04.prod.bus import Bus
from CA04.prod.status import Status
from CA04.prod.data import Data
from CA04.prod.command import Command
from CA04.prod.remoteterminal import RemoteTerminal

class CommandTest(unittest.TestCase):
    rt = RemoteTerminal(4)

    def test_init(self):
        #Happy Case
        com = Command(self.rt.getAddress())
        self.assertTrue(isinstance(com, Command), 
                        "Command is being initialized correctly.")
        
        #Sad Case
        self.assertRaises(ValueError, Command, -1)
    
    def test_getTerminalAddress(self):
        com = Command(self.rt.getAddress())
        self.assertEqual(com.getTerminal(), 4, 
                         "address is incorrect. Should be 4.")
    
    def test_setToCommandWord(self):
        #Happy Case
        com = Command(self.rt.getAddress())
        self.assertEqual(com.setToCommandWord(), False, 
                         "Should be false. Initializing incorrectly"
                         " or not properly altering variable.")
        com.setToModeCommand(4)
        self.assertEqual(com.setToCommandWord(), True,
                         "Should be true. Incorrect logic or assignment not being made.")
        
        #Sad Case
        self.assertRaises(ValueError, com.setToModeCommand, 3)
    
    def test_setToModeCommand(self):
        #Happy Case
        com = Command(self.rt.getAddress())
        self.assertEqual(com.setToModeCommand(2), 2,
                         "Not returning passed integer correctly.")
        
        #Sad Case
        self.assertRaises(ValueError, com.setSubAddress,  'a')
        self.assertRaises(ValueError, com.setSubAddress, 4)
        self.assertRaises(ValueError, com.getSubAddress)
        self.assertRaises(ValueError, com.setWordCount, -2)
        self.assertRaises(ValueError, com.setWordCount, 2)
        self.assertRaises(ValueError, com.getWordCount)
        
        com.setToCommandWord()
        self.assertRaises(ValueError, com.setWordCount, -2)
        self.assertRaises(ValueError, com.setSubAddress,  'a')
        
    def test_getModeCode(self):
        com = Command(self.rt.getAddress())
        com.setToModeCommand(4)
        self.assertEqual(com.getModeCode(), 4,
                         "Not assigning mode code correctly.")
    
    def test_isModeCode(self):
        com = Command(self.rt.getAddress())
        com.setToModeCommand(4)
        self.assertTrue(com.isModeCommand(), 
                        "Mode command not being assigned correctly or logic is wrong.")
    
    def test_setSubAddress(self):
        com = Command(self.rt.getAddress())
        com.setToCommandWord()
        self.assertEqual(com.setSubAddress(self.rt.getAddress()), 4,
                         "Parameter not being returned correctly or is in mode command.")
        
    def test_getSubAddress(self):
        com = Command(self.rt.getAddress())
        com.setToCommandWord()
        com.setSubAddress(self.rt.getAddress())
        self.assertEqual(com.getSubAddress(), 4,
                         "subaddress not being assigned correctly.")
    
    def test_setWordCount(self):
        com = Command(self.rt.getAddress())
        com.setToCommandWord()
        self.assertEqual(com.setWordCount(2), 2, 
                         "In mode command or parameter not being returned correctly.")
    
    def test_getWordCount(self):
        com = Command(self.rt.getAddress())
        com.setToCommandWord()
        com.setWordCount(2)
        self.assertEqual(com.getWordCount(), 2, 
                         "Word Count not being set correctly or in mode command.")
    
    def test_setTransmitCommand(self):
        com = Command(self.rt.getAddress())        
        self.assertEqual(com.setTransmitCommand(), False, 
                         "Logic is incorrect.")
    
    def test_setReceiveCommand(self):
        com = Command(self.rt.getAddress())
        self.assertEqual(com.setReceiveCommand(), True, 
                         "Logic is incorrect.")
    
    def test_isTransmitCommand(self):
        com = Command(self.rt.getAddress())
        self.assertEqual(com.isTransmitCommand(), False,
                         "Logic is incorrect.")
        
        
        
        
