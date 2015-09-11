'''
@author: Chauncey Philpot: cbp0009
'''
import re
import math
import os.path
class StarCatalog(object):
   
    def __init__(self, fileName = None):
        self.fov = 0.017453
        self.currentCatalog = []
        self.catalog = []
        
        if(fileName != None):
            self.loadCatalog(fileName)

    def getCount(self, magnitude = None):
        #Error Checking --------------------------
        try:
            if(self.catalog == None):
                raise ValueError
        except  ValueError:
            print("CA02.getCount:  Must load a star catalog first.")
         
        try:
            if(isinstance(magnitude, (float,int)) == False):
                raise ValueError           
        except ValueError:
            print("CA02.getCount:  Must be a number.")
        
        #Logic ----------------------------
        count = 0
        if(magnitude == None):
            return len(self.catalog)
        
        
        for catalog in self.catalog:
            mag = float(catalog[1])
            diff = magnitude - mag
            if(diff < 0.5 and diff > -0.5):
                count = count + 1
                
        return count

    def getMagnitude(self, ra, dec):
        try:
            if(self.catalog == None):
                raise ValueError
        except ValueError:
            print("CA02.getMagnitude:  CA02 is empty!")
        
        validStars = []
        
        try:
            if(ra < 0 or ra > 2 * math.pi):
                raise ValueError
        except ValueError:
            print("CA02.getMagnitude:  ra isn't in the proper range of 0 to 2pi")
        
        try:
            if(dec < -math.pi/2 or dec > math.pi/2):
                raise ValueError
        except ValueError:
            print ("CA02.getMagnitude:  dec isn't in the proper range of -pi/2 to pi/2")
            
        for catalog in self.catalog:
            rAsc = float(catalog[2])
            declination = float(catalog[3])
            modifiedFOV = float(self.fov/2)
            
            #rAsc is the one from the file. It must be between the ra +- fov/2
            #repeat for declination
            if(((rAsc >= (ra - modifiedFOV)) and (rAsc <= (ra + modifiedFOV))) 
               and ((declination >= (dec - modifiedFOV)) and (declination <= (dec + modifiedFOV)))):
                
                validStars.append(catalog[1])
        
        validStars.sort()
        if(len(validStars) == 0):
            return None
        
        return validStars[0]
        
    def getView(self):
        return self.fov

    def setView(self, fov):
        self.fov = fov
        

    def loadCatalog(self, fileName = None):
        
        try:
            if(fileName == None):
                raise ValueError
        except ValueError:
            print("CA02.loadCatalog:  Must give a file name to read from!")
        
        #Verify file exist
        try:
            if(os.path.isfile(fileName)):
                content = open(fileName, 'r')
            else:
                raise ValueError
        except ValueError:
            print ("CA02.loadCatalog:  Invalid filename. File likely does not exist.")
        
        #empty StarCatalog
        self.catalog = []
        for item in content: #for each line in the file
            
            splitString = re.split('\s+', item) #parse line by space and tabs                
            
            if(len(splitString) != 4):
                splitString.pop(4) #remove newline char
            
            for num in splitString:
                try:
                    if(isinstance(num, (int, long, float)) == True):
                        raise ValueError #make sure data is a number
                except ValueError:
                    print ("CA02.loadCatalog:  File contains invalid data. Data must contain numbers.")                    
            
            self.catalog.append(splitString) #add list to catalog

        
        return len(self.catalog)

