

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 515)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 520, 390))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(180, 20, 291, 361))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Logo = QtWidgets.QLabel(self.widget)
        self.Logo.setGeometry(QtCore.QRect(270, 30, 111, 121))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("imgs/download.png"))
        self.Logo.setScaledContents(False)
        self.Logo.setObjectName("Logo")
        self.Username = QtWidgets.QLineEdit(self.widget)
        self.Username.setGeometry(QtCore.QRect(220, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgba(0,0,0);\n"
"padding -bottom:7px;")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(220, 250, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgba(0,0,0);\n"
"padding -bottom:7px;")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Login = QtWidgets.QPushButton(self.widget)
        self.Login.setGeometry(QtCore.QRect(220, 320, 221, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Login.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")

        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Username.setPlaceholderText(_translate("Form", "Username"))
        self.Password.setPlaceholderText(_translate("Form", "Password"))
        self.Login.setText(_translate("Form", "Log In"))



