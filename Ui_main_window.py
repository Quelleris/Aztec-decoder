# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sugil\OneDrive\Pulpit\Inżynierka\Ui_Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Lb_Image = QtWidgets.QLabel(self.centralwidget)
        self.Lb_Image.setGeometry(QtCore.QRect(20, 20, 401, 421))
        self.Lb_Image.setText("")
        self.Lb_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Lb_Image.setObjectName("Lb_Image")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 80, 301, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Vlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Vlayout.setContentsMargins(20, 20, 20, 20)
        self.Vlayout.setSpacing(20)
        self.Vlayout.setObjectName("Vlayout")
        self.Btn_open_image = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_open_image.setObjectName("Btn_open_image")
        self.Vlayout.addWidget(self.Btn_open_image)
        self.Gb_options = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.Gb_options.setObjectName("Gb_options")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Gb_options)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Rbtn_odszumianie_1 = QtWidgets.QRadioButton(self.Gb_options)
        self.Rbtn_odszumianie_1.setObjectName("Rbtn_odszumianie_1")
        self.horizontalLayout.addWidget(self.Rbtn_odszumianie_1)
        self.Rbtn_odszumianie_2 = QtWidgets.QRadioButton(self.Gb_options)
        self.Rbtn_odszumianie_2.setObjectName("Rbtn_odszumianie_2")
        self.horizontalLayout.addWidget(self.Rbtn_odszumianie_2)
        self.Vlayout.addWidget(self.Gb_options)
        self.Btn_decode = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Btn_decode.setObjectName("Btn_decode")
        self.Vlayout.addWidget(self.Btn_decode)
        self.Lb_decoded_code = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Lb_decoded_code.setObjectName("Lb_decoded_code")
        self.Vlayout.addWidget(self.Lb_decoded_code)
        self.Te_decoded_text = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.Te_decoded_text.setObjectName("Te_decoded_text")
        self.Vlayout.addWidget(self.Te_decoded_text)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuO_programie = QtWidgets.QMenu(self.menubar)
        self.menuO_programie.setObjectName("menuO_programie")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionO_programie = QtWidgets.QAction(MainWindow)
        self.actionO_programie.setObjectName("actionO_programie")
        self.menuO_programie.addAction(self.actionO_programie)
        self.menubar.addAction(self.menuO_programie.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_open_image.setText(_translate("MainWindow", "Otwórz obraz"))
        self.Gb_options.setTitle(_translate("MainWindow", "Opcje odszumiania"))
        self.Rbtn_odszumianie_1.setText(_translate("MainWindow", "Opcja 1"))
        self.Rbtn_odszumianie_2.setText(_translate("MainWindow", "Opcja 2"))
        self.Btn_decode.setText(_translate("MainWindow", "Rozszyfruj kod"))
        self.Lb_decoded_code.setText(_translate("MainWindow", "Rozszyfrowany tekst:"))
        self.menuO_programie.setTitle(_translate("MainWindow", "Program"))
        self.actionO_programie.setText(_translate("MainWindow", "O programie"))