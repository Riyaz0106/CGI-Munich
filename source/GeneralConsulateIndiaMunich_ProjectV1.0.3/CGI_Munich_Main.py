# Developer: Shaik Riyaz
# Created for: CGI Munich

from PyQt5 import QtCore, QtGui, QtWidgets

from CGI_Munich_Receipt import Ui_MainWindow
from CGI_Munich_Report import Ui_ReportWindow
from CGI_Munich_excgrate import Ui_ExchangeWindow
from CGI_Munich_Refund import Ui_RefundWindow
from CGI_Munich_Receipt_Database import Ui_ReceiptDataWindow
from CGI_Munich_Country_Database import Ui_CountryDataWindow
from CGI_Munich_Services_Database import Ui_ServicesDataWindow
from CGI_Munich_Find_Receipt import Ui_FindReceiptDialogBox
from CGI_Munich_About import Ui_AboutDialog as Ui_AboutWindow
from CGI_Munich_Version import Ui_VersionDialog as Ui_VersionWindow


class Ui_StartWindow(object):

    def __init__(self):
        self.d = None
        self.w = None

    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(1300, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartWindow.sizePolicy().hasHeightForWidth())
        StartWindow.setSizePolicy(sizePolicy)
        StartWindow.setMinimumSize(QtCore.QSize(1300, 690))
        StartWindow.setMaximumSize(QtCore.QSize(1300, 690))
        StartWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Main_Logo.setGeometry(QtCore.QRect(100, 110, 1100, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Logo.sizePolicy().hasHeightForWidth())
        self.Main_Logo.setSizePolicy(sizePolicy)
        self.Main_Logo.setMaximumSize(QtCore.QSize(1100, 1000))
        self.Main_Logo.setScaledContents(True)
        self.Main_Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_Logo.setObjectName("Main_Logo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QtCore.QRect(10, 590, 1281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QtCore.QRect(10, 0, 1281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QtCore.QRect(0, 10, 20, 591))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QtCore.QRect(1280, 10, 20, 591))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.login_status = QtWidgets.QLabel(self.centralwidget)
        self.login_status.setObjectName(u"login_status")
        self.login_status.setGeometry(QtCore.QRect(1200, 620, 100, 20))
        font = QtGui.QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.login_status.setFont(font)
        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 26))
        self.menubar.setObjectName("menubar")
        self.menuPrint = QtWidgets.QMenu(self.menubar)
        self.menuPrint.setObjectName("menuPrint")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        StartWindow.setMenuBar(self.menubar)

        self.actionEditDataBase = self.menuDatabase.addMenu("Edit Database")
        self.actionServDataBase = QtWidgets.QAction(StartWindow)
        self.actionServDataBase.setObjectName("actionServDataBase")
        self.actionNatDataBase = QtWidgets.QAction(StartWindow)
        self.actionNatDataBase.setObjectName("actionNatDataBase")
        self.actionRecDataBase = QtWidgets.QAction(StartWindow)
        self.actionRecDataBase.setObjectName("actionRecDataBase")
        self.menuReceipt = self.menuPrint.addMenu("Print Receipt")
        self.actionPayment = QtWidgets.QAction(StartWindow)
        self.actionPayment.setObjectName("actionPayment")
        self.actionRefund = QtWidgets.QAction(StartWindow)
        self.actionRefund.setObjectName("actionRefund")
        self.actionReport = QtWidgets.QAction(StartWindow)
        self.actionReport.setObjectName("actionReport")
        self.actionsyncExchg = QtWidgets.QAction(StartWindow)
        self.actionsyncExchg.setObjectName("actionsyncExchg")
        self.actionAbout = QtWidgets.QAction(StartWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionVersion = QtWidgets.QAction(StartWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.exit_btn = QtWidgets.QAction(StartWindow)
        self.exit_btn.setObjectName("exit_btn")
        self.menuPrint.addAction(self.actionReport)
        self.menuPrint.addAction(self.exit_btn)
        self.menuReceipt.addAction(self.actionPayment)
        self.menuReceipt.addAction(self.actionRefund)
        self.menuDatabase.addAction(self.actionsyncExchg)
        self.actionEditDataBase.addAction(self.actionNatDataBase)
        self.actionEditDataBase.addAction(self.actionRecDataBase)
        self.actionEditDataBase.addAction(self.actionServDataBase)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuPrint.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

        self.actionPayment.triggered.connect(self.openReceiptWindow)
        self.actionRefund.triggered.connect(self.openRefundWindow)

        self.actionReport.triggered.connect(self.openReportWindow)

        self.actionsyncExchg.triggered.connect(self.openExchangeRateWindow)

        self.actionRecDataBase.triggered.connect(self.openReceiptDatabaseWindow)

        self.actionNatDataBase.triggered.connect(self.openCountryDatabaseWindow)

        self.actionServDataBase.triggered.connect(self.openServicesDatabaseWindow)

        self.actionAbout.triggered.connect(self.openAboutWindow)

        self.actionVersion.triggered.connect(self.openVersionWindow)

        self.exit_btn.triggered.connect(StartWindow.close)

    def openReceiptWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

    def openRefundWindow(self):
        if self.w is None:
            self.window = QtWidgets.QMainWindow()
            self.rui = Ui_RefundWindow()
            self.w = self.window
            self.rui.setupUi(self.w)

        if self.d is None:
            self.FindReceiptDialogBox = QtWidgets.QDialog()
            self.findui = Ui_FindReceiptDialogBox()
            self.d = self.FindReceiptDialogBox
            self.findui.setupUi(self.d)
            self.findui.select_btn.clicked.connect(self.dummy)

        # Function Calls
        self.w.show()
        self.d.show()

    def dummy(self):
        self.w.showNormal()
        records = self.findui.send_receiptdata()
        self.rui.fetchreceipt(records)

    def openReportWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReportWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

    def openExchangeRateWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ExchangeWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

    def openReceiptDatabaseWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReceiptDataWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

    def openCountryDatabaseWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CountryDataWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

    def openServicesDatabaseWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ServicesDataWindow()
        self.ui.setupUi(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()

    def openAboutWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.exec_()

    def openVersionWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_VersionWindow()
        self.ui.setupUi(self.window)
        self.window.exec_()

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "CGI Munich"))
        self.Main_Logo.setText(_translate("StartWindow", "<html><head/><body><p>"
                                                         "<img src=\"./assets/template1_logo.png\"/>"
                                                         "</p></body></html>"))
        self.login_status.setText(_translate("StartWindow", "Logged in..."))
        self.menuPrint.setTitle(_translate("StartWindow", "Print"))
        self.menuDatabase.setTitle(_translate("StartWindow", "Edit"))
        self.menuHelp.setTitle(_translate("StartWindow", "Help"))
        self.actionReport.setText(_translate("StartWindow", "Print Report"))
        self.actionsyncExchg.setText(_translate("StartWindow", "Synchronize Exchange Rate"))
        self.actionPayment.setText(_translate("StartWindow", "Payment Receipt"))
        self.actionRefund.setText(_translate("StartWindow", "Refund Receipt"))
        self.actionNatDataBase.setText(_translate("StartWindow", "Nationality Database"))
        self.actionRecDataBase.setText(_translate("StartWindow", "Receipt Database"))
        self.actionServDataBase.setText(_translate("StartWindow", "Services Database"))
        self.actionAbout.setText(_translate("StartWindow", "About"))
        self.actionVersion.setText(_translate("StartWindow", "Version"))
        self.exit_btn.setText(_translate("StartWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())
