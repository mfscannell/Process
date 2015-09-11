'''
@author: 
'''
import re
import math
import os.path
 
class StarCatalog(object):
   
    def __init__(self, fileName=None):
        self.fov = 0.017453
        self.currentCatalog = []
        self.catalog = None
        
        if(fileName != None):
            self.loadCatalog(fileName)

    def getCount(self, magnitude=None):
        # initialize variables
        variance = 0.5
        magIndex = 1
        
        #Error Checking --------------------------
        try:
            if(self.catalog == None):
                raise ValueError
        except  ValueError:
            print("StarCatalog.getCount:  Must load a star catalog first.")
            raise ValueError
         
        try:
            if(isinstance(magnitude, (float, int)) == False):
                raise ValueError           
        except ValueError:
            print("StarCatalog.getCount:  Must be a number.")
            raise ValueError
        
        #Logic ----------------------------
        count = 0
        if(magnitude == None):
            return len(self.catalog)        
        
        for catalog in self.catalog:
            
            mag = float(catalog[magIndex])
            diff = magnitude - mag            
            
            if(diff < variance and diff > -variance):
                count = count + 1
                
        return count

    def getMagnitude(self, ra, dec):
        # initialize variables
        divisor = 2
        raIndex = 2
        declIndex = 3
        magIndex = 1
        validStars = []  
        
        #error checking --------------------------------
        try:
            if(self.catalog == None):
                raise ValueError
        except ValueError:
            print("StarCatalog.getMagnitude:  Catalog is empty!")
            raise ValueError        
              
        lowerBound = 0
        upperBound = 2 * math.pi
        
        try:
            if(ra < lowerBound or ra > upperBound):
                raise ValueError
        except ValueError:
            print("StarCatalog.getMagnitude:  ra isn't in the proper range of 0 to 2pi")
            raise ValueError
        
        lowerBound = math.pi / divisor
        upperBound = math.pi / divisor
        
        try:
            if(dec < -lowerBound or dec > upperBound):
                raise ValueError
        except ValueError:
            print ("StarCatalog.getMagnitude:  dec isn't in the proper range of -pi/2 to pi/2")
            raise ValueError
        
        #logic--------------------------------------- 
        
        for catalog in self.catalog:
            rAsc = float(catalog[raIndex])
            declination = float(catalog[declIndex])
            modifiedFOV = float(self.fov / divisor)
            
            # rAsc is the one from the file. It must be between the ra +- fov/2
            # repeat for declination
            if(((rAsc >= (ra - modifiedFOV)) and (rAsc <= (ra + modifiedFOV))) 
               and ((declination >= (dec - modifiedFOV)) 
               and (declination <= (dec + modifiedFOV)))):
                
                validStars.append(catalog[magIndex])
        
        validStars.sort()
        if(len(validStars) == 0):
            return None
        
        return float(validStars[0])
        
    def getView(self):
        return self.fov

    def setView(self, fov):
        
        #error Checking ----------------------------
        try:  # fov must be a number
            if(isinstance(fov, (int, float, long)) == False):          
                raise ValueError
        except ValueError:
            print("StarCatalog.setView:  fov isn't a number")
            raise ValueError
        
        lowerBound = 0
        upperBound = 2 * math.pi
        
        try:  # bounds checking
            if(fov < lowerBound or fov > upperBound):
                raise ValueError
        except ValueError:
            print("StarCatalog.setView:  fov isn't in the proper range of 0 to 2pi")
            raise ValueError
        
        #logic -----------------------------------
        self.fov = fov
        

    def loadCatalog(self, fileName=None):
        
        lengthOfCatalog = 4
        popIndex = 4
        
        #error Checking --------------------------
        try:
            if(fileName == None):
                raise ValueError
        except ValueError:
            print("StarCatalog.loadCatalog:  Must give a file name to read from!")
            raise ValueError
        
        # Verify file exist
        try:
            if(os.path.isfile(fileName)):
                content = open(fileName, 'r')
            else:
                raise ValueError
        except ValueError:
            print ("StarCatalog.loadCatalog:  Invalid filename. File likely does not exist.")
            raise ValueError
        
        #logic -------------------------
        # empty StarCatalog for new one
        self.catalog = []
        for item in content:  # for each line in the file
            
            splitString = re.split('\s+', item)  # parse line by space and tabs                
            
            if(len(splitString) != lengthOfCatalog):
                splitString.pop(popIndex)  # remove newline char
            
            for num in splitString:
                try:
                    if(isinstance(num, (int, long, float)) == True):
                        raise ValueError  # make sure data is a number
                except ValueError:
                    print ("StarCatalog.loadCatalog:  File contains invalid data. Data must contain numbers.")
                    raise ValueError                    
            
            self.catalog.append(splitString)  # add list to catalog

        
        return len(self.catalog)
