# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_inventoryWindow(object):
    def setupUi(self, inventoryWindow):
        inventoryWindow.setObjectName(_fromUtf8("inventoryWindow"))
        inventoryWindow.resize(1110, 672)
        inventoryWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.centralwidget = QtGui.QWidget(inventoryWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 2)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 7, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 9, 0, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 4, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 8, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.cartButton = QtGui.QPushButton(self.centralwidget)
        self.cartButton.setObjectName(_fromUtf8("cartButton"))
        self.gridLayout_2.addWidget(self.cartButton, 5, 2, 1, 1)
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setMinimumSize(QtCore.QSize(400, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeView.setFont(font)
        self.treeView.setMouseTracking(False)
        self.treeView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.treeView.setFrameShadow(QtGui.QFrame.Sunken)
        self.treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout_2.addWidget(self.treeView, 4, 0, 2, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 2, 1, 1)
        inventoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(inventoryWindow)
        QtCore.QMetaObject.connectSlotsByName(inventoryWindow)

    def retranslateUi(self, inventoryWindow):
        inventoryWindow.setWindowTitle(_translate("inventoryWindow", "MainWindow", None))
        self.label_2.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Inventory Browser</span></p></body></html>", None))
        self.pushButton.setText(_translate("inventoryWindow", "Add to Cart", None))
        self.label_15.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Microcontroller</span></p></body></html>", None))
        self.label_8.setText(_translate("inventoryWindow", "68206165", None))
        self.label_9.setText(_translate("inventoryWindow", "5", None))
        self.label_5.setText(_translate("inventoryWindow", "Box:", None))
        self.label_3.setText(_translate("inventoryWindow", "ID:", None))
        self.label_4.setText(_translate("inventoryWindow", "Shelf:", None))
        self.label_12.setText(_translate("inventoryWindow", "Available Quantity:", None))
        self.label_7.setText(_translate("inventoryWindow", "035", None))
        self.label_10.setText(_translate("inventoryWindow", "5", None))
        self.label_11.setText(_translate("inventoryWindow", "RFID:", None))
        self.label_13.setText(_translate("inventoryWindow", "<html><head/><body><p align=\"center\">ATMega328</p></body></html>", None))
        self.label_6.setText(_translate("inventoryWindow", "3", None))
        self.cartButton.setText(_translate("inventoryWindow", "View Cart", None))

