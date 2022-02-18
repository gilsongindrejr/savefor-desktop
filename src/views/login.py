# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(607, 491)
        Login.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(Login)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(Login)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setFrameShape(QFrame.NoFrame)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.mid_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mid_left_frame = QFrame(self.mid_frame)
        self.mid_left_frame.setObjectName(u"mid_left_frame")
        self.mid_left_frame.setFrameShape(QFrame.NoFrame)
        self.mid_left_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.mid_left_frame)

        self.mid_center_frame = QFrame(self.mid_frame)
        self.mid_center_frame.setObjectName(u"mid_center_frame")
        self.mid_center_frame.setMinimumSize(QSize(250, 200))
        self.mid_center_frame.setMaximumSize(QSize(250, 200))
        self.mid_center_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(57, 57, 57);\n"
"}")
        self.mid_center_frame.setFrameShape(QFrame.NoFrame)
        self.mid_center_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mid_center_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.form_frame = QFrame(self.mid_center_frame)
        self.form_frame.setObjectName(u"form_frame")
        self.form_frame.setFrameShape(QFrame.NoFrame)
        self.form_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.form_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.username_label = QLabel(self.form_frame)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setStyleSheet(u"color: white;")

        self.verticalLayout_3.addWidget(self.username_label)

        self.username_lineEdit = QLineEdit(self.form_frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.username_lineEdit)

        self.password_label = QLabel(self.form_frame)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setStyleSheet(u"color: white;")

        self.verticalLayout_3.addWidget(self.password_label)

        self.password_lineEdit = QLineEdit(self.form_frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")

        self.verticalLayout_3.addWidget(self.password_lineEdit)


        self.verticalLayout_2.addWidget(self.form_frame)

        self.info_frame = QFrame(self.mid_center_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 10))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.info_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.info_label = QLabel(self.info_frame)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.info_label, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.info_frame)

        self.button_frame = QFrame(self.mid_center_frame)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setFrameShape(QFrame.NoFrame)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.login_button = QPushButton(self.button_frame)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMaximumSize(QSize(100, 16777215))
        self.login_button.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.login_button)


        self.verticalLayout_2.addWidget(self.button_frame)


        self.horizontalLayout.addWidget(self.mid_center_frame)

        self.mid_right_frame = QFrame(self.mid_frame)
        self.mid_right_frame.setObjectName(u"mid_right_frame")
        self.mid_right_frame.setFrameShape(QFrame.NoFrame)
        self.mid_right_frame.setFrameShadow(QFrame.Raised)
        self.mid_right_frame.setLineWidth(0)

        self.horizontalLayout.addWidget(self.mid_right_frame)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bot_frame = QFrame(Login)
        self.bot_frame.setObjectName(u"bot_frame")
        self.bot_frame.setFrameShape(QFrame.NoFrame)
        self.bot_frame.setFrameShadow(QFrame.Raised)
        self.bot_frame.setLineWidth(0)

        self.verticalLayout.addWidget(self.bot_frame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Savefor - Login", None))
        self.username_label.setText(QCoreApplication.translate("Login", u"Username", None))
        self.username_lineEdit.setText("")
        self.password_label.setText(QCoreApplication.translate("Login", u"Password", None))
        self.info_label.setText("")
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

