# Developer: Shaik Riyaz
# Created for: CGI Munich

from PyQt5 import QtWidgets


# Error Messages DialogBox
def errordialog(errmsg):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(errmsg)
    msg.setWindowTitle("Error")
    msg.exec_()


# Information Messages DialogBox
def infodialog(infomsg, object=False):
    if not object:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(infomsg)
        msg.setWindowTitle("Information")
        msg.exec_()
    else:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(infomsg)
        msg.setWindowTitle("Information")
        return msg


# Warning Messages DialogBox
def warningdialog(warnmsg, buttons=False):
    if not buttons:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(warnmsg)
        msg.setWindowTitle("Warning")
        msg.exec_()
    else:
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(warnmsg)
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        return msg


