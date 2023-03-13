from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from browserUi import Ui_Form
import sys

class MoWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MoWidget, self).__init__()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

class BrowserApp(MoWidget, Ui_Form):
    def __init__(self):
        super(BrowserApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2.clicked.connect(self.winShowMaximized)
        self.pushButton_3.clicked.connect(sys.exit)
        self.lineEdit.returnPressed.connect(self.load)
        self.pushButton_4.clicked.connect(self.backward)
        self.pushButton_5.clicked.connect(self.forward)
        self.pushButton_6.clicked.connect(self.reload)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)    
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)
    def winShowMaximized(self):
        if self.pushButton_2.isChecked():
            self.widget.setStyleSheet("QWidget#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(20, 20, 20, 255), stop:0.706215 rgba(20, 20, 20, 255), stop:0.711864 rgba(45, 45, 46, 255), stop:1 rgba(45, 45, 45, 255));border:0px solid rgb(45, 45, 45);border-radius:0px;}")
            self.showMaximized()
        else:
            self.widget.setStyleSheet("QWidget#widget{border:4px solid rgb(45, 45, 45);border-radius:20px;}")
            self.showNormal()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = BrowserApp()
        Form.show()
        sys.exit(app.exec_())
