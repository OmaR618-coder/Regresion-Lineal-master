from PyQt5 import QtWidgets,uic
from CASOS.Caso_1 import Caso_uno #Importamos por que esta en otro archivo
from CASOS.Caso_2 import Caso_dos
from CASOS.Caso_3 import Caso_tres
from CASOS.Caso_4 import Caso_cuatro

class Interfaz(QtWidgets.QDialog): #HEREDAS DE UN MAIN WINDOW
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Interfaz Regresión Líneal.ui",self) #NOMBRE ARCHIVO
        self.showMaximized()
       
       
        self.caso1.clicked.connect(self.case1) #Nombre QPushButton y .CLICKED
       
        """self.boton_sumar.clicked.connect(self.botonSumarClick)"""
        self.caso2.clicked.connect(self.case2) #Nombre QPushButton y .CLICKED
       
        self.caso3.clicked.connect(self.case3) #Nombre QPushButton y .CLICKED
       

        self.caso4.clicked.connect(self.case4) #Nombre QPushButton y .CLICKED
       

    def case1(self):
        c1 = Caso_uno(self)
        c1.code1()
   
    def case2(self):
        c2 = Caso_dos(self)
        c2.code2()

    def case3(self):
        c3 = Caso_tres(self)
        c3.code3()

    def case4(self):
        c4 = Caso_cuatro(self)
        c4.code4()
       
    def salir(self):
        self.close()
    