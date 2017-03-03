#write top layouts by hand
from PyQt4 import QtCore, QtGui
import sys

from ui_mainwindow import Ui_splashScreen
from ui_userprofile import Ui_userWindow
from ui_resetpin import Ui_resetPinWindow
from ui_finger import Ui_loginWindow
from ui_requestitem import Ui_requestItemWindow
from ui_editdetails import Ui_editDetailsWindow
from ui_inventory import Ui_inventoryWindow
from ui_cart import Ui_cartWindow

from sql.user_details import user_info
from sql.reset_pin import resetPin
from sql.view_cart import view_cart
from sql.inventory import selectFromInventory
from sql.purchase import purchaseRequests

class userDetails():
    def __init__(self, _name = "ARC-User-X", _userId = 1, _isAdmin = True):
        self.name = _name
        self.userId = _userId
        self.isAdmin = _isAdmin

class mainWindow(QtGui.QWidget):
    def __init__(self, widget):
        super(mainWindow, self).__init__()

        self.windowWidget = widget
        self.windowWidget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n* {font: 16pt}\n")
        self.windowWidget.setWindowTitle("Smart Inventory Management System")
        self.windowWidget.resize(1280, 800)

        self.splashScreen = QtGui.QMainWindow()
        self.userProfile = QtGui.QDialog()
        self.resetPin = QtGui.QWidget()
        self.fingerprint = QtGui.QDialog()
        self.requestItem = QtGui.QWidget()
        self.editDetails = QtGui.QWidget()
        self.inventory = QtGui.QMainWindow()
        self.arcHeader = QtGui.QWidget()
        self.cart = QtGui.QWidget()
        self.finger = QtGui.QDialog()

        self.currentPage = 0
        self.previousPage = 0

        self.StackWidget = QtGui.QStackedWidget(self)
        self.HomeWidget = QtGui.QStackedWidget(self)
        self.screenWidget = QtGui.QWidget()

        self.setupSplashScreen()
        self.HomeWidget.addWidget(self.splashScreen)
        self.HomeWidget.addWidget(self.screenWidget)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.arcHeader)
        vbox.addWidget(self.StackWidget)
        self.screenWidget.setLayout(vbox)

        windowVBox = QtGui.QVBoxLayout()
        windowVBox.addWidget(self.HomeWidget)

        self.windowWidget.setLayout(windowVBox)

        self.HomeWidget.setCurrentIndex(0)
        self.StackWidget.setCurrentIndex(0)

    def setupHeaderWidget(self, widget):
        hbox = QtGui.QHBoxLayout()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        #setting up gui
        backButton = QtGui.QPushButton()
        backButton.setFlat(True)
        backButton.setIcon(icon)
        backButton.setIconSize(QtCore.QSize(48, 48))

        arcLogo = QtGui.QLabel()
        arcLogo.setMinimumSize(QtCore.QSize(0, 0))
        arcLogo.setMaximumSize(QtCore.QSize(175, 150))
        arcLogo.setPixmap(QtGui.QPixmap("images/arclogo.png"))
        arcLogo.setScaledContents(True)

        userWidget = QtGui.QWidget()
        userHBox = QtGui.QHBoxLayout()
        userIcon = QtGui.QLabel()
        comboBox = QtGui.QComboBox()

        userIcon.setMinimumSize(QtCore.QSize(0, 40))
        userIcon.setMaximumSize(QtCore.QSize(50, 50))
        userIcon.setPixmap(QtGui.QPixmap("images/index.png"))
        userIcon.setScaledContents(True)
        comboBox.setMinimumSize(QtCore.QSize(200, 40))
        comboBox.setMaximumSize(QtCore.QSize(300, 16777215))

        comboBox.addItem(self.user.name)

        if self.user.isAdmin == True:
            comboBox.addItem("Admin Panel")

        comboBox.activated.connect(self.handleComboBox)

        userHBox.addWidget(userIcon)
        userHBox.addWidget(comboBox)
        userWidget.setLayout(userHBox)

        hbox.addWidget(backButton)
        hbox.addWidget(arcLogo)
        hbox.addWidget(userWidget)
        hbox.setAlignment(backButton, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        hbox.setAlignment(arcLogo, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        hbox.setAlignment(userWidget, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        widget.setLayout(hbox)
        widget.setStyleSheet("QPushButton {padding: 10px}\nQWidget {background-color: white}\n")

        backButton.clicked.connect(self.goBack)

    def handleComboBox(self, val):
        if val == 1:
            print 'This functionality is not added yet!'
            self.windowWidget.close()
#            self.HomeWidget.setCurrentIndex(0)
#            self.user = userDetails() #for resetting things

    def createStackedPages(self):
        self.setupWindows()
        self.StackWidget.addWidget(self.userProfile)
        self.StackWidget.addWidget(self.resetPin)
        self.StackWidget.addWidget(self.fingerprint)
        self.StackWidget.addWidget(self.requestItem)
        self.StackWidget.addWidget(self.editDetails)
        self.StackWidget.addWidget(self.inventory)
        self.StackWidget.addWidget(self.cart)

    def setupSplashScreen(self):
        Ui_splashScreen().setupUi(self.splashScreen)
        button = self.splashScreen.findChild(QtGui.QPushButton, "pushButton")

        button.clicked.connect(lambda: self.unlockScreen())

    def setupFingerprint(self):
        Ui_loginWindow.setupUi(self.finger)

    def setupUserProfile(self):
        Ui_userWindow().setupUi(self.userProfile)
        inventoryButton = self.userProfile.findChild(QtGui.QPushButton, "inventoryButton")
        editDetailsButton = self.userProfile.findChild(QtGui.QPushButton, "editDetailsButton")
        requestButton = self.userProfile.findChild(QtGui.QPushButton, "requestButton")
        resetPinButton = self.userProfile.findChild(QtGui.QPushButton, "resetPinButton")
        cartButton = self.userProfile.findChild(QtGui.QPushButton, "cartButton")
        lockButton = self.userProfile.findChild(QtGui.QPushButton, "lockButton")
        logoutButton = self.userProfile.findChild(QtGui.QPushButton, "logoutButton")
        welcomeLabel = self.userProfile.findChild(QtGui.QLabel, "welcomeLabel")

        inventoryButton.clicked.connect(lambda: self.launchWindow(5))
        editDetailsButton.clicked.connect(lambda: self.launchWindow(4))
        requestButton.clicked.connect(lambda: self.launchWindow(3))
        resetPinButton.clicked.connect(lambda: self.launchWindow(1))
        cartButton.clicked.connect(lambda: self.launchWindow(6))

        logoutButton.clicked.connect(lambda: self.logoutUser())

        welcomeLabel.setText("Welcome, " + self.user.name)

    def setupResetPin(self):
        Ui_resetPinWindow().setupUi(self.resetPin)
        buttonBox = self.resetPin.findChild(QtGui.QDialogButtonBox, "buttonBox")
        currentPwd = self.resetPin.findChild(QtGui.QLineEdit, "currentPwd")
        newPwd = self.resetPin.findChild(QtGui.QLineEdit, "newPwd")

        buttonBox.accepted.connect(lambda: self.execResetPin(currentPwd.text(), newPwd.text()))
        buttonBox.rejected.connect(lambda: self.launchWindow(0))

    def execResetPin(self, currentPwd, newPwd):
        resetPinObject = resetPin()
        result = resetPinObject.compareEnteredPin(self.user.userId, currentPwd, newPwd)
        if result == 0:
            self.showSuccessDialog('Wrong PIN!')
        else:
            self.showSuccessDialog('PIN successfully updated!')
            self.launchWindow(0)

    def setupFinger(self):
        Ui_loginWindow().setupUi(self.finger)

    def setupRequestItem(self):
        Ui_requestItemWindow().setupUi(self.requestItem)
        project = self.requestItem.findChild(QtGui.QLineEdit, "project")
        item = self.requestItem.findChild(QtGui.QLineEdit, "item")
        price = self.requestItem.findChild(QtGui.QLineEdit, "price")
        requestItemButton = self.requestItem.findChild(QtGui.QPushButton, "requestItemButton")

        purchaseRequest = purchaseRequests()
        requestItemButton.clicked.connect(lambda: purchaseRequest.addToTable(self.user.userId, \
                                    str(project.text()), str(price.text()), \
                                    str(item.text()), 1000))

    def setupEditDetails(self):
        Ui_editDetailsWindow().setupUi(self.editDetails)

        buttonBox = self.editDetails.findChild(QtGui.QDialogButtonBox, "buttonBox")
        buttonBox.rejected.connect(lambda: self.launchWindow(0))
        buttonBox.accepted.connect(lambda: self.saveUserDetails(self.user.userId))
        buttonBox.accepted.connect(lambda: self.showSuccessDialog('Database successfully updated!'))
        buttonBox.accepted.connect(lambda: self.launchWindow(0))

        userInfo = user_info()
        userData = userInfo.get_user_info(self.user.userId)

        name = self.editDetails.findChild(QtGui.QLineEdit, "name")
        phoneCall = self.editDetails.findChild(QtGui.QLineEdit, "phoneCall")
        phoneWhatsApp = self.editDetails.findChild(QtGui.QLineEdit, "phoneWhatsApp")
        roomNumber = self.editDetails.findChild(QtGui.QLineEdit, "roomNumber")
        email = self.editDetails.findChild(QtGui.QLineEdit, "email")

        name.setText(userData[0])
        phoneCall.setText(userData[1])
        phoneWhatsApp.setText(userData[2])
        roomNumber.setText(userData[3])
        email.setText(userData[4])

    def setupInventory(self):
        Ui_inventoryWindow().setupUi(self.inventory)

        self.inventoryDb = selectFromInventory()
        self.categoryList = self.inventoryDb.getCatagories()
        self.categoryModel = QtGui.QStandardItemModel()
        self.itemListModel = QtGui.QStandardItemModel()

        cartButton = self.inventory.findChild(QtGui.QPushButton, "cartButton")
        categoryView = self.inventory.findChild(QtGui.QListView, "categoryView")
        itemView = self.inventory.findChild(QtGui.QListView, "itemListView")
        addToCartButton = self.inventory.findChild(QtGui.QPushButton, "addToCartButton")
        qtySpinBox = self.inventory.findChild(QtGui.QSpinBox, "qtySpinBox")
        partQty = self.inventory.findChild(QtGui.QLabel, "partQty")

        categoryView.setModel(self.categoryModel)
        itemView.setModel(self.itemListModel)

        for item in self.categoryList:
            self.categoryModel.appendRow(QtGui.QStandardItem(item))

        categoryView.clicked.connect(self.updateInventoryItemList)
        itemView.clicked.connect(self.updateInventoryItemInfo)
        cartButton.clicked.connect(lambda: self.launchWindow(6))
        addToCartButton.clicked.connect(lambda: self.addToCartAction(itemView, qtySpinBox, partQty))

    def setupCart(self):
        Ui_cartWindow().setupUi(self.cart)

        self.viewCart = view_cart()
        self.model = QtGui.QStandardItemModel()

        listView = self.cart.findChild(QtGui.QListView, "listView")
        buttonBox = self.cart.findChild(QtGui.QDialogButtonBox, "buttonBox")
        openInventory = self.cart.findChild(QtGui.QPushButton, "openInventory")
        removeCartButton = self.cart.findChild(QtGui.QPushButton, "removeCartButton")
        partID = self.cart.findChild(QtGui.QLabel, "partID")
        partQty = self.cart.findChild(QtGui.QLabel, "partQty")

        listView.setModel(self.model)
        self.updateViewCart()

        removeCartButton.clicked.connect(
                                        lambda: (
                                        self.viewCart.removeFromCart(self.user.userId, int(str(partID.text()))),
                                        self.updateViewCart()))
        listView.clicked.connect(self.displayCartItem)
        openInventory.clicked.connect(lambda: self.launchWindow(5))

    def logoutUser(self):
        self.windowWidget.close()
        self.windowWidget = QtGui.QWidget()
        mainWindow(self.windowWidget)
        self.windowWidget.show()

    def saveUserDetails(self, userId):
        name = self.editDetails.findChild(QtGui.QLineEdit, "name")
        phoneCall = self.editDetails.findChild(QtGui.QLineEdit, "phoneCall")
        phoneWhatsApp = self.editDetails.findChild(QtGui.QLineEdit, "phoneWhatsApp")
        roomNumber = self.editDetails.findChild(QtGui.QLineEdit, "roomNumber")
        email = self.editDetails.findChild(QtGui.QLineEdit, "email")

        userInfo = user_info()
        userInfo.update_user_info([str(name.text()), str(phoneCall.text()), \
                                str(phoneWhatsApp.text()), str(roomNumber.text()), \
                                str(email.text())], userId)

    def addToCartAction(self, itemView, qtySpinBox, partQty):
        itemName = '\'' + itemView.selectedIndexes()[0].data().toString() + '\''
        itemId = self.inventoryDb.getItemId(itemName)
        self.inventoryDb.addToCart(self.user.userId, self.user.name, itemId, qtySpinBox.value(), '123')
        qty = int(str(partQty.text()))-qtySpinBox.value()
        if qty < 0:
            qty = 0
        partQty.setText(str(qty))

    def updateInventoryItemList(self, id):
        self.itemListModel.clear()
        itemList = self.inventoryDb.getItems(id.row())
        for item in itemList:
            self.itemListModel.appendRow(QtGui.QStandardItem(item))

    def updateInventoryItemInfo(self, id):
        partName = self.inventory.findChild(QtGui.QLabel, "partName")
        partCategory = self.inventory.findChild(QtGui.QLabel, "partCategory")
        partID = self.inventory.findChild(QtGui.QLabel, "partID")
        partShelf = self.inventory.findChild(QtGui.QLabel, "partShelf")
        partBox = self.inventory.findChild(QtGui.QLabel, "partBox")
        partQty = self.inventory.findChild(QtGui.QLabel, "partQty")

        itemDetails = self.inventoryDb.getItemInfo(id.row())
        partName.setText(itemDetails[1])
        partCategory.setText(itemDetails[5])
        partID.setText(str(itemDetails[0]))
        partShelf.setText(str(itemDetails[3]))
        partBox.setText(str(itemDetails[4]))
        partQty.setText(str(itemDetails[6]))

    def updateViewCart(self):
        self.model.clear()
        itemList = self.viewCart.getItemList(self.user.userId)
        for item in itemList:
            self.model.appendRow(QtGui.QStandardItem(item))

    def displayCartItem(self, itemId):
        partName = self.cart.findChild(QtGui.QLabel, "partName")
        partCategory = self.cart.findChild(QtGui.QLabel, "partCategory")
        partID = self.cart.findChild(QtGui.QLabel, "partID")
        partShelf = self.cart.findChild(QtGui.QLabel, "partShelf")
        partBox = self.cart.findChild(QtGui.QLabel, "partBox")
        partQty = self.cart.findChild(QtGui.QLabel, "partQty")

        itemName = '\'' + itemId.data().toString() + '\''
        itemId = self.inventoryDb.getItemId(itemName)

        itemDetails = self.viewCart.getItemInfo(self.user.userId, itemId)
        partName.setText(itemDetails[1])
        partCategory.setText(itemDetails[5])
        partID.setText(str(itemDetails[0]))
        partShelf.setText(str(itemDetails[3]))
        partBox.setText(str(itemDetails[4]))
        partQty.setText(str(itemDetails[6]))

    def comboAction(self, x):
        if (x == 1):
            self.launchWindow(0)

    def launchWindow(self, value):
        self.previousPage = self.currentPage
        self.StackWidget.setCurrentIndex(value)
        self.currentPage = value
        self.updateViewCart()

    def goBack(self):
        self.StackWidget.setCurrentIndex(0)
        #have to build a history tree for proper back button

    def unlockScreen(self):
        self.user = userDetails()
        self.createStackedPages()
        self.HomeWidget.setCurrentIndex(1)

    def setupWindows(self):
        self.setupHeaderWidget(self.arcHeader)
        self.setupUserProfile()
        self.setupResetPin()
#        self.setupFingerprint()
        self.setupRequestItem()
        self.setupEditDetails()
        self.setupInventory()
        self.setupCart()

    def showSuccessDialog(self, text):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('images/arclogo.png'))

    widget = QtGui.QWidget()
    prog = mainWindow(widget)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
