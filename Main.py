

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from numpy.lib.twodim_base import fliplr

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 423)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Casilla = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla.setGeometry(QtCore.QRect(170, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla.setFont(font)
        self.Casilla.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla.setObjectName("Casilla")
        self.Casilla_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_2.setGeometry(QtCore.QRect(250, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_2.setFont(font)
        self.Casilla_2.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_2.setObjectName("Casilla_2")
        self.Casilla_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_3.setGeometry(QtCore.QRect(330, 80, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_3.setFont(font)
        self.Casilla_3.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_3.setObjectName("Casilla_3")
        self.Casilla_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_4.setGeometry(QtCore.QRect(170, 160, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_4.setFont(font)
        self.Casilla_4.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_4.setObjectName("Casilla_4")
        self.Casilla_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_5.setGeometry(QtCore.QRect(250, 160, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_5.setFont(font)
        self.Casilla_5.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_5.setObjectName("Casilla_5")
        self.Casilla_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_6.setGeometry(QtCore.QRect(330, 160, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_6.setFont(font)
        self.Casilla_6.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_6.setObjectName("Casilla_6")
        self.Casilla_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_7.setGeometry(QtCore.QRect(170, 240, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_7.setFont(font)
        self.Casilla_7.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_7.setObjectName("Casilla_7")
        self.Casilla_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_8.setGeometry(QtCore.QRect(250, 240, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_8.setFont(font)
        self.Casilla_8.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_8.setObjectName("Casilla_8")
        self.Casilla_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Casilla_9.setGeometry(QtCore.QRect(330, 240, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Casilla_9.setFont(font)
        self.Casilla_9.setStyleSheet("background-color: white;\n"
"color: green;")
        self.Casilla_9.setObjectName("Casilla_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 143, 238, 8))
        self.label.setStyleSheet("background-color: black;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 226, 238, 8))
        self.label_2.setStyleSheet("background-color: black;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(232, 72, 8, 235))
        self.label_3.setStyleSheet("background-color: black;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(314, 70, 8, 235))
        self.label_4.setStyleSheet("background-color: black;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Boton_Inicio = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Inicio.setGeometry(QtCore.QRect(430, 180, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Boton_Inicio.setFont(font)
        self.Boton_Inicio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Boton_Inicio.setObjectName("Boton_Inicio")
        self.Label_Win = QtWidgets.QLabel(self.centralwidget)
        self.Label_Win.setGeometry(QtCore.QRect(160, 330, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Win.setFont(font)
        self.Label_Win.setText("")
        self.Label_Win.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Win.setObjectName("Label_Win")
        self.Label_Win_2 = QtWidgets.QLabel(self.centralwidget)
        self.Label_Win_2.setGeometry(QtCore.QRect(160, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Win_2.setFont(font)
        self.Label_Win_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Win_2.setObjectName("Label_Win_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Boton_Inicio.clicked.connect(self.limpiar)
        self.casillas = [self.Casilla,self.Casilla_2,self.Casilla_3,self.Casilla_4,self.Casilla_5,self.Casilla_6,self.Casilla_7,self.Casilla_8,self.Casilla_9]
        self.tablero=np.zeros((3,3),dtype=int)
        self.marca = "X"
        self.Casilla.clicked.connect(lambda: self.marcar(self.Casilla,[0,0]))
        self.Casilla_2.clicked.connect(lambda: self.marcar(self.Casilla_2,[0,1]))
        self.Casilla_3.clicked.connect(lambda: self.marcar(self.Casilla_3,[0,2]))
        self.Casilla_4.clicked.connect(lambda: self.marcar(self.Casilla_4,[1,0]))
        self.Casilla_5.clicked.connect(lambda: self.marcar(self.Casilla_5,[1,1]))
        self.Casilla_6.clicked.connect(lambda: self.marcar(self.Casilla_6,[1,2]))
        self.Casilla_7.clicked.connect(lambda: self.marcar(self.Casilla_7,[2,0]))
        self.Casilla_8.clicked.connect(lambda: self.marcar(self.Casilla_8,[2,1]))
        self.Casilla_9.clicked.connect(lambda: self.marcar(self.Casilla_9,[2,2]))
        



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TresEnRaya"))
        self.Casilla.setText(_translate("MainWindow", "X"))
        self.Casilla_2.setText(_translate("MainWindow", "X"))
        self.Casilla_3.setText(_translate("MainWindow", "X"))
        self.Casilla_4.setText(_translate("MainWindow", "X"))
        self.Casilla_5.setText(_translate("MainWindow", "X"))
        self.Casilla_6.setText(_translate("MainWindow", "X"))
        self.Casilla_7.setText(_translate("MainWindow", "X"))
        self.Casilla_8.setText(_translate("MainWindow", "X"))
        self.Casilla_9.setText(_translate("MainWindow", "X"))
        self.Boton_Inicio.setText(_translate("MainWindow", "Iniciar/Reiniciar"))
        self.Label_Win_2.setText(_translate("MainWindow", "TRES EN RAYA"))
    def comprobar(self):
        if np.sum(self.tablero[0,:])==3 or np.sum(self.tablero[1,:])==3 or np.sum(self.tablero[2,:])==3:
                return True
        elif np.sum(self.tablero[:,0])==3 or np.sum(self.tablero[:,1])==3 or np.sum(self.tablero[:,2])==3:
                return True
        elif np.sum(np.trace(self.tablero))==3 or np.sum(np.trace(np.fliplr( self.tablero)))==3 :
                return True
        elif np.sum(self.tablero[0,:])==-3 or np.sum(self.tablero[1,:])==-3 or np.sum(self.tablero[2,:])==-3:
                return True
        elif np.sum(self.tablero[:,0])==-3 or np.sum(self.tablero[:,1])==-3 or np.sum(self.tablero[:,2])==-3:
                return True
        elif np.sum(np.trace(self.tablero))==-3 or np.sum(np.trace(np.fliplr( self.tablero)))==-3 :
                return True
        return False

        pass 

    def marcar(self,cas,cord):
        if self.marca=="X":
                cas.setStyleSheet("color: green")
                cas.setText("X")
                self.tablero[cord[0],cord[1]]=1
                if self.comprobar():
                        self.Label_Win.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                self.marca="O"
        else:
                cas.setStyleSheet("color: red")
                cas.setText("O")
                self.tablero[cord[0],cord[1]]=-1
                if self.comprobar():
                        self.Label_Win.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                                
                self.marca="X"
        

        print(self.tablero)
        pass
    def limpiar(self):
        self.marca = "X"
        self.tablero=np.zeros((3,3),dtype=int)
        self.Label_Win.clear()
        for c in self.casillas:
                c.setText("")
                c.setDisabled(False)
                c.setStyleSheet("background-color: white;\n"
"color: green;")
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
