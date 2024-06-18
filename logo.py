import sys
from PyQt5 import QtGui, QtCore, QtWidgets
def window():
    pass
    

if __name__=="__main__":
    app = QtWidgets.QApplication (sys.argv)
    Form = QtWidgets.QWidget() 
    Form.resize(540,600)
    Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    label = QtWidgets.QLabel(Form)
    label.setGeometry(QtCore.QRect(10, 15, 840, 550))
    movie1 = QtGui.QMovie('abcd.gif')
    label.setMovie(movie1)
    movie1.start()
    Form.show()
    a =input("tg6g4rf")    
    print(a)
    sys.exit(app.exec_())


                                                