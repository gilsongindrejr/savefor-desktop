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


class Ui_UI_Upload(object):
    def setupUi(self, UI_Upload):
        if not UI_Upload.objectName():
            UI_Upload.setObjectName(u"UI_Upload")
        UI_Upload.resize(728, 527)
        self.verticalLayout = QVBoxLayout(UI_Upload)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttons_frame = QFrame(UI_Upload)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(0, 80))
        self.buttons_frame.setMaximumSize(QSize(16777215, 80))
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_frame = QFrame(self.buttons_frame)
        self.select_frame.setObjectName(u"select_frame")
        self.select_frame.setMaximumSize(QSize(100, 16777215))
        self.select_frame.setFrameShape(QFrame.StyledPanel)
        self.select_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.select_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_button = QPushButton(self.select_frame)
        self.select_button.setObjectName(u"select_button")

        self.horizontalLayout_3.addWidget(self.select_button)


        self.horizontalLayout.addWidget(self.select_frame)

        self.filename_frame = QFrame(self.buttons_frame)
        self.filename_frame.setObjectName(u"filename_frame")
        self.filename_frame.setFrameShape(QFrame.StyledPanel)
        self.filename_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.filename_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.filename_label = QLabel(self.filename_frame)
        self.filename_label.setObjectName(u"filename_label")

        self.horizontalLayout_4.addWidget(self.filename_label)


        self.horizontalLayout.addWidget(self.filename_frame)

        self.upload_frame = QFrame(self.buttons_frame)
        self.upload_frame.setObjectName(u"upload_frame")
        self.upload_frame.setMaximumSize(QSize(100, 16777215))
        self.upload_frame.setFrameShape(QFrame.StyledPanel)
        self.upload_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.upload_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.upload_button = QPushButton(self.upload_frame)
        self.upload_button.setObjectName(u"upload_button")

        self.horizontalLayout_2.addWidget(self.upload_button)


        self.horizontalLayout.addWidget(self.upload_frame)


        self.verticalLayout.addWidget(self.buttons_frame)

        self.content_frame = QFrame(UI_Upload)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 708, 424))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.file_frame = QFrame(self.scrollAreaWidgetContents)
        self.file_frame.setObjectName(u"file_frame")
        self.file_frame.setMinimumSize(QSize(0, 80))
        self.file_frame.setMaximumSize(QSize(16777215, 80))
        self.file_frame.setFrameShape(QFrame.StyledPanel)
        self.file_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.file_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.file_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.sending_filename_label = QLabel(self.frame)
        self.sending_filename_label.setObjectName(u"sending_filename_label")

        self.horizontalLayout_7.addWidget(self.sending_filename_label)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.file_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 0))
        self.frame_2.setMaximumSize(QSize(150, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.time_label = QLabel(self.frame_2)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout_8.addWidget(self.time_label)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.file_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_10.addWidget(self.progressBar)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.file_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(80, 0))
        self.frame_4.setMaximumSize(QSize(80, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cancel_button = QPushButton(self.frame_4)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_9.addWidget(self.cancel_button)


        self.horizontalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.file_frame)

        self.upload_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.upload_scrollArea)


        self.verticalLayout.addWidget(self.content_frame)


        self.retranslateUi(UI_Upload)

        QMetaObject.connectSlotsByName(UI_Upload)
    # setupUi

    def retranslateUi(self, UI_Upload):
        UI_Upload.setWindowTitle(QCoreApplication.translate("UI_Upload", u"Savefor - Upload", None))
        self.select_button.setText(QCoreApplication.translate("UI_Upload", u"Select", None))
        self.filename_label.setText(QCoreApplication.translate("UI_Upload", u"test_file.txt", None))
        self.upload_button.setText(QCoreApplication.translate("UI_Upload", u"Upload", None))
        self.sending_filename_label.setText(QCoreApplication.translate("UI_Upload", u"test_file.txt", None))
        self.time_label.setText(QCoreApplication.translate("UI_Upload", u"TextLabel", None))
        self.cancel_button.setText(QCoreApplication.translate("UI_Upload", u"PushButton", None))
    # retranslateUi

