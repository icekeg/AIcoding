from krita import *
from PyQt5.QtWidgets import QWidget, QMessageBox

def showwin():
    QMessageBox.information(QWidget(), "WindowTest", "It works!")

class WindowTest(Extension):
    def __init__(self, parent):
        super(WindowTest, self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("window_test_id", "window Test", "tools/scripts")
        action.triggered.connect(showwin)

Krita.instance().addExtension(WindowTest(Krita.instance()))
        