# Developer: Shaik Riyaz
# Created for: CGI Munich

import pandas as pd
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

import db_utils as db_conn
import Message_DialogBox as DialogBox


class Ui_CountryDataWindow(object):

    def __init__(self):
        self.selectedbutton = ""

    def setupUi(self, CountryDataWindow):
        CountryDataWindow.setObjectName("CountryDataWindow")
        CountryDataWindow.resize(1020, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CountryDataWindow.sizePolicy().hasHeightForWidth())
        CountryDataWindow.setSizePolicy(sizePolicy)
        CountryDataWindow.setMinimumSize(QtCore.QSize(1020, 850))
        CountryDataWindow.setMaximumSize(QtCore.QSize(1020, 850))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        CountryDataWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CountryDataWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 10, 501, 71))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.email_id = QtWidgets.QLabel(self.centralwidget)
        self.email_id.setGeometry(QtCore.QRect(350, 80, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.email_id.setFont(font)
        self.email_id.setStyleSheet("color: rgb(81, 81, 81);")
        self.email_id.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.email_id.setObjectName("email_id")
        self.ctry_name_edt = QtWidgets.QLineEdit(self.centralwidget)
        self.ctry_name_edt.setEnabled(True)
        self.ctry_name_edt.setGeometry(QtCore.QRect(180, 140, 641, 40))
        self.ctry_name_edt.setObjectName("ctry_name_edt")
        reg_ex = QtCore.QRegExp("^[A-Za-z\s]+$")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.ctry_name_edt)
        self.ctry_name_edt.setValidator(input_validator)
        self.ctry_name_lbl = QtWidgets.QLabel(self.centralwidget)
        self.ctry_name_lbl.setGeometry(QtCore.QRect(20, 140, 151, 40))
        self.ctry_name_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ctry_name_lbl.setObjectName("ctry_name_lbl")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: CountryDataWindow.close())
        self.exit_btn.setGeometry(QtCore.QRect(850, 750, 150, 40))
        self.exit_btn.setObjectName("exit_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(850, 140, 150, 40))
        self.add_btn.setObjectName("add_btn")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(20, 750, 150, 40))
        self.del_btn.setObjectName("del_btn")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 100, 1001, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 20, 791))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(10, 0, 1001, 20))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1000, 10, 20, 791))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(10, 200, 1001, 20))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(10, 790, 1001, 20))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.country_table = QtWidgets.QTableWidget(self.centralwidget)
        self.country_table.setGeometry(QtCore.QRect(15, 290, 990, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_table.sizePolicy().hasHeightForWidth())
        self.country_table.setSizePolicy(sizePolicy)
        self.country_table.setMinimumSize(QtCore.QSize(990, 450))
        self.country_table.setMaximumSize(QtCore.QSize(990, 450))
        self.country_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.country_table.setObjectName("country_table")
        self.country_table.setColumnCount(1)
        self.country_table.setRowCount(0)
        self.country_table.setAlternatingRowColors(True)

        self.country_table.setColumnWidth(0, 1000)

        horizontalheader = self.country_table.horizontalHeader()
        horizontalheader.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)

        verticalheader = self.country_table.verticalHeader()
        verticalheader.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        item.setFont(font)
        self.country_table.setHorizontalHeaderItem(0, item)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.country_table.setFont(font)

        self.srch_country_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.srch_country_entry.setObjectName("srch_country_entry")
        self.srch_country_entry.setGeometry(QtCore.QRect(15, 230, 391, 50))

        CountryDataWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CountryDataWindow)
        self.statusbar.setObjectName("statusbar")
        CountryDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CountryDataWindow)
        QtCore.QMetaObject.connectSlotsByName(CountryDataWindow)

        # Function Calls
        self.date_assign()
        self.load_country_table()
        self.srch_country_entry.textChanged.connect(self.filter_country_table)
        self.add_btn.clicked.connect(self.save_country)
        self.del_btn.clicked.connect(self.delete_country)

    # Date assign
    def date_assign(self):
        self.date_entry.setText(str(date.today()))

    def load_country_table(self):
        self.country_table.setRowCount(0)
        find_query = "SELECT * FROM nationality"
        records = db_conn.fetch_rows(find_query, None)
        if records:
            df = pd.DataFrame(records)
            df.columns = ['SNo.', 'Country Name']

            self.country_table.setRowCount(len(records))
            i = 0
            for index, row in df.iterrows():
                self.country_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row['Country Name'])))
                i += 1

            self.country_table.update()
            self.country_table.sortItems(1, QtCore.Qt.AscendingOrder)
        else:
            DialogBox.errordialog("No data available in the country database.")

    def filter_country_table(self):
        name = self.srch_country_entry.text().lower()
        for row in range(self.country_table.rowCount()):
            item = self.country_table.item(row, 0)
            # if the search is *not* in the item's text *do not hide* the row
            self.country_table.setRowHidden(row, name not in item.text().lower())

    def save_country(self):
        self.selectedbutton = ""

        if self.ctry_name_edt.text().replace(" ", "") != "":
            warningdialog = DialogBox.warningdialog("Are you sure you want to add/update this country to database?", True)
            warningdialog.buttonClicked.connect(self.msgbtn)
            warningdialog.exec_()

            if self.selectedbutton == "Yes":
                find_query = "SELECT name FROM nationality WHERE name LIKE %s"
                records = db_conn.fetch_rows(find_query, (self.ctry_name_edt.text(),))
                if not records:
                    query = """INSERT INTO `nationality` (`name`) VALUES (%s)"""
                    values = (self.ctry_name_edt.text(),)

                    records = db_conn.insert_rows(query, values)
                    if records:
                        self.load_country_table()
                        self.ctry_name_edt.setText("")
                        DialogBox.infodialog("Country successfully added to database.")
                    else:
                        DialogBox.errordialog("Failed to add country in database.")
                else:
                    DialogBox.errordialog("Failed to add country in database. "
                                          "This country already exists in the database")
        else:
            DialogBox.errordialog("Country name field is blank. Please enter a valid country name.")

    def delete_country(self):
        self.selectedbutton = ""

        if self.country_table.selectedItems():
            warningdialog = DialogBox.warningdialog("Are you sure you want to delete this country from database?", True)
            warningdialog.buttonClicked.connect(self.msgbtn)
            warningdialog.exec_()

            if self.selectedbutton == "Yes":
                selected_row = self.country_table.currentRow()
                country_name = self.country_table.item(selected_row, 0).text()

                query = "DELETE FROM nationality WHERE name LIKE %s"
                delete_ind = db_conn.delete_rows(query, (country_name,))
                if delete_ind:
                    self.load_country_table()
                    DialogBox.infodialog("Country deleted successfully from database.")
                else:
                    DialogBox.errordialog("Failed to delete country from database.")
        else:
            DialogBox.errordialog("Please select a row from the table that you want to delete.")

    def msgbtn(self, i):
        if i.text() == "&Yes":
            self.selectedbutton = "Yes"

    def retranslateUi(self, CountryDataWindow):
        _translate = QtCore.QCoreApplication.translate
        CountryDataWindow.setWindowTitle(_translate("CountryDataWindow", "Nationality Database"))
        self.date_lbl.setText(_translate("CountryDataWindow", "Date:"))
        self.label_10.setText(_translate("CountryDataWindow", "<html><head/><body><p>"
                                                              "<img src=\"./assets/Munich_logo.png\"/>"
                                                              "</p></body></html>"))
        self.email_id.setText(_translate("CountryDataWindow", "Website: cgimunich.gov.in"))
        self.ctry_name_lbl.setText(_translate("CountryDataWindow", "Country Name:"))
        self.exit_btn.setText(_translate("CountryDataWindow", "Exit"))
        self.add_btn.setText(_translate("CountryDataWindow", "Add"))
        self.del_btn.setText(_translate("CountryDataWindow", "Delete"))
        self.srch_country_entry.setPlaceholderText(_translate("CountryDataWindow", "Search"))
        self.ctry_name_edt.setPlaceholderText(_translate("CountryDataWindow", "Enter Country Name"))
        item = self.country_table.horizontalHeaderItem(0)
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        item.setText(_translate("CountryDataWindow", "Country Name"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CountryDataWindow = QtWidgets.QMainWindow()
    ui = Ui_CountryDataWindow()
    ui.setupUi(CountryDataWindow)
    CountryDataWindow.show()
    sys.exit(app.exec_())
