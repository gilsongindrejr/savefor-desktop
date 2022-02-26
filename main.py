import os
import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QFrame, QHBoxLayout, QLabel, QProgressBar, \
    QPushButton, QButtonGroup, QSystemTrayIcon, QMenu, QAction
from PySide2.QtCore import QSize

from src.views.login import Ui_Login
from src.views.upload import Ui_Upload
from src.controllers.worker import Worker
from src.controllers.monitor import Monitor
from src.controllers.communication import Communicate
from src.controllers.authentication import login
from src.models.file import File


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('resources/images/icon.png'))
        
        # login window
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)

        # upload window
        self.ui_upload_window = QWidget()
        self.ui_upload = Ui_Upload()
        self.ui_upload.setupUi(self.ui_upload_window)

        # Attributes used across the class
        self.client = None
        self.file = None
        self.file_frame = None
        self.login_url = 'http://127.0.0.1:8000/users/login'
        self.upload_url = 'http://127.0.0.1:8000/upload'
        self.counter = 0
        self.group = QButtonGroup(self.ui_upload.scrollAreaWidgetContents)
        self.proc_arr = []

        # communication slots
        # used to communicate between the main thread and the monitor thread
        self.comm = Communicate()
        self.comm.started.connect(self.set_estimated_time)
        self.comm.ended.connect(self.complete_info)
        self.comm.update.connect(self.update_progress_bar)
        self.comm.canceled.connect(self.cancel_info)

        # button connections
        self.ui_login.login_button.clicked.connect(self.login)
        self.ui_upload.logout_button.clicked.connect(self.logout)
        self.ui_upload.select_button.clicked.connect(self.select_file)
        self.ui_upload.upload_button.clicked.connect(self.add_file_frame)
        self.ui_upload.upload_button.clicked.connect(self.create_worker)
        self.ui_upload.upload_button.clicked.connect(self.clear_filename)
        self.group.idClicked.connect(self.cancel_worker)

        # set echo mode
        self.ui_login.password_lineEdit.setEchoMode(QLineEdit.Password)

    def login(self):
        """Method to handle user login"""

        client = login(
            username=self.ui_login.username_lineEdit.text(),
            password=self.ui_login.password_lineEdit.text(),
            login_url=self.login_url,
            test_url=self.upload_url
        )

        if client:
            # clear all the fields and label in login screen and show upload screen
            self.ui_login.username_lineEdit.clear()
            self.ui_login.password_lineEdit.clear()
            self.ui_login.info_label.clear()

            self.hide()
            self.ui_upload_window.show()

            self.client = client
        else:
            self.ui_login.info_label.setText('Wrong username or password')

    def logout(self):
        """ Function to handle logout """
        self.show()
        # clear upload window
        for children in self.ui_upload.scrollAreaWidgetContents.children():
            if children.objectName() == 'file_frame':
                children.deleteLater()
        self.counter = 0
        self.client = None
        self.ui_upload_window.hide()

    def select_file(self):
        """Instantiate a file class and send to the class attr"""
        self.file = File()
        self.ui_upload.filename_label.setText(self.file.get_filename())

    def add_file_frame(self):
        """ Add a file upload frame with the filename, estimated time, progress bar and cancel button """
        # The frame containing all the info
        if not self.file:
            return
        self.file_frame = QFrame(self.ui_upload.scrollAreaWidgetContents)
        self.file_frame.setObjectName(f"file_frame")
        self.file_frame.setMinimumSize(QSize(0, 80))
        self.file_frame.setMaximumSize(QSize(16777215, 80))
        self.file_frame.setFrameShape(QFrame.NoFrame)
        self.file_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6 = QHBoxLayout(self.file_frame)
        self.horizontalLayout_6.setObjectName(f"horizontalLayout_6_x")

        # Frame containing the filename
        self.sending_filename_frame = QFrame(self.file_frame)
        self.sending_filename_frame.setObjectName(f"sending_filename_frame_x")
        self.sending_filename_frame.setMinimumSize(QSize(150, 0))
        self.sending_filename_frame.setMaximumSize(QSize(150, 16777215))
        self.sending_filename_frame.setFrameShape(QFrame.NoFrame)
        self.sending_filename_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.sending_filename_frame)
        self.horizontalLayout_7.setObjectName(f"horizontalLayout_7_x")
        self.sending_filename_label = QLabel(self.sending_filename_frame)
        self.sending_filename_label.setText(self.file.get_filename())
        self.sending_filename_label.setStyleSheet(u'color: white;')
        self.sending_filename_label.setObjectName(f"sending_filename_label_x")

        self.horizontalLayout_7.addWidget(self.sending_filename_label)
        self.horizontalLayout_6.addWidget(self.sending_filename_frame)

        # Frame containing the estimated time
        self.time_frame = QFrame(self.file_frame)
        self.time_frame.setObjectName(f"time_frame_x")
        self.time_frame.setMinimumSize(QSize(150, 0))
        self.time_frame.setMaximumSize(QSize(150, 16777215))
        self.time_frame.setFrameShape(QFrame.NoFrame)
        self.time_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.time_frame)
        self.horizontalLayout_8.setObjectName(f"horizontalLayout_8_x")
        self.time_label = QLabel(self.time_frame)
        self.time_label.setStyleSheet(u'color: white;')
        self.time_label.setObjectName(f"time_label_x")

        self.horizontalLayout_8.addWidget(self.time_label)
        self.horizontalLayout_6.addWidget(self.time_frame)

        # Frame containing the progress bar
        self.progressBar_frame = QFrame(self.file_frame)
        self.progressBar_frame.setObjectName(f"progressBar_frame_x")
        self.progressBar_frame.setFrameShape(QFrame.NoFrame)
        self.progressBar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.progressBar_frame)
        self.horizontalLayout_10.setObjectName(f"horizontalLayout_10_x")
        self.progressBar = QProgressBar(self.progressBar_frame)
        self.progressBar.setObjectName(f"progressBar_x")
        self.progressBar.setValue(0)

        self.horizontalLayout_10.addWidget(self.progressBar)
        self.horizontalLayout_6.addWidget(self.progressBar_frame)

        # Frame containing the cancel button
        self.cancel_frame = QFrame(self.file_frame)
        self.cancel_frame.setObjectName(f"cancel_frame_x")
        self.cancel_frame.setMinimumSize(QSize(80, 0))
        self.cancel_frame.setMaximumSize(QSize(80, 16777215))
        self.cancel_frame.setFrameShape(QFrame.NoFrame)
        self.cancel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.cancel_frame)
        self.horizontalLayout_9.setObjectName(f"horizontalLayout_9_x")
        self.cancel_button = QPushButton(self.cancel_frame)
        self.cancel_button.setObjectName(f"cancel_button_x")
        self.cancel_button.setText('Cancel')
        self.cancel_button.setStyleSheet(u'background-color: #bf2424; color: white;')

        self.horizontalLayout_9.addWidget(self.cancel_button)
        self.horizontalLayout_6.addWidget(self.cancel_frame)
        self.ui_upload.verticalLayout_2.addWidget(self.file_frame)
        self.ui_upload.upload_scrollArea.setWidget(self.ui_upload.scrollAreaWidgetContents)
        self.ui_upload.horizontalLayout_5.addWidget(self.ui_upload.upload_scrollArea)
        self.ui_upload.verticalLayout.addWidget(self.ui_upload.content_frame)

        # Add the cancel button to the button group with the id being the counter number
        self.group.addButton(self.cancel_button, self.counter)
        self.counter += 1

    def create_worker(self):
        """ Instantiate and start a worker and monitor"""
        if not self.file:
            return
        worker = Worker(self.client, self.file.get_file(), self.upload_url)
        self.proc_arr.append(worker)
        monitor = Monitor(worker, self.comm, self.file_frame)
        monitor.create_thread()

    def cancel_worker(self, id):
        """ Cancel the worker process by calling the method terminate """
        worker = self.proc_arr[id]
        if worker.proc.is_alive():
            worker.canceled = True
        else:
            self.group.button(id).parent().parent().deleteLater()

    def clear_filename(self):
        """ Clear the filename label"""
        self.ui_upload.filename_label.clear()

    def complete_info(self, file_frame):
        """ Set all the info when the file upload is completed """
        progress_bar = file_frame.children()[3].children()[-1]
        progress_bar.setValue(100)
        button = file_frame.children()[-1].children()[-1]
        button.setText('Done')
        button.setStyleSheet(u'background-color: #1fad1a;')

    def update_progress_bar(self, file_frame):
        """ Set progress bar value += 1 """
        progress_bar = file_frame.children()[3].children()[-1]
        if progress_bar.value() == 99:
            return
        else:
            progress_bar.setValue(progress_bar.value() + 1)

    def cancel_info(self, file_frame):
        """ Set all the info when file upload is canceled """
        time_label = file_frame.children()[2].children()[-1]
        time_label.setText('Canceled')
        button = file_frame.children()[-1].children()[-1]
        button.setText('Remove')

    def set_estimated_time(self, file_frame):
        """ Funtion to set the estimated time for the upload file

            OBS: Since django communication with the python libs to show progress and estimated time
            (tqdm and requests_toolbelt)
            can't be done yet, the best option was to use this fake estimated time
        """
        time_label = file_frame.children()[2].children()[-1]
        if int(os.path.getsize(self.file.get_file_path()) / float(1 << 20)) < 30:
            time_label.setText('Estimated < 1s')
        elif int(os.path.getsize(self.file.get_file_path()) / float(1 << 20)) < 60:
            time_label.setText('Estimated < 1.5s')
        elif int(os.path.getsize(self.file.get_file_path()) / float(1 << 20)) < 120:
            time_label.setText('Estimated < 2')
        elif int(os.path.getsize(self.file.get_file_path()) / float(1 << 20)) < 240:
            time_label.setText('Estimated < 2.5')
        elif int(os.path.getsize(self.file.get_file_path()) / float(1 << 20)) < 460:
            time_label.setText('Estimated < 20s')
        else:
            time_label.setText('Estimated > 20s')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    icon = QIcon('resources/images/icon.png')

    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QMenu()
    option1 = QAction('Quit')
    option1.triggered.connect(app.quit)

    menu.addAction(option1)
    tray.setContextMenu(menu)

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
