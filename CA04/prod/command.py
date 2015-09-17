'''
Created on Mar 27, 2014
LOC: 151
@author: 
'''


class Command(object):
    
    address = None
    COMMANDWORD = 1
    MODECOMMAND = 2
    TRANSMIT = 1
    RECEIVE = 2
    
    #Mode Codes
    TRANSMITSTATUS = 2
    SHUTDOWN = 4
    RESET = 8
    TRANSMITVECTOR = 12
    TRANSMITLASTCOMMAND = 14
    
    commandType = 1
    modeCommand = 0
    count = 0
    tran_receiveFlag = RECEIVE
    subaddress = 0
    
    def __init__(self, addressIn = None):
        self.commandType = self.MODECOMMAND
        self.tran_receiveFlag = self.RECEIVE
        self.modeCommand = self.TRANSMITSTATUS
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
        except:
            print("Command.init: Address is invalid or missing."
                  "Must be from 0 to 31.")
            raise ValueError
    
    def getTerminal(self):
        return self.address
    
    def setToCommandWord(self):
        if(self.commandType == self.COMMANDWORD)  :          
            return True
        else:
            self.commandType = self.COMMANDWORD
            return False
    
    def setToModeCommand(self, modeIn = None):
        MODEMIN = 0
        MODEMAX = 14
        if(modeIn != None):
            try:
                if(isinstance(modeIn, int)):
                    
                    if(modeIn >= MODEMIN and modeIn <= MODEMAX):
                        
                        if(modeIn == self.TRANSMITSTATUS):
                            self.modeCommand = self.TRANSMITSTATUS
                            return modeIn
                        elif(modeIn == self.SHUTDOWN):
                            self.modeCommand = self.SHUTDOWN
                            return modeIn
                        elif(modeIn == self.RESET):
                            self.modeCommand = self.RESET
                            return modeIn
                        elif(modeIn == self.TRANSMITVECTOR):
                            self.modeCommand = self.TRANSMITVECTOR
                            return modeIn
                        elif(modeIn == self.TRANSMITLASTCOMMAND):
                            self.modeCommand = self.TRANSMITLASTCOMMAND
                            return modeIn
                        else:
                            raise ValueError
                            
                    else:
                        raise ValueError
                else:
                    raise ValueError
                
            except ValueError:
                print("Command.setToModeCommand: mode is invalid. Must be 2, 4, 8, 12, or 14.")
                raise ValueError
        else:
            self.modeCommand = self.TRANSMITSTATUS
    
    def getModeCode(self):
        try:
            if(self.commandType == self.MODECOMMAND):
                return self.modeCommand
            else:
                raise ValueError
        except ValueError:
            print("Command.getModeCode:  Current state is command word.")
            raise ValueError
    
    def isModeCommand(self):
        if(self.commandType == self.MODECOMMAND):
            return True
        else:
            return False
    
    def setSubAddress(self, address = None):
        ADDRESSMIN = 0
        ADDRESSMAX = 31
        try:
            if(self.commandType == self.MODECOMMAND):
                raise ValueError
        except ValueError:
            print("Command.setSubAddress:  Instance is in mode commmand.")
            raise ValueError
            return
            
        try:
            if(address == None):
                raise ValueError            
            else:
                if(isinstance(address, int)):
                    if(address >= ADDRESSMIN and address <= ADDRESSMAX):
                        self.subaddress = address
                        return address
                else:
                    raise ValueError
        except ValueError:
            print("Command.setSubAddress:  address is invalid. Must be an int from 0 to 31.")
            raise ValueError
    
    def getSubAddress(self):
        try:
            if(self.commandType == self.MODECOMMAND):
                raise ValueError
            else:
                return self.subaddress
        except ValueError:
            print("Command.getSubAddress:  Instance is in mode commmand.")
            raise ValueError
    
    def setWordCount(self, countIn = None):
        try:
            if(self.commandType == self.MODECOMMAND):
                raise ValueError           
        except ValueError:
            print("Command.setWordCount:  Instance is in mode commmand.")
            raise ValueError
            return
        
        try:
            if(isinstance(countIn, int)):
                if(countIn >= 0 and countIn <= 32):
                    self.count = countIn
                    return countIn
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Command.setWordCount:  Count isn't a valid int. Must be from 0 to 32.")
            raise ValueError
    
    def getWordCount(self):
        try:
            if(self.commandType == self.MODECOMMAND):
                raise ValueError           
            else:
                return self.count
        except ValueError:
            print("Command.getWordCount:  Instance is in mode commmand.")
            raise ValueError
            return
        
    def setTransmitCommand(self):
        if(self.tran_receiveFlag == self.TRANSMIT):            
            return True
        else:
            self.tran_receiveFlag = self.TRANSMIT
            return False
    def setReceiveCommand(self):
        if(self.tran_receiveFlag == self.RECEIVE):            
            return True
        else:
            self.tran_receiveFlag = self.RECEIVE
            return False
    
    def isTransmitCommand(self):
        if(self.tran_receiveFlag == self.TRANSMIT):            
            return True
        else:      
            return False
        
