# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Upload(object):
    def setupUi(self, Upload):
        if not Upload.objectName():
            Upload.setObjectName(u"Upload")
        Upload.resize(728, 527)
        Upload.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.verticalLayout = QVBoxLayout(Upload)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttons_frame = QFrame(Upload)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(0, 80))
        self.buttons_frame.setMaximumSize(QSize(16777215, 80))
        self.buttons_frame.setFrameShape(QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_frame = QFrame(self.buttons_frame)
        self.select_frame.setObjectName(u"select_frame")
        self.select_frame.setMaximumSize(QSize(100, 16777215))
        self.select_frame.setFrameShape(QFrame.NoFrame)
        self.select_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.select_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_button = QPushButton(self.select_frame)
        self.select_button.setObjectName(u"select_button")
        self.select_button.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.select_button)


        self.horizontalLayout.addWidget(self.select_frame)

        self.filename_frame = QFrame(self.buttons_frame)
        self.filename_frame.setObjectName(u"filename_frame")
        self.filename_frame.setFrameShape(QFrame.NoFrame)
        self.filename_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.filename_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.filename_label = QLabel(self.filename_frame)
        self.filename_label.setObjectName(u"filename_label")
        self.filename_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_4.addWidget(self.filename_label)


        self.horizontalLayout.addWidget(self.filename_frame)

        self.upload_frame = QFrame(self.buttons_frame)
        self.upload_frame.setObjectName(u"upload_frame")
        self.upload_frame.setMaximumSize(QSize(100, 16777215))
        self.upload_frame.setFrameShape(QFrame.NoFrame)
        self.upload_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.upload_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.upload_button = QPushButton(self.upload_frame)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.upload_button)


        self.horizontalLayout.addWidget(self.upload_frame)

        self.logout_frame = QFrame(self.buttons_frame)
        self.logout_frame.setObjectName(u"logout_frame")
        self.logout_frame.setMinimumSize(QSize(80, 0))
        self.logout_frame.setMaximumSize(QSize(80, 16777215))
        self.logout_frame.setFrameShape(QFrame.NoFrame)
        self.logout_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.logout_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.logout_button = QPushButton(self.logout_frame)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"color: white;")

        self.horizontalLayout_11.addWidget(self.logout_button)


        self.horizontalLayout.addWidget(self.logout_frame)


        self.verticalLayout.addWidget(self.buttons_frame)

        self.content_frame = QFrame(Upload)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.upload_scrollArea = QScrollArea(self.content_frame)
        self.upload_scrollArea.setObjectName(u"upload_scrollArea")
        self.upload_scrollArea.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QFrame {\n"
"	\n"
"	background-color: rgb(68, 68, 68);\n"
"}")
        self.upload_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 710, 426))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.upload_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.upload_scrollArea)


        self.verticalLayout.addWidget(self.content_frame)


        self.retranslateUi(Upload)

        QMetaObject.connectSlotsByName(Upload)
    # setupUi

    def retranslateUi(self, Upload):
        Upload.setWindowTitle(QCoreApplication.translate("Upload", u"Savefor - Upload", None))
        self.select_button.setText(QCoreApplication.translate("Upload", u"Select", None))
        self.filename_label.setText("")
        self.upload_button.setText(QCoreApplication.translate("Upload", u"Upload", None))
        self.logout_button.setText(QCoreApplication.translate("Upload", u"Logout", None))
    # retranslateUi

