import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Calculator')

        self.divideMultiplySubtractAdd = QtWidgets.QVBoxLayout()


        self.sub2 = QtWidgets.QHBoxLayout()
        self.finalbox1 = QtWidgets.QVBoxLayout()


        self.buttonAdd = QtWidgets.QPushButton('+')

        self.divideMultiplySubtractAdd.addWidget(self.buttonAdd)

        self.sub2.addLayout(self.divideMultiplySubtractAdd)

        self.finalbox1.addLayout(self.sub2)
        self.setLayout(self.finalbox1)



# DO NOT EDIT ANYTHING BELOW THIS COMMENT

class Controller:

    def __init__(self):
        pass

    def show_calculator(self):
        self.window = MainWindow()
        self.window.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()