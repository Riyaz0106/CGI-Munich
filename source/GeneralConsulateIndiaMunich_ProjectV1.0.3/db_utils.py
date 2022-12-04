# Developer: Shaik Riyaz
# Created for: CGI Munich

import mysql.connector

import Message_DialogBox as DialogBox
from CGI_Munich_Database_Connection import ConnectDb


def fetch_rows(query, values):
    obj = ConnectDb()
    conn = obj.dbconn
    cursor = obj.dbcursor
    try:
        if conn.is_connected():
            # db_Info = conn.get_server_info()
            if values is not None:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            records = cursor.fetchall()
            return records
    except mysql.connector.Error as error:
        DialogBox.errordialog("Database Error {0}".format(error))
    finally:
        if conn.is_connected():
            obj.closedatabaseconnection()


def insert_rows(query, values):
    obj = ConnectDb()
    conn = obj.dbconn
    cursor = obj.dbcursor
    try:
        if conn.is_connected():
            # db_Info = conn.get_server_info()
            cursor.execute(query, values)
            conn.commit()
            return True
    except mysql.connector.Error as error:
        DialogBox.errordialog("Database Error {0}".format(error))
    finally:
        if conn.is_connected():
            obj.closedatabaseconnection()


def delete_rows(query, values):
    obj = ConnectDb()
    conn = obj.dbconn
    cursor = obj.dbcursor
    try:
        if conn.is_connected():
            # db_Info = conn.get_server_info()
            cursor.execute(query, values)
            conn.commit()
            return True
    except mysql.connector.Error as error:
        DialogBox.errordialog("Database Error {0}".format(error))
    finally:
        if conn.is_connected():
            obj.closedatabaseconnection()
