# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cart.ui'
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

class Ui_cartWindow(object):
    def setupUi(self, cartWindow):
        cartWindow.setObjectName(_fromUtf8("cartWindow"))
        cartWindow.resize(1094, 795)
        cartWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"\\"))
        self.gridLayout_3 = QtGui.QGridLayout(cartWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 3)
        self.label_2 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(cartWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.treeView = QtGui.QTreeView(cartWindow)
        self.treeView.setMinimumSize(QtCore.QSize(400, 350))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.gridLayout_2.addWidget(self.treeView, 2, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spinBox = QtGui.QSpinBox(cartWindow)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 7, 1, 1, 1)
        self.label_3 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_11 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(cartWindow)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1)
        self.label_5 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_8 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_10 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1)
        self.label_4 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_13 = QtGui.QLabel(cartWindow)
        self.label_13.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 2)
        self.label_9 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)
        self.label_15 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 2)
        self.label_12 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 5, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)

        self.retranslateUi(cartWindow)
        QtCore.QMetaObject.connectSlotsByName(cartWindow)

    def retranslateUi(self, cartWindow):
        cartWindow.setWindowTitle(_translate("cartWindow", "Form", None))
        self.label_2.setText(_translate("cartWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Cart</span></p></body></html>", None))
        self.label_3.setText(_translate("cartWindow", "ID:", None))
        self.label_7.setText(_translate("cartWindow", "035", None))
        self.label_11.setText(_translate("cartWindow", "RFID:", None))
        self.pushButton.setText(_translate("cartWindow", "Remove From Cart", None))
        self.label_5.setText(_translate("cartWindow", "Box:", None))
        self.label_8.setText(_translate("cartWindow", "68206165", None))
        self.label_6.setText(_translate("cartWindow", "3", None))
        self.label_10.setText(_translate("cartWindow", "5", None))
        self.label_4.setText(_translate("cartWindow", "Shelf:", None))
        self.label_13.setText(_translate("cartWindow", "<html><head/><body><p align=\"center\">ATMega328</p></body></html>", None))
        self.label_9.setText(_translate("cartWindow", "5", None))
        self.label_15.setText(_translate("cartWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Microcontroller</span></p></body></html>", None))
        self.label_12.setText(_translate("cartWindow", "Available Quantity:", None))

