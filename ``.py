import sys
from PyQt5 import QtGui, QtCore, QtWidgets
def window():
    app = QtWidgets.QApplication (sys.argv)
    From = QtWidgets.QWidget() 
    From.resize(540,600)
    From.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    From.setAttribut(QtCore.Qt.WA_TranslucentBackground)
    label = QtWidgets.QLabel(Form)
    label.setGeometry(QtCore.QRect(10, 15, 840, 550))
    movie1 = QtGui.QMovie("abcd.gif")
    label.setMovie(movie1)
    movie1.start()
    Form.show()
    sys.exit(app.exec_())
if"__name__"=="__main__":
    window()
    