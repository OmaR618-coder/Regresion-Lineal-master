#CASOS-Caso_2.py
#TEST 2 X1,Y2
class Caso_dos(object):
    def __init__(self, dialog):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
        self.xavg=0
        self.contadorN=0
        self.yavg=0
        self.contador2N=0
        self.x2=0
        self.xy=0
        self.y2=0
        #SHOW
        self.B1=0
        self.rxy=0
        self.r2=0
        self.B0=0
        self.yk=0
        self.dialog = dialog

    def code2(self):
        #SACAMOS XAVG
        for i in self.x:
            self.xavg += i
            self.contadorN += 1
        self.xavg = self.xavg/self.contadorN

        #SACAMOS YAVG
        for i in self.y:
            self.yavg += i
            self.contador2N += 1
        self.yavg = self.yavg/self.contador2N
        print("yavg = ",self.yavg )

        #sacamos x²
        for i in self.x:
            self.x2 += i**2
        print("x² =", self.x2)
       
        #sacamos xy
        for i in range(len(self.x)):
            self.xy += self.x[i]*self.y[i]
        print("x*y =", self.xy)

        #sacamos y²
        for i in self.y:
            self.y2 += i**2
        print("y² =", self.y2)

        #CALCULAMOS B1
        self.B1 = (self.xy-(self.contadorN*self.xavg*self.yavg))/((self.x2)-(self.contadorN*self.xavg**2))
        """print("B1 =", "%.6f"%self.B1) #IMPRIMOS B1 CON 6 DECIMALES"""
        self.dialog.showB1A.setText(str(self.B1)) #nombre del label de qt

        #CALCULAMOS Rxy
        self.rxy = (10*self.xy-self.xavg*self.yavg)/((10*self.x2-self.xavg**2)*(10*self.y2-self.yavg**2))**0.5
        self.dialog.showrxyA.setText(str(self.rxy)) #nombre del label de qt
       
        #CALCULAMOS R²
        self.r2 = self.rxy*self.rxy
        self.dialog.showr2A.setText(str(self.r2)) #nombre del label de qt
       
        #CALCULAMOS B0
        self.B0 = self.yavg-self.xavg*self.B1
        self.dialog.showB0A.setText(str(self.B0)) #nombre del label de qt
       
        #CALCULAMOS YK SABIENDO QUE XK ES 386
        self.yk  =self.B0+self.B1*386
        self.dialog.showykA.setText(str(self.yk)) #nombre del label de qt
       