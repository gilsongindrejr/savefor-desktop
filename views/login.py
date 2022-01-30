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


class Ui_UI_Login(object):
    def setupUi(self, UI_Login):
        if not UI_Login.objectName():
            UI_Login.setObjectName(u"UI_Login")
        UI_Login.resize(607, 491)
        UI_Login.setStyleSheet(u"background-color: rgb(122, 122, 122);")
        self.verticalLayout = QVBoxLayout(UI_Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(UI_Login)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(UI_Login)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.mid_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mid_left_frame = QFrame(self.mid_frame)
        self.mid_left_frame.setObjectName(u"mid_left_frame")
        self.mid_left_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_left_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.mid_left_frame)

        self.mid_center_frame = QFrame(self.mid_frame)
        self.mid_center_frame.setObjectName(u"mid_center_frame")
        self.mid_center_frame.setMinimumSize(QSize(250, 200))
        self.mid_center_frame.setMaximumSize(QSize(250, 200))
        self.mid_center_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(57, 57, 57);\n"
"}")
        self.mid_center_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_center_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mid_center_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.form_frame = QFrame(self.mid_center_frame)
        self.form_frame.setObjectName(u"form_frame")
        self.form_frame.setFrameShape(QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.form_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.username_label = QLabel(self.form_frame)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout_3.addWidget(self.username_label)

        self.username_lineEdit = QLineEdit(self.form_frame)
        self.username_lineEdit.setObjectName(u"username_lineEdit")

        self.verticalLayout_3.addWidget(self.username_lineEdit)

        self.password_label = QLabel(self.form_frame)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout_3.addWidget(self.password_label)

        self.password_lineEdit = QLineEdit(self.form_frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")

        self.verticalLayout_3.addWidget(self.password_lineEdit)


        self.verticalLayout_2.addWidget(self.form_frame)

        self.button_frame = QFrame(self.mid_center_frame)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.login_button = QPushButton(self.button_frame)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.login_button)


        self.verticalLayout_2.addWidget(self.button_frame)


        self.horizontalLayout.addWidget(self.mid_center_frame)

        self.mid_right_frame = QFrame(self.mid_frame)
        self.mid_right_frame.setObjectName(u"mid_right_frame")
        self.mid_right_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_right_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.mid_right_frame)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bot_frame = QFrame(UI_Login)
        self.bot_frame.setObjectName(u"bot_frame")
        self.bot_frame.setFrameShape(QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.bot_frame)


        self.retranslateUi(UI_Login)

        QMetaObject.connectSlotsByName(UI_Login)
    # setupUi

    def retranslateUi(self, UI_Login):
        UI_Login.setWindowTitle(QCoreApplication.translate("UI_Login", u"Savefor - Login", None))
        self.username_label.setText(QCoreApplication.translate("UI_Login", u"Username", None))
        self.username_lineEdit.setText("")
        self.password_label.setText(QCoreApplication.translate("UI_Login", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("UI_Login", u"Login", None))
    # retranslateUi

