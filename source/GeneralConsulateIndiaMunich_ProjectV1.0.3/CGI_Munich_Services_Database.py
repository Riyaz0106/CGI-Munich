# Developer: Shaik Riyaz
# Created for: CGI Munich

import pandas as pd
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

import db_utils as db_conn
import Message_DialogBox as DialogBox


class Ui_ServicesDataWindow(object):
    def __init__(self):
        self.selectedbutton = ""

    def setupUi(self, ServicesDataWindow):
        ServicesDataWindow.setObjectName("ServicesDataWindow")
        ServicesDataWindow.resize(1020, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ServicesDataWindow.sizePolicy().hasHeightForWidth())
        ServicesDataWindow.setSizePolicy(sizePolicy)
        ServicesDataWindow.setMinimumSize(QtCore.QSize(1020, 950))
        ServicesDataWindow.setMaximumSize(QtCore.QSize(1020, 950))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        ServicesDataWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ServicesDataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(10, 908, 1001, 20))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(340, 870, 150, 40))
        self.del_btn.setObjectName("del_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(340, 870, 150, 40))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setEnabled(False)
        self.cancel_btn.setVisible(False)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 20, 911))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 100, 1001, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 10, 501, 71))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: ServicesDataWindow.close())
        self.exit_btn.setGeometry(QtCore.QRect(850, 870, 150, 40))
        self.exit_btn.setObjectName("exit_btn")
        self.services_table = QtWidgets.QTableWidget(self.centralwidget)
        self.services_table.setGeometry(QtCore.QRect(15, 450, 990, 410))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.services_table.sizePolicy().hasHeightForWidth())
        self.services_table.setSizePolicy(sizePolicy)
        self.services_table.setMinimumSize(QtCore.QSize(990, 410))
        self.services_table.setMaximumSize(QtCore.QSize(990, 410))
        self.services_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.services_table.setObjectName("services_table")
        self.services_table.setColumnCount(6)
        self.services_table.setRowCount(0)
        self.services_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.services_table.setAlternatingRowColors(True)

        self.services_table.setColumnWidth(0, 200)
        self.services_table.setColumnWidth(1, 300)
        self.services_table.setColumnWidth(2, 400)
        self.services_table.setColumnWidth(3, 200)
        self.services_table.setColumnWidth(4, 200)
        self.services_table.setColumnWidth(5, 1500)

        self.services_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        verticalheader = self.services_table.verticalHeader()
        verticalheader.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.services_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.services_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.services_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.services_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.services_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.services_table.setHorizontalHeaderItem(5, item)

        self.srch_srvc_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.srch_srvc_entry.setObjectName("srch_srvc_entry")
        self.srch_srvc_entry.setGeometry(QtCore.QRect(15, 390, 391, 50))

        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(10, 370, 1001, 20))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1000, 10, 20, 911))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(20, 870, 150, 40))
        self.add_btn.setObjectName("add_btn")
        self.edt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edt_btn.setObjectName("edt_btn")
        self.edt_btn.setGeometry(QtCore.QRect(180, 870, 150, 40))
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setEnabled(False)
        self.save_btn.setVisible(False)
        self.save_btn.setGeometry(QtCore.QRect(180, 870, 150, 40))
        self.email_id = QtWidgets.QLabel(self.centralwidget)
        self.email_id.setGeometry(QtCore.QRect(350, 80, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.email_id.setFont(font)
        self.email_id.setStyleSheet("color: rgb(81, 81, 81);")
        self.email_id.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email_id.setObjectName("email_id")
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
        self.date_entry.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date_entry.setObjectName("date_entry")
        self.horizontalLayout.addWidget(self.date_entry)
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(10, 0, 1001, 20))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.srvc_lbl = QtWidgets.QLabel(self.centralwidget)
        self.srvc_lbl.setGeometry(QtCore.QRect(10, 120, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.srvc_lbl.setFont(font)
        self.srvc_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.srvc_lbl.setObjectName("srvc_lbl")
        self.srvc_desc_entry = QtWidgets.QTextEdit(self.centralwidget)
        self.srvc_desc_entry.setEnabled(True)
        self.srvc_desc_entry.setGeometry(QtCore.QRect(120, 220, 871, 101))
        self.srvc_desc_entry.setObjectName("srvc_desc_entry")
        self.srvc_desc_entry.setEnabled(False)
        self.srvc_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.srvc_entry.setGeometry(QtCore.QRect(120, 120, 250, 40))
        self.srvc_entry.setText("")
        self.srvc_entry.setObjectName("srvc_entry")
        self.srvc_entry.setEnabled(False)
        self.srvc_type_cbx = QtWidgets.QComboBox(self.centralwidget)
        self.srvc_type_cbx.addItem("")
        self.srvc_type_cbx.setObjectName("srvc_type_cbx")
        self.srvc_type_cbx.setGeometry(QtCore.QRect(120, 170, 331, 40))
        self.srvc_type_cbx.setEditable(True)
        self.srvc_type_cbx.setEnabled(False)
        self.srvc_type_cbx.model().item(0).setEnabled(False)
        self.srvc_sub_cbx = QtWidgets.QComboBox(self.centralwidget)
        self.srvc_sub_cbx.addItem("")
        self.srvc_sub_cbx.setObjectName("srvc_sub_cbx")
        self.srvc_sub_cbx.setGeometry(QtCore.QRect(460, 170, 531, 40))
        self.srvc_sub_cbx.setEditable(True)
        self.srvc_sub_cbx.setEnabled(False)
        self.srvc_sub_cbx.model().item(0).setEnabled(False)
        self.fees_lbl = QtWidgets.QLabel(self.centralwidget)
        self.fees_lbl.setGeometry(QtCore.QRect(10, 330, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.fees_lbl.setFont(font)
        self.fees_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fees_lbl.setObjectName("fees_lbl")
        self.fees_entry = QtWidgets.QSpinBox(self.centralwidget)
        self.fees_entry.setEnabled(False)
        self.fees_entry.setGeometry(QtCore.QRect(120, 330, 150, 40))
        self.fees_entry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.fees_entry.setMaximum(9999)
        self.fees_entry.setObjectName("fees_entry")
        self.icwf_entry = QtWidgets.QSpinBox(self.centralwidget)
        self.icwf_entry.setEnabled(False)
        self.icwf_entry.setGeometry(QtCore.QRect(840, 330, 150, 40))
        self.icwf_entry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.icwf_entry.setMaximum(9999)
        self.icwf_entry.setObjectName("icwf_entry")
        self.icwf_lbl = QtWidgets.QLabel(self.centralwidget)
        self.icwf_lbl.setGeometry(QtCore.QRect(730, 330, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.icwf_lbl.setFont(font)
        self.icwf_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.icwf_lbl.setObjectName("icwf_lbl")
        ServicesDataWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ServicesDataWindow)
        self.statusbar.setObjectName("statusbar")
        ServicesDataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ServicesDataWindow)
        QtCore.QMetaObject.connectSlotsByName(ServicesDataWindow)

        # Function Calls
        self.date_assign()
        self.get_service_types()
        self.srvc_type_cbx.currentIndexChanged.connect(self.get_service_subtype)
        self.get_service_subtype(self.srvc_type_cbx.currentIndex())
        self.load_services_table()
        self.services_table.currentItemChanged.connect(self.initializefields)
        self.srch_srvc_entry.textChanged.connect(self.filter_services_table)
        self.add_btn.clicked.connect(self.add_Ui)
        self.save_btn.clicked.connect(self.save_service)
        self.edt_btn.clicked.connect(self.edit_Ui)
        self.del_btn.clicked.connect(self.delete_service)
        self.cancel_btn.clicked.connect(self.reset_Ui)

    # Date assign
    def date_assign(self):
        self.date_entry.setText(str(date.today()))

    # Get Service Type
    def get_service_types(self):
        items = []
        items1 = []

        selectquery = "SELECT sub_category, category FROM services"
        records = db_conn.fetch_rows(selectquery, None)
        if records:
            for row in records:
                items.append(row[0])
                items1.append(row[1])

            k = sorted(set(items1))
            serv_dict = dict(zip(items, items1))
            for i in k:
                final_key = []
                for key in serv_dict:
                    if i == serv_dict[key]:
                        final_key.append(key)
                self.srvc_type_cbx.addItem(i, final_key)

    # Generate service sub type based on service type
    def get_service_subtype(self, index):
        if self.srvc_type_cbx.currentText() != "":
            subType = self.srvc_type_cbx.itemData(index)
            if subType:
                self.srvc_sub_cbx.addItems(subType)

    def load_services_table(self):
        find_query = "SELECT * FROM services"
        records = db_conn.fetch_rows(find_query, None)
        if records:
            df = pd.DataFrame(records)
            df.columns = ['Service Code', 'Service Description', 'Service Charges', 'ICWF Charges', 'Service Type',
                          'Service SubType']

            self.services_table.setRowCount(len(records))
            i = 0
            for index, row in df.iterrows():
                self.services_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row['Service Code'])))
                self.services_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row['Service Type'])))
                self.services_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row['Service SubType'])))
                self.services_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row['Service Charges'])))
                self.services_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row['ICWF Charges'])))
                self.services_table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(row['Service Description'])))
                i += 1

            self.services_table.update()
            self.services_table.sortItems(0, QtCore.Qt.AscendingOrder)
            self.services_table.selectRow(0)
            self.initializefields()
        else:
            DialogBox.errordialog("No data available in the Services database.")

    def filter_services_table(self):
        name = self.srch_srvc_entry.text().lower()
        for row in range(self.services_table.rowCount()):
            item = self.services_table.item(row, 0)
            # if the search is *not* in the item's text *do not hide* the row
            self.services_table.setRowHidden(row, name not in item.text().lower())

    def initializefields(self):
        self.reset_Ui()
        selected_row = self.services_table.currentRow()
        service_code = self.services_table.item(selected_row, 0).text()
        service_type = self.services_table.item(selected_row, 1).text()
        service_subtype = self.services_table.item(selected_row, 2).text()
        service_desc = self.services_table.item(selected_row, 5).text()
        service_chrg = self.services_table.item(selected_row, 3).text()
        icwf_chrg = self.services_table.item(selected_row, 4).text()

        self.srvc_entry.setText(service_code)
        self.srvc_type_cbx.setCurrentText(service_type)
        self.srvc_sub_cbx.setCurrentText(service_subtype)
        self.srvc_desc_entry.setText(service_desc)
        self.fees_entry.setValue(int(service_chrg))
        self.icwf_entry.setValue(int(icwf_chrg))

    def save_service(self):
        self.selectedbutton = ""

        if self.srvc_entry.text() != "" and (self.srvc_type_cbx.currentText() != "" or self.srvc_type_cbx.currentText() != "Select Type"):
            warningdialog = DialogBox.warningdialog("Are you sure you want to add/update this service to database?", True)
            warningdialog.buttonClicked.connect(self.msgbtn)
            warningdialog.exec_()

            if self.selectedbutton == "Yes":
                find_query = "SELECT code FROM services WHERE code LIKE %s"
                records = db_conn.fetch_rows(find_query, (self.srvc_entry.text(),))
                if not records:
                    query = """INSERT INTO `services` (`code`, `description`, `charges`, `icwf`, `category`, `sub_category`) 
                            VALUES (%s, %s, %s, %s, %s, %s)"""
                    values = (self.srvc_entry.text(), self.srvc_desc_entry.toPlainText(), str(self.fees_entry.value()),
                              str(self.icwf_entry.value()), self.srvc_type_cbx.currentText(), self.srvc_sub_cbx.currentText())
                    msg = "Service successfully added to database!!!"
                    self.clear_Ui()
                else:
                    query = """UPDATE services SET
                                code = %s,
                                description = %s,
                                charges = %s,
                                icwf = %s,
                                category = %s,
                                sub_category = %s 
                                WHERE code LIKE %s"""
                    values = (self.srvc_entry.text(), self.srvc_desc_entry.toPlainText(), str(self.fees_entry.value()),
                              str(self.icwf_entry.value()), self.srvc_type_cbx.currentText(), self.srvc_sub_cbx.currentText(),
                              self.services_table.item(self.services_table.currentRow(), 0).text())
                    msg = "Service successfully updated to database"

                records = db_conn.insert_rows(query, values)
                if records:
                    self.load_services_table()
                    self.reset_Ui()
                    DialogBox.infodialog(msg)
                else:
                    DialogBox.errordialog("Failed to add Service in database.")
        else:
            DialogBox.errordialog("Service Code and Service Type fields cannot be blank.")

    def delete_service(self):
        self.selectedbutton = ""

        if self.services_table.selectedItems():
            warningdialog = DialogBox.warningdialog("Are you sure you want to delete this service from database?", True)
            warningdialog.buttonClicked.connect(self.msgbtn)
            warningdialog.exec_()

            if self.selectedbutton == "Yes":
                selected_row = self.services_table.currentRow()
                service_code = self.services_table.item(selected_row, 0).text()

                query = "DELETE FROM services WHERE code LIKE %s"
                delete_ind = db_conn.delete_rows(query, (service_code,))
                if delete_ind:
                    self.load_services_table()
                    DialogBox.infodialog("Service deleted successfully from database.")
                else:
                    DialogBox.errordialog("Failed to delete the service from database.")
        else:
            DialogBox.errordialog("Please select a row from the table that you want to delete.")

    def msgbtn(self, i):
        if i.text() == "&Yes":
            self.selectedbutton = "Yes"

    def add_Ui(self):
        self.clear_Ui()
        self.edit_fields()

    def edit_Ui(self):
        if self.services_table.selectedItems():
            self.edit_fields()
        else:
            DialogBox.errordialog("Please select a row from the table that you want to edit.")

    def edit_fields(self):
        self.srvc_entry.setEnabled(True)
        self.srvc_type_cbx.setEnabled(True)
        self.srvc_sub_cbx.setEnabled(True)
        self.srvc_desc_entry.setEnabled(True)
        self.fees_entry.setEnabled(True)
        self.icwf_entry.setEnabled(True)
        self.add_btn.setEnabled(False)
        self.edt_btn.setEnabled(False)
        self.edt_btn.setVisible(False)
        self.save_btn.setEnabled(True)
        self.save_btn.setVisible(True)
        self.del_btn.setEnabled(False)
        self.del_btn.setVisible(False)
        self.cancel_btn.setVisible(True)
        self.cancel_btn.setEnabled(True)

    def clear_Ui(self):
        self.srvc_entry.setText("")
        self.srvc_type_cbx.setCurrentIndex(0)
        self.srvc_sub_cbx.setCurrentIndex(0)
        self.srvc_desc_entry.setText("")
        self.fees_entry.setValue(0)
        self.icwf_entry.setValue(0)

    def reset_Ui(self):
        self.clear_Ui()
        self.add_btn.setEnabled(True)
        self.edt_btn.setEnabled(True)
        self.edt_btn.setVisible(True)
        self.del_btn.setEnabled(True)
        self.del_btn.setVisible(True)
        self.save_btn.setEnabled(False)
        self.save_btn.setVisible(False)
        self.cancel_btn.setVisible(False)
        self.cancel_btn.setEnabled(False)
        self.srvc_entry.setEnabled(False)
        self.srvc_type_cbx.setEnabled(False)
        self.srvc_sub_cbx.setEnabled(False)
        self.srvc_desc_entry.setEnabled(False)
        self.fees_entry.setEnabled(False)
        self.icwf_entry.setEnabled(False)

    def retranslateUi(self, ServicesDataWindow):
        _translate = QtCore.QCoreApplication.translate
        ServicesDataWindow.setWindowTitle(_translate("ServicesDataWindow", "Services Database"))
        self.del_btn.setText(_translate("ServicesDataWindow", "Delete"))
        self.cancel_btn.setText(_translate("ServicesDataWindow", "Cancel"))
        self.label_10.setText(_translate("ServicesDataWindow", "<html><head/><body><p>"
                                                               "<img src=\"./assets/Munich_logo.png\"/>"
                                                               "</p></body></html>"))
        self.exit_btn.setText(_translate("ServicesDataWindow", "Exit"))
        item = self.services_table.horizontalHeaderItem(0)
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setText(_translate("ServicesDataWindow", "Service Code"))
        item = self.services_table.horizontalHeaderItem(1)
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setText(_translate("ServicesDataWindow", "Service Type"))
        item = self.services_table.horizontalHeaderItem(2)
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setText(_translate("ServicesDataWindow", "Service SubType"))
        item = self.services_table.horizontalHeaderItem(3)
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setText(_translate("ServicesDataWindow", "Service Charges"))
        item = self.services_table.horizontalHeaderItem(4)
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setText(_translate("ServicesDataWindow", "ICWF Charges"))
        item = self.services_table.horizontalHeaderItem(5)
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setText(_translate("ServicesDataWindow", "Service Description"))
        self.add_btn.setText(_translate("ServicesDataWindow", "New"))
        self.edt_btn.setText(_translate("ServicesDataWindow", "Edit"))
        self.save_btn.setText(_translate("ServicesDataWindow", "Save"))
        self.email_id.setText(_translate("ServicesDataWindow", "Website: cgimunich.gov.in"))
        self.date_lbl.setText(_translate("ServicesDataWindow", "Date:"))
        self.srvc_lbl.setText(_translate("ServicesDataWindow", "Service:"))
        self.srvc_desc_entry.setPlaceholderText(_translate("ServicesDataWindow", "Description"))
        self.srvc_entry.setPlaceholderText(_translate("ServicesDataWindow", "Code"))
        self.srvc_sub_cbx.setPlaceholderText(_translate("ServicesDataWindow", "Sub Type"))
        self.srvc_type_cbx.setPlaceholderText(_translate("ServicesDataWindow", "Type"))
        self.fees_lbl.setText(_translate("ServicesDataWindow", "Fees:"))
        self.icwf_lbl.setText(_translate("ServicesDataWindow", "ICWF:"))
        self.srch_srvc_entry.setPlaceholderText(_translate("CountryDataWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServicesDataWindow = QtWidgets.QMainWindow()
    ui = Ui_ServicesDataWindow()
    ui.setupUi(ServicesDataWindow)
    ServicesDataWindow.show()
    sys.exit(app.exec_())
