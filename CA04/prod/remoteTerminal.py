'''
Created on Mar 27, 2014
Total LOC: 287
LOC: 22
@author: chanpod
'''

from CA04.prod.bus import Bus

class RemoteTerminal(object):
    
    address = None
    
    def __init__(self, addressIn=None):
        try:
            if(addressIn == None):
                raise ValueError
            else:
                if(isinstance(addressIn, int)):
                    if(addressIn >= 0 and addressIn <= 31):
                        self.address = addressIn
                    else:
                        raise ValueError
                else:
                    raise ValueError
        except ValueError:
            print("RemoteTerminal.init:"
                  "  Valid Address from 0 to 31 must be given.")
            raise ValueError
    
    def readBus(self, busIn = None):
            bus = Bus()
            try:
                if(busIn == None):
                    raise ValueError
                else:
                    if(isinstance(busIn, Bus)):
                        bus.writeBus(busIn.readBus())
                    else:
                        raise ValueError
                return bus
            except ValueError:
                print("RemoteTerminal.readBus:"  
                    "  Bus object not give or not an instance of Bus.")
                raise ValueError
    def getAddress(self):
        return self.address
        

                     
