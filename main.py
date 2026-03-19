#main.py
from load.load_interfaz_regresion_lineal import Interfaz

from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    interface = Interfaz()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
