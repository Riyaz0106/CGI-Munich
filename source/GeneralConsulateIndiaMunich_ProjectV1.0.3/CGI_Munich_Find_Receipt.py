# Developer: Shaik Riyaz
# Created for: CGI Munich

import time
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

import db_utils as db_conn
import Message_DialogBox as DialogBox


class Ui_FindReceiptDialogBox(object):
    def __init__(self):
        self.receipt_table_df = None

    def setupUi(self, FindReceiptDialogBox):
        FindReceiptDialogBox.setObjectName("FindReceiptDialogBox")
        FindReceiptDialogBox.resize(1020, 660)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FindReceiptDialogBox.sizePolicy().hasHeightForWidth())
        FindReceiptDialogBox.setSizePolicy(sizePolicy)
        FindReceiptDialogBox.setMinimumSize(QtCore.QSize(1020, 660))
        FindReceiptDialogBox.setMaximumSize(QtCore.QSize(1020, 660))
        self.line_7 = QtWidgets.QFrame(FindReceiptDialogBox)
        self.line_7.setGeometry(QtCore.QRect(10, 640, 1001, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_16 = QtWidgets.QFrame(FindReceiptDialogBox)
        self.line_16.setGeometry(QtCore.QRect(10, 0, 1001, 20))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.cancel_btn = QtWidgets.QPushButton(FindReceiptDialogBox, clicked=lambda: FindReceiptDialogBox.close())
        self.cancel_btn.setGeometry(QtCore.QRect(580, 600, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.line_6 = QtWidgets.QFrame(FindReceiptDialogBox)
        self.line_6.setGeometry(QtCore.QRect(10, 80, 1001, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.receipt_table = QtWidgets.QTableWidget(FindReceiptDialogBox)
        self.receipt_table.setEnabled(True)
        self.receipt_table.setGeometry(QtCore.QRect(10, 90, 1000, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receipt_table.sizePolicy().hasHeightForWidth())
        self.receipt_table.setSizePolicy(sizePolicy)
        self.receipt_table.setMinimumSize(QtCore.QSize(1000, 500))
        self.receipt_table.setMaximumSize(QtCore.QSize(1000, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.receipt_table.setFont(font)
        self.receipt_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.receipt_table.setObjectName("receipt_table")
        self.receipt_table.setColumnCount(8)
        self.receipt_table.setRowCount(0)
        self.receipt_table.verticalHeader().hide()
        self.receipt_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.receipt_table.setAlternatingRowColors(True)

        self.receipt_table.setColumnWidth(0, 150)
        self.receipt_table.setColumnWidth(1, 400)
        self.receipt_table.setColumnWidth(2, 200)
        self.receipt_table.setColumnWidth(3, 150)
        self.receipt_table.setColumnWidth(4, 800)
        self.receipt_table.setColumnWidth(5, 200)
        self.receipt_table.setColumnWidth(6, 200)
        self.receipt_table.setColumnWidth(7, 200)

        horizontalheader = self.receipt_table.horizontalHeader()
        horizontalheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(5, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(6, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(7, QtWidgets.QHeaderView.Fixed)

        verticalheader = self.receipt_table.verticalHeader()
        verticalheader.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.receipt_table.setHorizontalHeaderItem(7, item)
        self.rcpt_lbl = QtWidgets.QLabel(FindReceiptDialogBox)
        self.rcpt_lbl.setGeometry(QtCore.QRect(10, 30, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.rcpt_lbl.setFont(font)
        self.rcpt_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rcpt_lbl.setObjectName("rcpt_lbl")
        self.line_2 = QtWidgets.QFrame(FindReceiptDialogBox)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 20, 640))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(FindReceiptDialogBox)
        self.line_3.setGeometry(QtCore.QRect(1000, 10, 20, 640))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.select_btn = QtWidgets.QPushButton(FindReceiptDialogBox)
        self.select_btn.setGeometry(QtCore.QRect(300, 600, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.select_btn.setFont(font)
        self.select_btn.setObjectName("select_btn")
        self.srch_rcptno_edt = QtWidgets.QLineEdit(FindReceiptDialogBox)
        self.srch_rcptno_edt.setGeometry(QtCore.QRect(230, 30, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.srch_rcptno_edt.setFont(font)
        self.srch_rcptno_edt.setObjectName("srch_rcptno_edt")
        self.srch_btn = QtWidgets.QPushButton(FindReceiptDialogBox)
        self.srch_btn.setGeometry(QtCore.QRect(850, 30, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.srch_btn.setFont(font)
        self.srch_btn.setObjectName("srch_btn")

        self.retranslateUi(FindReceiptDialogBox)
        QtCore.QMetaObject.connectSlotsByName(FindReceiptDialogBox)

        self.load_receipt_table()
        self.srch_btn.clicked.connect(self.filter_receipt_table)

    def load_receipt_table(self):
        self.receipt_table.setRowCount(0)
        find_query = "Select receipt.*, services.description, services.category, services.sub_category," \
                     "IFNULL(refund_receipt.total_refund,0) FROM receipt " \
                     "INNER JOIN services ON receipt.service_code LIKE services.code " \
                     "LEFT OUTER JOIN refund_receipt ON refund_receipt.receipt_no LIKE receipt.refund_receipt_no"
        records = db_conn.fetch_rows(find_query, None)
        if records:
            self.receipt_table_df = records
            df = pd.DataFrame(records)
            df.columns = ['Receipt No.', 'Receipt Date', 'Receipt Time', 'Name', 'Nationality', 'Service Code',
                          'No of Docs', 'Transaction Type', 'Special Service', 'Gratis', 'Postal Express', 'Wave ICWF',
                          'Misc Amount', 'Misc Desc', 'Postal Charges', 'Fees', 'ICWF Charges', 'Total Amount',
                          'Refund Receipt No.', 'Service Description', 'Service Type', 'Service SubType',
                          'Total Refund Amount']

            paymentseconds = df['Receipt Time'].dt.total_seconds()
            df['Receipt Time'] = self.convert_time(paymentseconds).values

            self.receipt_table.setRowCount(len(records))
            i = 0
            for index, row in df.iterrows():
                self.receipt_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row['Receipt No.'])))
                self.receipt_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row['Name'])))
                self.receipt_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row['Nationality'])))
                self.receipt_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row['Service Type'])))
                self.receipt_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row['Service Description'])))
                self.receipt_table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(row['Total Amount'])))
                self.receipt_table.setItem(i, 6, QtWidgets.QTableWidgetItem(str(row['Receipt Date'])))
                self.receipt_table.setItem(i, 7, QtWidgets.QTableWidgetItem(str(row['Receipt Time'])))
                i += 1

            self.receipt_table.update()
            self.receipt_table.sortItems(0, QtCore.Qt.AscendingOrder)
        else:
            DialogBox.errordialog("No Receipts generated yet to process a refund.")

    def filter_receipt_table(self):
        flag = 0
        name = self.srch_rcptno_edt.text().lower()
        for row in range(self.receipt_table.rowCount()):
            item = self.receipt_table.item(row, 0)
            # if the search is *not* in the item's text *do not hide* the row
            if name not in item.text().lower():
                self.receipt_table.setRowHidden(row, True)
            else:
                flag = 1
        if flag != 1:
            DialogBox.infodialog("No Receipts generated yet.")

    def send_receiptdata(self):
        if self.receipt_table.selectedItems():
            selected_row = self.receipt_table.selectedItems()[0].row()
            receipt_no = self.receipt_table.item(selected_row, 0).text()
            for row in self.receipt_table_df:
                if str(row[0]) == receipt_no:
                    return row

    def convert_time(self, seconds):
        mlist = []
        for i in seconds:
            mlist.append(time.strftime("%H:%M:%S", time.gmtime(i)))

        df = pd.DataFrame({'Time': mlist})

        return df['Time']

    def retranslateUi(self, FindReceiptDialogBox):
        _translate = QtCore.QCoreApplication.translate
        FindReceiptDialogBox.setWindowTitle(_translate("FindReceiptDialogBox", "Find Receipt"))
        self.cancel_btn.setText(_translate("FindReceiptDialogBox", "Cancel"))
        item = self.receipt_table.horizontalHeaderItem(0)
        item.setText(_translate("FindReceiptDialogBox", "Receipt No."))
        item = self.receipt_table.horizontalHeaderItem(1)
        item.setText(_translate("FindReceiptDialogBox", "Name"))
        item = self.receipt_table.horizontalHeaderItem(2)
        item.setText(_translate("FindReceiptDialogBox", "Nationality"))
        item = self.receipt_table.horizontalHeaderItem(3)
        item.setText(_translate("FindReceiptDialogBox", "Service"))
        item = self.receipt_table.horizontalHeaderItem(4)
        item.setText(_translate("FindReceiptDialogBox", "Service Description"))
        item = self.receipt_table.horizontalHeaderItem(5)
        item.setText(_translate("FindReceiptDialogBox", "Total amount"))
        item = self.receipt_table.horizontalHeaderItem(6)
        item.setText(_translate("FindReceiptDialogBox", "Receipt Date"))
        item = self.receipt_table.horizontalHeaderItem(7)
        item.setText(_translate("FindReceiptDialogBox", "Receipt Time"))
        self.rcpt_lbl.setText(_translate("FindReceiptDialogBox", "Enter Receipt No:"))
        self.select_btn.setText(_translate("FindReceiptDialogBox", "Select"))
        self.srch_btn.setText(_translate("FindReceiptDialogBox", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindReceiptDialogBox = QtWidgets.QDialog()
    ui = Ui_FindReceiptDialogBox()
    ui.setupUi(FindReceiptDialogBox)
    FindReceiptDialogBox.show()
    sys.exit(app.exec_())
