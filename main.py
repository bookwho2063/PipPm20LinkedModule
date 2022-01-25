import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("ui/test02.ui", self)
        self.ui.show()

    def init_widget(self):
        self.setWindowTitle("타이틀명칭")

    @pyqtSlot()
    def slot_1st(self):
        self.ui.label.setText('첫번째')

    @pyqtSlot()
    def slot_2nd(self):
        self.ui.label.setText('두번째')

    @pyqtSlot()
    def slot_3rd(self):
        self.ui.label.setText('세번째')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    sys.exit(app.exec())