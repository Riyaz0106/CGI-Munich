# Developer: Shaik Riyaz
# Created for: CGI Munich

from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

import db_utils as db_conn
import Message_DialogBox as DialogBox


class Ui_ReceiptDataWindow(object):
    def __init__(self):
        self.selectedbutton = ""

    def setupUi(self, ReceiptDataWindow):
        ReceiptDataWindow.setObjectName("ReceiptDataWindow")
        ReceiptDataWindow.resize(1020, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReceiptDataWindow.sizePolicy().hasHeightForWidth())
        ReceiptDataWindow.setSizePolicy(sizePolicy)
        ReceiptDataWindow.setMinimumSize(QtCore.QSize(1020, 850))
        ReceiptDataWindow.setMaximumSize(QtCore.QSize(1020, 850))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        ReceiptDataWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ReceiptDataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nat_view = QtWidgets.QLineEdit(self.centralwidget)
        self.nat_view.setEnabled(False)
        self.nat_view.setGeometry(QtCore.QRect(210, 230, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.nat_view.setFont(font)
        self.nat_view.setObjectName("nat_view")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(10, 0, 1001, 20))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.name_view = QtWidgets.QLineEdit(self.centralwidget)
        self.name_view.setEnabled(False)
        self.name_view.setGeometry(QtCore.QRect(210, 180, 611, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.name_view.setFont(font)
        self.name_view.setObjectName("name_view")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 100, 1001, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.trans_type_lbl = QtWidgets.QLabel(self.centralwidget)
        self.trans_type_lbl.setGeometry(QtCore.QRect(10, 390, 191, 40))
        self.trans_type_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.trans_type_lbl.setObjectName("trans_type_lbl")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: ReceiptDataWindow.close())
        self.exit_btn.setGeometry(QtCore.QRect(850, 740, 150, 40))
        self.exit_btn.setObjectName("exit_btn")
        self.trans_type_view = QtWidgets.QLineEdit(self.centralwidget)
        self.trans_type_view.setEnabled(False)
        self.trans_type_view.setGeometry(QtCore.QRect(210, 390, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.trans_type_view.setFont(font)
        self.trans_type_view.setObjectName("trans_type_view")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(990, 530, 20, 71))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.doc_lbl = QtWidgets.QLabel(self.centralwidget)
        self.doc_lbl.setGeometry(QtCore.QRect(569, 230, 131, 40))
        self.doc_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.doc_lbl.setObjectName("doc_lbl")
        self.docs_view = QtWidgets.QLineEdit(self.centralwidget)
        self.docs_view.setEnabled(False)
        self.docs_view.setGeometry(QtCore.QRect(710, 230, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.docs_view.setFont(font)
        self.docs_view.setObjectName("docs_view")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setEnabled(False)
        self.del_btn.setGeometry(QtCore.QRect(700, 740, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")
        self.spsrvc_view = QtWidgets.QLineEdit(self.centralwidget)
        self.spsrvc_view.setEnabled(False)
        self.spsrvc_view.setGeometry(QtCore.QRect(210, 440, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.spsrvc_view.setFont(font)
        self.spsrvc_view.setObjectName("spsrvc_view")
        self.total_lbl = QtWidgets.QLabel(self.centralwidget)
        self.total_lbl.setGeometry(QtCore.QRect(10, 610, 191, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.total_lbl.setFont(font)
        self.total_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.total_lbl.setObjectName("total_lbl")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 790, 1001, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 20, 791))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1000, 10, 20, 791))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.srvc_desc_view = QtWidgets.QLineEdit(self.centralwidget)
        self.srvc_desc_view.setEnabled(False)
        self.srvc_desc_view.setGeometry(QtCore.QRect(430, 290, 571, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.srvc_desc_view.setFont(font)
        self.srvc_desc_view.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.srvc_desc_view.setObjectName("srvc_desc_view")
        self.rcpt_lbl = QtWidgets.QLabel(self.centralwidget)
        self.rcpt_lbl.setGeometry(QtCore.QRect(10, 120, 191, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.rcpt_lbl.setFont(font)
        self.rcpt_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.rcpt_lbl.setObjectName("rcpt_lbl")
        self.nat_lbl = QtWidgets.QLabel(self.centralwidget)
        self.nat_lbl.setGeometry(QtCore.QRect(10, 230, 191, 40))
        self.nat_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.nat_lbl.setObjectName("nat_lbl")
        self.spsrvc_lbl = QtWidgets.QLabel(self.centralwidget)
        self.spsrvc_lbl.setGeometry(QtCore.QRect(10, 440, 191, 40))
        self.spsrvc_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.spsrvc_lbl.setObjectName("spsrvc_lbl")
        self.email_id = QtWidgets.QLabel(self.centralwidget)
        self.email_id.setGeometry(QtCore.QRect(300, 80, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.email_id.setFont(font)
        self.email_id.setStyleSheet("color: rgb(81, 81, 81);")
        self.email_id.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.email_id.setObjectName("email_id")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 270, 1001, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gratis_view = QtWidgets.QLineEdit(self.centralwidget)
        self.gratis_view.setEnabled(False)
        self.gratis_view.setGeometry(QtCore.QRect(210, 340, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.gratis_view.setFont(font)
        self.gratis_view.setObjectName("gratis_view")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(210, 10, 501, 71))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(650, 520, 351, 20))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(710, 19, 291, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.receipt_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.receipt_lbl.setFont(font)
        self.receipt_lbl.setObjectName("receipt_lbl")
        self.horizontalLayout_2.addWidget(self.receipt_lbl)
        self.rcpt_entry = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.rcpt_entry.setText("")
        self.rcpt_entry.setObjectName("rcpt_entry")
        self.horizontalLayout_2.addWidget(self.rcpt_entry)
        self.total_entry = QtWidgets.QSpinBox(self.centralwidget)
        self.total_entry.setEnabled(False)
        self.total_entry.setGeometry(QtCore.QRect(210, 610, 171, 41))
        self.total_entry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.total_entry.setMaximum(9999)
        self.total_entry.setObjectName("total_entry")
        self.other_entry = QtWidgets.QTextEdit(self.centralwidget)
        self.other_entry.setEnabled(False)
        self.other_entry.setGeometry(QtCore.QRect(210, 490, 391, 111))
        self.other_entry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.other_entry.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.other_entry.setObjectName("other_entry")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 186, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_lbl.sizePolicy().hasHeightForWidth())
        self.date_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.date_lbl.setFont(font)
        self.date_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.date_lbl.setObjectName("date_lbl")
        self.horizontalLayout.addWidget(self.date_lbl)
        self.date_entry = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_entry.sizePolicy().hasHeightForWidth())
        self.date_entry.setSizePolicy(sizePolicy)
        self.date_entry.setText("")
        self.date_entry.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.date_entry.setObjectName("date_entry")
        self.horizontalLayout.addWidget(self.date_entry)
        self.srch_btn = QtWidgets.QPushButton(self.centralwidget)
        self.srch_btn.setGeometry(QtCore.QRect(840, 170, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.srch_btn.setFont(font)
        self.srch_btn.setObjectName("srch_btn")
        self.srvc_view = QtWidgets.QLineEdit(self.centralwidget)
        self.srvc_view.setEnabled(False)
        self.srvc_view.setGeometry(QtCore.QRect(210, 290, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.srvc_view.setFont(font)
        self.srvc_view.setObjectName("srvc_view")
        self.other_lbl = QtWidgets.QLabel(self.centralwidget)
        self.other_lbl.setGeometry(QtCore.QRect(10, 490, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.other_lbl.setFont(font)
        self.other_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.other_lbl.setObjectName("other_lbl")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(650, 590, 351, 20))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gratis_lbl = QtWidgets.QLabel(self.centralwidget)
        self.gratis_lbl.setGeometry(QtCore.QRect(10, 340, 191, 40))
        self.gratis_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gratis_lbl.setObjectName("gratis_lbl")
        self.name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.name_lbl.setGeometry(QtCore.QRect(10, 180, 191, 40))
        self.name_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.name_lbl.setObjectName("name_lbl")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(640, 530, 20, 71))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.srvc_lbl = QtWidgets.QLabel(self.centralwidget)
        self.srvc_lbl.setGeometry(QtCore.QRect(10, 290, 191, 40))
        self.srvc_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.srvc_lbl.setObjectName("srvc_lbl")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(660, 540, 337, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.post_waveicf_layout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.post_waveicf_layout_2.setContentsMargins(0, 0, 0, 0)
        self.post_waveicf_layout_2.setObjectName("post_waveicf_layout_2")
        self.postExp_chk = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.postExp_chk.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.postExp_chk.setFont(font)
        self.postExp_chk.setObjectName("postExp_chk")
        self.post_waveicf_layout_2.addWidget(self.postExp_chk)
        self.waveicf_chk = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.waveicf_chk.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.waveicf_chk.setFont(font)
        self.waveicf_chk.setObjectName("waveicf_chk")
        self.post_waveicf_layout_2.addWidget(self.waveicf_chk)
        self.srch_rcptno_edt = QtWidgets.QLineEdit(self.centralwidget)
        self.srch_rcptno_edt.setGeometry(QtCore.QRect(210, 120, 300, 50))
        self.srch_rcptno_edt.setObjectName("srch_rcptno_edt")
        reg_ex = QtCore.QRegExp("[0-9]{7}[\w.-]{8,}$")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.srch_rcptno_edt)
        self.srch_rcptno_edt.setValidator(input_validator)
        self.rfnd_ind = QtWidgets.QCheckBox(self.centralwidget)
        self.rfnd_ind.setEnabled(False)
        self.rfnd_ind.setGeometry(QtCore.QRect(660, 340, 170, 40))
        self.rfnd_ind.setObjectName("rfnd_ind")
        ReceiptDataWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ReceiptDataWindow)
        self.statusbar.setObjectName("statusbar")
        ReceiptDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReceiptDataWindow)
        QtCore.QMetaObject.connectSlotsByName(ReceiptDataWindow)

        # Function Calls
        self.date_assign()
        self.srch_btn.clicked.connect(self.searchreceipt)
        self.del_btn.clicked.connect(self.deletereceipt)

    # Date assign
    def date_assign(self):
        self.date_entry.setText(str(date.today()))

    # Search receipt in database
    def searchreceipt(self):
        receipt_no = 0
        if self.srch_rcptno_edt.text() != "":
            if self.srch_rcptno_edt.text()[-1].isdigit():
                receipt_no = self.srch_rcptno_edt.text()
            else:
                find_query = "Select receipt_no FROM receipt WHERE refund_receipt_no LIKE %s LIMIT 1"
                records = db_conn.fetch_rows(find_query, (self.srch_rcptno_edt.text(),))
                if records:
                    for row in records:
                        receipt_no = row[0]

            errors = self.fetchreceipt(receipt_no)
            if errors != "":
                DialogBox.errordialog(errors)

        else:
            DialogBox.errordialog("Invalid Receipt Number. Please Enter a valid Receipt Number.")

    # Fetch receipt data
    def fetchreceipt(self, rcpt_no):
        self.clear_Ui()
        self.ref_rcpt_no = '0'
        msg = ""
        find_query = "Select receipt.*, services.description, services.category, " \
                     "IFNULL(refund_receipt.total_refund,0) FROM receipt " \
                     "INNER JOIN services ON receipt.service_code LIKE services.code " \
                     "LEFT OUTER JOIN refund_receipt ON refund_receipt.receipt_no LIKE receipt.refund_receipt_no " \
                     "WHERE receipt.receipt_no LIKE %s"
        records = db_conn.fetch_rows(find_query, (rcpt_no,))
        if records:
            for row in records:
                self.rcpt_entry.setText(self.srch_rcptno_edt.text())
                self.ref_rcpt_no = str(row[18])
                self.name_view.setText(row[3])
                self.nat_view.setText(row[4])
                self.docs_view.setText(str(row[6]))
                self.trans_type_view.setText(row[7])
                self.spsrvc_view.setText(row[8])
                self.gratis_view.setText(row[9])
                if row[10] != 0:
                    self.postExp_chk.setChecked(True)
                if row[11] != 0:
                    self.waveicf_chk.setChecked(True)
                self.other_entry.setText(row[13])
                if self.srch_rcptno_edt.text()[-1] == "R":
                    self.total_entry.setValue(row[21])
                    self.rfnd_ind.setChecked(True)
                else:
                    self.total_entry.setValue(row[17])
                self.srvc_view.setText(row[20])
                self.srvc_desc_view.setText(row[19])

            if self.ref_rcpt_no != "None" and (not self.rfnd_ind.isChecked()):
                self.del_btn.setEnabled(False)
                DialogBox.warningdialog("Transaction cannot be deleted.\n"
                                        "This Transaction is associted with a refund transaction\n"
                                        "(Receipt No: " + str(self.ref_rcpt_no) + ").\n\n" +
                                        "Delete the Refund transaction first to delete this transaction.")
            else:
                self.del_btn.setEnabled(True)

        else:
            msg = "Invalid Receipt Number. Please Enter a valid Receipt Number."
        return msg

    # Delete Receipt
    def deletereceipt(self):
        self.selectedbutton = ""

        warningdialog = DialogBox.warningdialog("Are you sure you want to delete this transaction from database?", True)
        warningdialog.buttonClicked.connect(self.msgbtn)
        warningdialog.exec_()

        if self.selectedbutton == "Yes":
            if self.rfnd_ind.isChecked():
                delete_query = "DELETE FROM refund_receipt WHERE receipt_no LIKE %s"
            else:
                delete_query = "DELETE FROM receipt WHERE receipt_no LIKE %s"

            delete_ind = db_conn.delete_rows(delete_query, (self.rcpt_entry.text(),))
            if delete_ind:
                DialogBox.infodialog("Transaction successfully deleted.")
                self.srch_rcptno_edt.setText("")
                self.clear_Ui()
            else:
                DialogBox.errordialog("Failed to delete this transaction.")

    def msgbtn(self, i):
        if i.text() == "&Yes":
            self.selectedbutton = "Yes"

    # Clear all data from fields
    def clear_Ui(self):
        self.rcpt_entry.setText("")
        self.name_view.setText("")
        self.docs_view.setText("")
        self.srvc_view.setText("")
        self.srvc_desc_view.setText("")
        self.nat_view.setText("")
        self.gratis_view.setText("")
        self.trans_type_view.setText("")
        self.spsrvc_view.setText("")
        self.other_entry.setText("")
        self.total_entry.setValue(0)
        self.reset_Ui()

    # Set all UI elements to it's default state
    def reset_Ui(self):
        self.rfnd_ind.setChecked(False)
        self.postExp_chk.setChecked(False)
        self.waveicf_chk.setChecked(False)
        self.del_btn.setEnabled(False)

    def retranslateUi(self, ReceiptDataWindow):
        _translate = QtCore.QCoreApplication.translate
        ReceiptDataWindow.setWindowTitle(_translate("ReceiptDataWindow", "Receipt Database"))
        self.trans_type_lbl.setText(_translate("ReceiptDataWindow", "Transaction Type:"))
        self.exit_btn.setText(_translate("ReceiptDataWindow", "Exit"))
        self.doc_lbl.setText(_translate("ReceiptDataWindow", "No. Docs:"))
        self.del_btn.setText(_translate("ReceiptDataWindow", "Delete"))
        self.total_lbl.setText(_translate("ReceiptDataWindow", "Total Amount:"))
        self.rcpt_lbl.setText(_translate("ReceiptDataWindow", "Enter Receipt No:"))
        self.nat_lbl.setText(_translate("ReceiptDataWindow", "Nationality:"))
        self.spsrvc_lbl.setText(_translate("ReceiptDataWindow", "Special Services:"))
        self.email_id.setText(_translate("ReceiptDataWindow", "Website: cgimunich.gov.in"))
        self.label_10.setText(_translate("ReceiptDataWindow", "<html><head/><body><p>"
                                                              "<img src=\"./assets/Munich_logo.png\"/>"
                                                              "</p></body></html>"))
        self.receipt_lbl.setText(_translate("ReceiptDataWindow", "Receipt No:"))
        self.date_lbl.setText(_translate("ReceiptDataWindow", "Date:"))
        self.srch_btn.setText(_translate("ReceiptDataWindow", "Search"))
        self.other_lbl.setText(_translate("ReceiptDataWindow", "Misc Description:"))
        self.gratis_lbl.setText(_translate("ReceiptDataWindow", "Gratis:"))
        self.name_lbl.setText(_translate("ReceiptDataWindow", "Name:"))
        self.srvc_lbl.setText(_translate("ReceiptDataWindow", "Service:"))
        self.postExp_chk.setText(_translate("ReceiptDataWindow", "Postal express"))
        self.waveicf_chk.setText(_translate("ReceiptDataWindow", "Wave ICWF"))
        self.rfnd_ind.setText(_translate("ReceiptDataWindow", "Refund"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ReceiptDataWindow = QtWidgets.QMainWindow()
    ui = Ui_ReceiptDataWindow()
    ui.setupUi(ReceiptDataWindow)
    ReceiptDataWindow.show()
    sys.exit(app.exec_())
