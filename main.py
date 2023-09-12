# -*- coding: utf-8 -*-
# @Author  : LG
# import os

from PyQt5 import QtWidgets
import os
import sys
os.environ['SAM_ANN_BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.environ['SAM_ANN_BASE_DIR'], 'lib'))
from sam_ann import MainWindow



if __name__ == '__main__':

    app = QtWidgets.QApplication([''])
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

