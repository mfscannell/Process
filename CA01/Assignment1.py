class Curve(object):
    def __init__(self, f):
        self.f = f
        self.e = 0.5
        
    def setErrorTolerance(self, e):
        if(e < 0):
            raise(ValueError,"Curve.setErrorTolerance:  invalid error threshold")
        self.e = e
        
    def getErrTolerance(self):
        return self.e
        
    def integrate(self, lowBound, highBound):
        width = 1
        areaOld = -1
        areaNew = 999
        
        while(abs(areaOld-areaNew)/areaNew > self.e):
            areaOld = areaNew
            nTrapezoids = int((highBound - lowBound) / width)
            areaNew = 0
            for i in range(1, nTrapezoids + 1):
                x0 = lowBound + (i-1)*width
                x1 = lowBound + i*width
                
                areaOfTrapezoid = width * (self.f(x0) + self.f(x1)) / 2
                areaNew = areaNew + areaOfTrapezoid
            width = width / 2.0
        return areaNew
