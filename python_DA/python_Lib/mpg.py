class Car:
    # class variable
    
    # 생성자(constructor)
    def __init__(self,a,b,c,d,e,f,g,h,i,j,k):
        self.cManufacturer = a
        self.cModel = b
        self.cDispl = float(c)
        self.cYear = int(d)
        self.cCyl = int(e)
        self.cTrans = f
        self.cDrv = g
        self.cCty = int(h)
        self.cHwy = int(i)
        self.cFl = j
        self.cClass = k
        
        self.cAvg = self.calcul_avg()
    
    # method
class Audi:
    


