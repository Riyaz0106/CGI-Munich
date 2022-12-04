# Developer: Shaik Riyaz
# Created for: CGI Munich

import mysql.connector
from mysql.connector import errorcode

import Message_DialogBox as DialogBox


class ConnectDb:
    def __init__(self):
        self.dbconn, self.dbcursor = self.startdatabaseconnection()

    def startdatabaseconnection(self):
        try:
            conn = mysql.connector.connect(host='localhost', user='root', database='cgi_munich', password='root1234', port=3306)
            if conn.is_connected():
                # db_Info = conn.get_server_info()
                cursor = conn.cursor(buffered=True)
                return conn, cursor
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='root1234', port=3306)
                    if conn.is_connected():
                        # db_Info = conn.get_server_info()
                        cursor = conn.cursor(buffered=True)
                        return conn, cursor
                except mysql.connector.Error as error:
                    DialogBox.errordialog("Database Error {0}".format(error))
            else:
                DialogBox.errordialog("Database Error {0}".format(error))

    def closedatabaseconnection(self):
        if self.dbconn.is_connected():
            self.dbcursor.close()
            self.dbconn.close()
