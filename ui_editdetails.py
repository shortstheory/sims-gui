# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdetails.ui'
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

class Ui_editDetailsWindow(object):
    def setupUi(self, editDetailsWindow):
        editDetailsWindow.setObjectName(_fromUtf8("editDetailsWindow"))
        editDetailsWindow.resize(1077, 788)
        editDetailsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        editDetailsWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.gridLayout_3 = QtGui.QGridLayout(editDetailsWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget = QtGui.QWidget(editDetailsWindow)
        self.widget.setMinimumSize(QtCore.QSize(450, 300))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 1, 451, 291))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.name = QtGui.QTextEdit(self.layoutWidget)
        self.name.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMaximumSize(QtCore.QSize(400, 40))
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.phoneCall = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneCall.sizePolicy().hasHeightForWidth())
        self.phoneCall.setSizePolicy(sizePolicy)
        self.phoneCall.setMaximumSize(QtCore.QSize(400, 40))
        self.phoneCall.setObjectName(_fromUtf8("phoneCall"))
        self.gridLayout.addWidget(self.phoneCall, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.phoneWhatsApp = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneWhatsApp.sizePolicy().hasHeightForWidth())
        self.phoneWhatsApp.setSizePolicy(sizePolicy)
        self.phoneWhatsApp.setMaximumSize(QtCore.QSize(400, 40))
        self.phoneWhatsApp.setObjectName(_fromUtf8("phoneWhatsApp"))
        self.gridLayout.addWidget(self.phoneWhatsApp, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.roomNumber = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomNumber.sizePolicy().hasHeightForWidth())
        self.roomNumber.setSizePolicy(sizePolicy)
        self.roomNumber.setMaximumSize(QtCore.QSize(400, 40))
        self.roomNumber.setObjectName(_fromUtf8("roomNumber"))
        self.gridLayout.addWidget(self.roomNumber, 3, 1, 1, 1)
        self.email = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)
        self.email.setMaximumSize(QtCore.QSize(400, 40))
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout.addWidget(self.email, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_10 = QtGui.QLabel(editDetailsWindow)
        self.label_10.setStyleSheet(_fromUtf8("font: 24pt \"Noto Sans\";"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(editDetailsWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(editDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(editDetailsWindow)

    def retranslateUi(self, editDetailsWindow):
        editDetailsWindow.setWindowTitle(_translate("editDetailsWindow", "Form", None))
        self.label_3.setText(_translate("editDetailsWindow", "Phone No. (WhatsApp)", None))
        self.label_2.setText(_translate("editDetailsWindow", "Phone No. (Calling)\n"
"", None))
        self.label_4.setText(_translate("editDetailsWindow", "Room Number\n"
"", None))
        self.label_5.setText(_translate("editDetailsWindow", "Personal Email", None))
        self.label.setText(_translate("editDetailsWindow", "Name", None))
        self.label_10.setText(_translate("editDetailsWindow", "Edit User Details", None))

