import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mainwindow
import startui

application = QApplication(sys.argv)


def quitevent():
    sys.exit(application.exec_())


def main():
    start = startui.startUI()
    start.show()
    application.aboutToQuit.connect(quitevent())
    

if __name__ == '__main__':
    main()
