'''
Created on Mar 27, 2014
LOC: 66
@author: 
'''


class Status(object):
    
    address = None
    requestFlag = None
    messageFlag = None
    busyFlag = None
    
    def __init__(self, addressIn):
        
        self.requestFlag = False
        self.messageFlag = False
        self.busyFlag = False
        
        try:
            if(addressIn == None):
                raise ValueError
            else:
                if(isinstance(addressIn, int)):
                    if(addressIn >= 0 and addressIn <=31):
                        self.address = addressIn
                else:
                    raise ValueError
        except ValueError:
            print("Status.init:  address is invalid or missing. Must be between from 0 to 31.")
    
    def getTerminalAddress(self):
        return self.address
    
    def setServiceRequest(self):
        isSet = False
        if(self.requestFlag == True):
            isSet = True
        else:
            isSet = False
            self.requestFlag = True
        
        return isSet
    
    def isServiceRequested(self):
        isService = False
        
        if(self.requestFlag == True):
            isService = True
        else:
            isService = False
            
        return isService
    
    def setMessageError(self):
        isSet = False
        if(self.messageFlag == True):
            isSet = True
        else:
            isSet = False
            self.messageFlag = True
        
        return isSet
    
    def isMessageError(self):
        isService = False
        
        if(self.messageFlag == True):
            isService = True
        else:
            isService = False
            
        return isService
    
    def setBusy(self):
        isSet = False
        if(self.busyFlag == True):
            isSet = True
        else:
            isSet = False
            self.busyFlag = True
        
        return isSet
    
    def isBusy(self):
        isService = False
        
        if(self.busyFlag == True):
            isService = True
        else:
            isService = False
            
        return isService
        
