'''
Created on Mar 29, 2014

@author: chanpod
'''
import unittest
from CA04.prod.bus import Bus
from CA04.prod.status import Status
from CA04.prod.data import Data
from CA04.prod.command import Command

class DataTest(unittest.TestCase):


    def test_init(self):
        #Happy Case
        data = Data(1)
        self.assertTrue(isinstance(data, Data), 
                         "Payload not being assigned properly.")
        data = Data()
        self.assertEqual(data.getContent(), None,
                         "Payload not being assigned properly.")
        
        #Sad Case
        self.assertRaises(ValueError, Data, -1)
        self.assertRaises(ValueError, Data, 'a')
    
    def test_setContent(self):
        #Happy Case
        data = Data()
        
        self.assertEqual(data.setContent(3), 3, 
                         "setContent is not returning the correct number.")
        
        #Sad Case
        self.assertRaises(ValueError, data.setContent, -1)
        self.assertRaises(ValueError, data.setContent, 'a')
    
    def test_getContent(self):
        data = Data(1)
        self.assertEqual(data.getContent(), 1, 
                         "payload isn't being assigned properly.")
