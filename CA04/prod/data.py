'''
Created on Mar 27, 2014
LOC: 30
@author: 
'''


class Data(object):
    MAXINT = 65535
    MININT = 0
    payload = None
    
    def __init__(self, payloadIn = None):
        if(payloadIn != None):
            try:
                if(isinstance(payloadIn, int)):
                    if(payloadIn >= self.MININT and payloadIn <= self.MAXINT):
                        self.payload = payloadIn
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Data.init: Payload isn't a valid integer: 0 to 65535")
                raise ValueError
    
    def setContent(self, payloadIn = None):
        try:
            if(payloadIn != None):                            
                if(isinstance(payloadIn, int)):
                    if(payloadIn >= self.MININT and payloadIn <= self.MAXINT):
                        self.payload = payloadIn
                        return payloadIn
                    else:
                        raise ValueError
                else:
                    raise ValueError
        
        except ValueError:
                print("Data.setContent: Payload isn't a valid integer: 0 to 65535 or is missing")
                raise ValueError
    
    def getContent(self):
        return self.payload
