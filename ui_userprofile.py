# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userprofile.ui'
#
# Created: Mon Jan  1 14:43:30 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userWindow(object):
    def setupUi(self, userWindow):
        userWindow.setObjectName("userWindow")
        userWindow.resize(972, 496)
        userWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(userWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.resetPinButton = QtWidgets.QPushButton(userWindow)
        self.resetPinButton.setMinimumSize(QtCore.QSize(400, 0))
        self.resetPinButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.resetPinButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resetPinButton.setObjectName("resetPinButton")
        self.gridLayout.addWidget(self.resetPinButton, 8, 1, 1, 1)
        self.welcomeLabel = QtWidgets.QLabel(userWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        self.welcomeLabel.setStyleSheet("*{font: 75 26pt \"Noto Sans\"}")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.gridLayout.addWidget(self.welcomeLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.inventoryButton = QtWidgets.QPushButton(userWindow)
        self.inventoryButton.setMinimumSize(QtCore.QSize(400, 0))
        self.inventoryButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.inventoryButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.inventoryButton.setObjectName("inventoryButton")
        self.gridLayout.addWidget(self.inventoryButton, 4, 1, 1, 1)
        self.requestButton = QtWidgets.QPushButton(userWindow)
        self.requestButton.setMinimumSize(QtCore.QSize(400, 0))
        self.requestButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.requestButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon.fromTheme("save")
        self.requestButton.setIcon(icon)
        self.requestButton.setObjectName("requestButton")
        self.gridLayout.addWidget(self.requestButton, 6, 1, 1, 1)
        self.editDetailsButton = QtWidgets.QPushButton(userWindow)
        self.editDetailsButton.setMinimumSize(QtCore.QSize(400, 0))
        self.editDetailsButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.editDetailsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.editDetailsButton.setObjectName("editDetailsButton")
        self.gridLayout.addWidget(self.editDetailsButton, 7, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.cartButton = QtWidgets.QPushButton(userWindow)
        self.cartButton.setMinimumSize(QtCore.QSize(400, 0))
        self.cartButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.cartButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cartButton.setObjectName("cartButton")
        self.gridLayout.addWidget(self.cartButton, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.profilePic = QtWidgets.QLabel(userWindow)
        self.profilePic.setMinimumSize(QtCore.QSize(75, 75))
        self.profilePic.setMaximumSize(QtCore.QSize(200, 200))
        self.profilePic.setText("")
        self.profilePic.setPixmap(QtGui.QPixmap("images/index.png"))
        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName("profilePic")
        self.gridLayout.addWidget(self.profilePic, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.logoutButton = QtWidgets.QPushButton(userWindow)
        self.logoutButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutButton.setIcon(icon)
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout.addWidget(self.logoutButton, 9, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)
        userWindow.setTabOrder(self.inventoryButton, self.cartButton)
        userWindow.setTabOrder(self.cartButton, self.requestButton)
        userWindow.setTabOrder(self.requestButton, self.editDetailsButton)
        userWindow.setTabOrder(self.editDetailsButton, self.resetPinButton)
        userWindow.setTabOrder(self.resetPinButton, self.logoutButton)

    def retranslateUi(self, userWindow):
        _translate = QtCore.QCoreApplication.translate
        userWindow.setWindowTitle(_translate("userWindow", "Dialog"))
        self.resetPinButton.setText(_translate("userWindow", "Reset PIN"))
        self.welcomeLabel.setText(_translate("userWindow", "Welcome, ARCUser"))
        self.inventoryButton.setText(_translate("userWindow", "Inventory"))
        self.requestButton.setText(_translate("userWindow", "Purchase Request"))
        self.editDetailsButton.setText(_translate("userWindow", "Edit Details"))
        self.cartButton.setText(_translate("userWindow", "View Cart"))
        self.logoutButton.setText(_translate("userWindow", "Logout"))

