from krita import *
from PyQt5.QtWidgets import *

class DockerExample(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docker Example")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)

        exampleButton = QPushButton("Show Popup", mainWidget)
        exampleButton.clicked.connect(self.popup)

        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(exampleButton)
    
    def popup(self):
        QMessageBox.information(QWidget(), "DockerExample", "It works!")

    def canvasChanged(self, canvas):
        pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("dockerExample", DockWidgetFactoryBase.DockRight, DockerExample))