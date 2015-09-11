'''
Created 2-25-2014

Modified 3-2-2014
@author: Chauncey Philpot: cbp0009
'''
import unittest
from starCatalog import StarCatalog
class StarCatalogTest(unittest.TestCase):
    
    fileName = "catalog.txt"
    
    def test_ObjectCreation(self):
        myCat = StarCatalog()        
        self.assertTrue(isinstance(myCat, StarCatalog), "Object is not of type StarCatalog.")
    
    def test_getView(self):
        myCat = StarCatalog()
        self.assertEqual(myCat.getView(), 0.017453, "Default Value Not Set")
    
    def test_loadCatalog(self):
        myCat = StarCatalog()
        self.assertEquals(myCat.loadCatalog(self.fileName), 12, "failed to load file correctly.")
        self.assertRaises(ValueError, myCat.loadCatalog, "invalidFile.txt")
    
    def test_getCount(self):
        myCat = StarCatalog()
        myCat.loadCatalog(self.fileName)
        
        self.assertEquals(myCat.getCount(6.5), 7, "Failed to get the correct number of stars.")
    
    def test_getCount2(self):
        myCat = StarCatalog()
        
        self.assertRaises(ValueError, myCat.getCount, 6.5)
        
    
    def test_set_GetView(self):
        myCat = StarCatalog()
        myCat.loadCatalog(self.fileName)
        myCat.setView(.01)
        self.assertEquals(myCat.getView(), 0.01, "Not setting or get field of view correctly.")
    
    def test_setView2(self):
        myCat = StarCatalog()
        myCat.loadCatalog(self.fileName)        
        self.assertRaises(ValueError, myCat.setView, 'a')
        self.assertRaises(ValueError, myCat.setView, -3)
        self.assertRaises(ValueError, myCat.setView, 9)
    
    def test_getMagnitude(self):
        myCat = StarCatalog()
        
        self.assertRaises(ValueError, myCat.getMagnitude, 0.00139706, -0.77301636)
        
        myCat.loadCatalog(self.fileName)
        myCat.setView(.01)
        self.assertEquals(myCat.getMagnitude(0.00139706, -0.77301636), 5.1, "Incorrect value returned for magnitude.")
        self.assertRaises(ValueError, myCat.getMagnitude, 7, -0.77301636)
        self.assertRaises(ValueError, myCat.getMagnitude, 0, 3)
        
if __name__ == '__main__':
    unittest.main()
