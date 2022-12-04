# Developer: Shaik Riyaz
# Created for: GCI Munich

import time
import pandas as pd
from datetime import date, datetime
from PyQt5 import QtCore, QtGui, QtWidgets

import db_utils as db_conn
import Message_DialogBox as DialogBox


class Ui_ExchangeWindow(object):

    def __init__(self):
        self.selectedbutton = ""
        self.currenttime = None

    def setupUi(self, ExchangeWindow):
        ExchangeWindow.setObjectName("ExchangeWindow")
        ExchangeWindow.setEnabled(True)
        ExchangeWindow.resize(800, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExchangeWindow.sizePolicy().hasHeightForWidth())
        ExchangeWindow.setSizePolicy(sizePolicy)
        ExchangeWindow.setMinimumSize(QtCore.QSize(800, 850))
        ExchangeWindow.setMaximumSize(QtCore.QSize(800, 850))
        font = QtGui.QFont()
        font.setFamily("Arial")
        ExchangeWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ExchangeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 110, 781, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 350, 781, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 10, 20, 811))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(780, 10, 20, 811))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.sync_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sync_btn.setGeometry(QtCore.QRect(200, 300, 391, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.sync_btn.setFont(font)
        self.sync_btn.setObjectName("sync_btn")
        self.rate_edit = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rate_edit.setGeometry(QtCore.QRect(410, 210, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.rate_edit.setFont(font)
        self.rate_edit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.rate_edit.setMaximum(10000.0)
        self.rate_edit.setDecimals(3)
        self.rate_edit.setObjectName("rate_edit")
        self.rate_lbl = QtWidgets.QLabel(self.centralwidget)
        self.rate_lbl.setGeometry(QtCore.QRect(240, 210, 161, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.rate_lbl.setFont(font)
        self.rate_lbl.setObjectName("rate_lbl")
        self.logo_lbl = QtWidgets.QLabel(self.centralwidget)
        self.logo_lbl.setGeometry(QtCore.QRect(200, 10, 451, 101))
        self.logo_lbl.setObjectName("logo_lbl")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: ExchangeWindow.close())
        self.exit_btn.setGeometry(QtCore.QRect(630, 770, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(20, 770, 150, 40))
        self.del_btn.setObjectName("del_btn")
        self.del_btn.setFont(font)
        self.email_id = QtWidgets.QLabel(self.centralwidget)
        self.email_id.setGeometry(QtCore.QRect(270, 90, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.email_id.setFont(font)
        self.email_id.setStyleSheet("color: rgb(81, 81, 81);")
        self.email_id.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.email_id.setObjectName("email_id")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, -10, 781, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.month_entry = QtWidgets.QSpinBox(self.centralwidget)
        self.month_entry.setGeometry(QtCore.QRect(210, 130, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.month_entry.setFont(font)
        self.month_entry.setMinimum(1)
        self.month_entry.setMaximum(12)
        self.month_entry.setObjectName("month_entry")
        self.year_entry = QtWidgets.QSpinBox(self.centralwidget)
        self.year_entry.setGeometry(QtCore.QRect(520, 130, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.year_entry.setFont(font)
        self.year_entry.setMinimum(1997)
        self.year_entry.setMaximum(9999)
        self.year_entry.setObjectName("year_entry")
        self.month_label = QtWidgets.QLabel(self.centralwidget)
        self.month_label.setGeometry(QtCore.QRect(130, 130, 71, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.month_label.setFont(font)
        self.month_label.setObjectName("month_label")
        self.year_label = QtWidgets.QLabel(self.centralwidget)
        self.year_label.setGeometry(QtCore.QRect(460, 130, 55, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.year_label.setFont(font)
        self.year_label.setObjectName("year_label")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 810, 781, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QtCore.QRect(10, 0, 781, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.exchange_table = QtWidgets.QTableWidget(self.centralwidget)
        self.exchange_table.setGeometry(QtCore.QRect(15, 371, 770, 390))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exchange_table.sizePolicy().hasHeightForWidth())
        self.exchange_table.setSizePolicy(sizePolicy)
        self.exchange_table.setMinimumSize(QtCore.QSize(770, 390))
        self.exchange_table.setMaximumSize(QtCore.QSize(770, 390))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.exchange_table.setFont(font)
        self.exchange_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.exchange_table.setObjectName("exchange_table")
        self.exchange_table.setColumnCount(4)
        self.exchange_table.setRowCount(0)
        self.exchange_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.exchange_table.setAlternatingRowColors(True)

        self.exchange_table.setColumnWidth(0, 150)
        self.exchange_table.setColumnWidth(1, 100)
        self.exchange_table.setColumnWidth(2, 100)
        self.exchange_table.setColumnWidth(3, 395)

        horizontalheader = self.exchange_table.horizontalHeader()
        horizontalheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        horizontalheader.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

        verticalheader = self.exchange_table.verticalHeader()
        verticalheader.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.exchange_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.exchange_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.exchange_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.exchange_table.setHorizontalHeaderItem(3, item)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 191, 80))
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
        font.setBold(False)
        self.date_entry.setFont(font)
        self.date_entry.setText("")
        self.date_entry.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.date_entry.setObjectName("date_entry")
        self.horizontalLayout.addWidget(self.date_entry)
        ExchangeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ExchangeWindow)
        self.statusbar.setObjectName("statusbar")
        ExchangeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ExchangeWindow)
        QtCore.QMetaObject.connectSlotsByName(ExchangeWindow)

        # Function Calls
        self.date_assign()
        self.load_echange_rate_table()
        self.sync_btn.clicked.connect(self.save_exchangerate)
        self.del_btn.clicked.connect(self.delete_exchangerate)

    # Date assign
    def date_assign(self):
        self.date_entry.setText(str(date.today()))

    def load_echange_rate_table(self):
        self.exchange_table.setRowCount(0)
        find_query = "SELECT * FROM exchange_rate "
        records = db_conn.fetch_rows(find_query, None)
        if records:
            df = pd.DataFrame(records)
            df.columns = ['Rate', 'Month', 'Year', 'Created Date', 'Created Time']

            paymentseconds = df['Created Time'].dt.total_seconds()
            df['Created Time'] = self.convert_time(paymentseconds).values

            self.exchange_table.setRowCount(len(records))
            i = 0
            for index, row in df.iterrows():
                self.exchange_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row['Rate'])))
                if row['Month'] < 10:
                    self.exchange_table.setItem(i, 1, QtWidgets.QTableWidgetItem('0'+str(row['Month'])))
                else:
                    self.exchange_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row['Month'])))
                self.exchange_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row['Year'])))
                self.exchange_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row['Created Date']) + ":" + str(row['Created Time'])))
                i += 1
            self.exchange_table.update()
            self.exchange_table.sortItems(1, QtCore.Qt.AscendingOrder)
            self.exchange_table.sortItems(2, QtCore.Qt.AscendingOrder)
        else:
            DialogBox.infodialog("No data available in the exchange rate database.")

    def save_exchangerate(self):
        self.selectedbutton = ""

        if self.rate_edit.value() > 0:
            warningdialog = DialogBox.warningdialog("Are you sure you want to add/update this exchange rate to database?", True)
            warningdialog.buttonClicked.connect(self.msgbtn)
            warningdialog.exec_()

            if self.selectedbutton == "Yes":
                now = datetime.now()
                self.currenttime = now.strftime("%H:%M:%S")

                find_query = "SELECT month FROM exchange_rate WHERE month = %s AND year = %s"
                records = db_conn.fetch_rows(find_query, (self.month_entry.value(), self.year_entry.value(),))

                if not records:
                    query = """INSERT INTO `exchange_rate`
                                (`rate`, `month`, `year`, `created_date`, `created_time`) 
                                VALUES (%s, %s, %s, %s, %s)"""
                    values = (self.rate_edit.value(), self.month_entry.value(), self.year_entry.value(), self.date_entry.text(),
                              self.currenttime)

                else:
                    query = """UPDATE exchange_rate SET 
                                rate = %s,
                                created_date = %s,
                                created_time = %s
                                WHERE month LIKE %s and year LIKE %s"""
                    values = (self.rate_edit.value(), self.date_entry.text(), self.currenttime, self.month_entry.value(), self.year_entry.value())

                records = db_conn.insert_rows(query, values)
                if records:
                    self.load_echange_rate_table()
                    DialogBox.infodialog("Exchange Rate synchronized successfully.")
                else:
                    DialogBox.errordialog("Exchange Rate synchronization failed.")
        else:
            DialogBox.errordialog("Exchange rate should be greater than 0.")

    def delete_exchangerate(self):
        self.selectedbutton = ""

        if self.exchange_table.selectedItems():
            warningdialog = DialogBox.warningdialog("Are you sure you want to delete this exchange rate from database?", True)
            warningdialog.buttonClicked.connect(self.msgbtn)
            warningdialog.exec_()

            if self.selectedbutton == "Yes":
                selected_row = self.exchange_table.currentRow()
                month = self.exchange_table.item(selected_row, 1).text()
                year = self.exchange_table.item(selected_row, 2).text()

                query = "DELETE FROM exchange_rate WHERE month = %s and year = %s"
                delete_ind = db_conn.delete_rows(query, (month, year,))
                if delete_ind:
                    self.load_echange_rate_table()
                    DialogBox.infodialog("Exchange Rate deleted successfully from database.")
                else:
                    DialogBox.errordialog("Failed to delete Exchange Rate from database.")
        else:
            DialogBox.errordialog("Please select a row from the table that you want to delete.")

    def convert_time(self, seconds):
        mlist = []
        for i in seconds:
            mlist.append(time.strftime("%H:%M:%S", time.gmtime(i)))

        df = pd.DataFrame({'Time': mlist})

        return df['Time']

    def msgbtn(self, i):
        if i.text() == "&Yes":
            self.selectedbutton = "Yes"

    def retranslateUi(self, ExchangeWindow):
        _translate = QtCore.QCoreApplication.translate
        ExchangeWindow.setWindowTitle(_translate("ExchangeWindow", "Synchronize Exchnage Rate"))
        self.sync_btn.setText(_translate("ExchangeWindow", "Synchronize"))
        self.rate_lbl.setText(_translate("ExchangeWindow", "Exchange Rate:"))
        self.logo_lbl.setText(_translate("ExchangeWindow", "<html><head/><body><p>"
                                                           "<img src=\"./assets/Munich_logo.png\"/>"
                                                           "</p></body></html>"))
        self.exit_btn.setText(_translate("ExchangeWindow", "Exit"))
        self.del_btn.setText(_translate("ExchangeWindow", "Delete"))
        self.email_id.setText(_translate("ExchangeWindow", "Website: cgimunich.gov.in"))
        self.month_label.setText(_translate("ExchangeWindow", "Month:"))
        self.year_label.setText(_translate("ExchangeWindow", "Year:"))
        item = self.exchange_table.horizontalHeaderItem(0)
        item.setText(_translate("ExchangeWindow", "Rate"))
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item = self.exchange_table.horizontalHeaderItem(1)
        item.setText(_translate("ExchangeWindow", "Month"))
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item = self.exchange_table.horizontalHeaderItem(2)
        item.setText(_translate("ExchangeWindow", "Year"))
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item = self.exchange_table.horizontalHeaderItem(3)
        item.setText(_translate("ExchangeWindow", "Created on"))
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.date_lbl.setText(_translate("ExchangeWindow", "Date:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ExchangeWindow = QtWidgets.QMainWindow()
    ui = Ui_ExchangeWindow()
    ui.setupUi(ExchangeWindow)
    ExchangeWindow.show()
    sys.exit(app.exec_())
