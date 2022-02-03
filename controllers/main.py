import os
import sys
import threading

import requests
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QFileDialog, QFrame, QHBoxLayout, QLabel, QProgressBar, \
    QPushButton, QButtonGroup, QSystemTrayIcon, QMenu, QAction
from PySide2.QtCore import QSize, Signal, QObject

from views.login import Ui_Login
from views.upload import Ui_Upload
from worker import Worker


def is_windows():
    """ Adds app to system tray """
    if os.name == 'nt':
        app.setQuitOnLastWindowClosed(False)
        icon = QIcon('icon.png')

        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)

        menu = QMenu()
        quit = QAction('Quit')
        quit.triggered.connect(app.quit)

        menu.addAction(quit)
        tray.setContextMenu(menu)


class Communicate(QObject):
    """ Signals so the secondary thread can communicate with the primary thread """
    ended = Signal(int)
    canceled = Signal(int)
    update = Signal(int)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # login window
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)

        # upload window
        self.ui_upload_window = QWidget()
        self.ui_upload = Ui_Upload()
        self.ui_upload.setupUi(self.ui_upload_window)

        # Attributes used across the class
        self.file = None
        self.filename = None
        self.counter = 0
        self.group = QButtonGroup(self.ui_upload.scrollAreaWidgetContents)
        self.proc_arr = []
        self.client = None

        self.comm = Communicate()
        self.comm.ended.connect(self.set_button_done)
        self.comm.ended.connect(self.complete_info)
        self.comm.update.connect(self.update_progress_bar)
        self.comm.canceled.connect(self.cancel_worker)

        # button connections
        self.ui_login.login_button.clicked.connect(self.login)
        self.ui_upload.logout_button.clicked.connect(self.logout)
        self.ui_upload.select_button.clicked.connect(self.select_file)
        self.ui_upload.upload_button.clicked.connect(self.add_file_frame)
        self.ui_upload.upload_button.clicked.connect(self.set_estimated_time)
        self.ui_upload.upload_button.clicked.connect(self.create_worker)
        self.group.idClicked.connect(self.cancel_worker)

        # set echo mode
        self.ui_login.password_lineEdit.setEchoMode(QLineEdit.Password)

    def login(self):
        """ Funtion to handle login """

        # get info from the user
        username = self.ui_login.username_lineEdit.text()
        password = self.ui_login.password_lineEdit.text()

        login_url = 'http://127.0.0.1:8000/users/login'
        upload_url = 'http://127.0.0.1:8000/upload'

        # create a session
        self.client = requests.session()

        # send get request to login url to retrieve csrf token
        self.client.get(login_url)
        csrftoken = self.client.cookies['csrftoken']

        # send login data and csrf token to login url
        login_data = {'username': username, 'password': password, 'csrfmiddlewaretoken': csrftoken}
        response = self.client.post(login_url, data=login_data)

        # send get request to upload page to see if the user is authenticated or not
        # if the user is authenticated it returns 200 if not it returns 403
        login_response = self.client.get(upload_url)

        if login_response.status_code == 403:
            self.ui_login.info_label.setText('Wrong username or password')
        if login_response.status_code == 200:
            # clear all the fields and label in login screen
            self.ui_login.username_lineEdit.clear()
            self.ui_login.password_lineEdit.clear()
            self.ui_login.info_label.clear()

            self.hide()
            self.ui_upload_window.show()

    def logout(self):
        """ Function to handle logout """
        self.show()
        for children in self.ui_upload.scrollAreaWidgetContents.children():
            children.deleteLater()
            self.counter = 0
        self.ui_upload_window.hide()

    def select_file(self):
        """ Select the file using QFileDialog and send to the global variable """
        self.file = QFileDialog.getOpenFileName()
        self.filename = self.file[0].split('/')[-1]

        self.ui_upload.filename_label.setText(self.filename)

    def add_file_frame(self):
        """ Add a file upload frame with the filename, estimated time, progress bar and cancel button """
        # The frame containing all the info
        self.file_frame = QFrame(self.ui_upload.scrollAreaWidgetContents)
        self.file_frame.setObjectName(f"file_frame_{self.counter}")
        self.file_frame.setMinimumSize(QSize(0, 80))
        self.file_frame.setMaximumSize(QSize(16777215, 80))
        self.file_frame.setFrameShape(QFrame.NoFrame)
        self.file_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6 = QHBoxLayout(self.file_frame)
        self.horizontalLayout_6.setObjectName(f"horizontalLayout_6_{self.counter}")

        # Frame containing the filename
        self.sending_filename_frame = QFrame(self.file_frame)
        self.sending_filename_frame.setObjectName(f"sending_filename_frame_{self.counter}")
        self.sending_filename_frame.setMinimumSize(QSize(150, 0))
        self.sending_filename_frame.setMaximumSize(QSize(150, 16777215))
        self.sending_filename_frame.setFrameShape(QFrame.NoFrame)
        self.sending_filename_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.sending_filename_frame)
        self.horizontalLayout_7.setObjectName(f"horizontalLayout_7_{self.counter}")
        self.sending_filename_label = QLabel(self.sending_filename_frame)
        self.sending_filename_label.setText(self.filename)
        self.sending_filename_label.setObjectName(f"sending_filename_label_{self.counter}")

        self.horizontalLayout_7.addWidget(self.sending_filename_label)
        self.horizontalLayout_6.addWidget(self.sending_filename_frame)

        # Frame containing the estimated time
        self.time_frame = QFrame(self.file_frame)
        self.time_frame.setObjectName(f"time_frame_{self.counter}")
        self.time_frame.setMinimumSize(QSize(150, 0))
        self.time_frame.setMaximumSize(QSize(150, 16777215))
        self.time_frame.setFrameShape(QFrame.NoFrame)
        self.time_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.time_frame)
        self.horizontalLayout_8.setObjectName(f"horizontalLayout_8_{self.counter}")
        self.time_label = QLabel(self.time_frame)
        self.time_label.setObjectName(f"time_label_{self.counter}")

        self.horizontalLayout_8.addWidget(self.time_label)
        self.horizontalLayout_6.addWidget(self.time_frame)

        # Frame containing the progress bar
        self.progressBar_frame = QFrame(self.file_frame)
        self.progressBar_frame.setObjectName(f"progressBar_frame_{self.counter}")
        self.progressBar_frame.setFrameShape(QFrame.NoFrame)
        self.progressBar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.progressBar_frame)
        self.horizontalLayout_10.setObjectName(f"horizontalLayout_10_{self.counter}")
        self.progressBar = QProgressBar(self.progressBar_frame)
        self.progressBar.setObjectName(f"progressBar_{self.counter}")
        self.progressBar.setValue(0)

        self.horizontalLayout_10.addWidget(self.progressBar)
        self.horizontalLayout_6.addWidget(self.progressBar_frame)

        # Frame containing the cancel button
        self.cancel_frame = QFrame(self.file_frame)
        self.cancel_frame.setObjectName(f"cancel_frame_{self.counter}")
        self.cancel_frame.setMinimumSize(QSize(80, 0))
        self.cancel_frame.setMaximumSize(QSize(80, 16777215))
        self.cancel_frame.setFrameShape(QFrame.NoFrame)
        self.cancel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.cancel_frame)
        self.horizontalLayout_9.setObjectName(f"horizontalLayout_9_{self.counter}")
        self.cancel_button = QPushButton(self.cancel_frame)
        self.cancel_button.setObjectName(f"cancel_button_{self.counter}")
        self.cancel_button.setText('Cancel')
        self.cancel_button.setStyleSheet(u'background-color: #bf2424;')

        self.horizontalLayout_9.addWidget(self.cancel_button)
        self.horizontalLayout_6.addWidget(self.cancel_frame)
        self.ui_upload.verticalLayout_2.addWidget(self.file_frame)
        self.ui_upload.upload_scrollArea.setWidget(self.ui_upload.scrollAreaWidgetContents)
        self.ui_upload.horizontalLayout_5.addWidget(self.ui_upload.upload_scrollArea)
        self.ui_upload.verticalLayout.addWidget(self.ui_upload.content_frame)

        # Add the cancel button to the button group with the id being the counter number
        self.group.addButton(self.cancel_button, self.counter)

    def create_worker(self):
        """ Create the worker process to send the file """
        worker = Worker(self.counter, self.client, self.file)
        self.proc_arr.append(worker)
        for process in self.proc_arr:
            if process.id == self.counter:
                process.create_process()
                self.create_threads(worker)
                self.counter += 1

    def cancel_worker(self, id):
        """ Cancel the worker process by calling the method terminate """
        # self.proc_arr[id].cancel()
        if self.proc_arr[id].proc.is_alive():
            self.proc_arr[id].canceled = True
            self.proc_arr[id].proc.terminate()
            self.cancel_info(id)
        else:
            self.group.button(id).parent().parent().deleteLater()

    def set_button_done(self):
        """ Set the cancel button to done """
        self.group.button(self.counter - 1).setText('Done')
        self.group.button(self.counter - 1).setStyleSheet(u'background-color: #1fad1a;')

    def create_threads(self, worker):
        """ Create the thread to monitor the process """
        t = threading.Thread(target=self.check_if_process_is_alive, args=(worker,))
        t.start()

    def check_if_process_is_alive(self, worker):
        """ Function to check if the process is still alive """
        while 1:
            try:
                if worker.proc.is_alive():
                    self.comm.update.emit(worker.id)
                    continue
                else:
                    if worker.canceled:
                        self.comm.canceled.emit(worker.id)
                        break
                    self.comm.ended.emit(worker.id)
                    break
            except Exception:
                # Using broad exception clause just to know if the process is not created
                break

    def complete_info(self, id):
        """ Set the progress bar value to 100 """
        progress_bar = self.group.button(id).parent().parent().children()[3].children()[1]
        progress_bar.setValue(100)

    def update_progress_bar(self, worker_id):
        """ Set progress bar value += 1 """
        progress_bar = self.group.button(worker_id).parent().parent().children()[3].children()[1]
        if progress_bar.value() == 99:
            return
        else:
            progress_bar.setValue(progress_bar.value() + 1)

    def cancel_info(self, id):
        """ Set the progress bar value to 0 """
        time_label = self.group.button(id).parent().parent().children()[2].children()[1]
        self.group.button(id).setText('Remove')
        time_label.setText('Canceled')

    def set_estimated_time(self):
        """ Funtion to set the estimated time for the upload file

            OBS: Since django communication with the python libs to show progress and estimated time
            (tqdm and requests_toolbelt)
            can't be done yet, the better option was to use this fake estimated time
        """
        time_label = self.group.button(self.counter).parent().parent().children()[2].children()[1]
        if int(os.path.getsize(self.file[0]) / float(1 << 20)) < 30:
            time_label.setText('Estimated < 1s')
        elif int(os.path.getsize(self.file[0]) / float(1 << 20)) < 60:
            time_label.setText('Estimated < 1.5s')
        elif int(os.path.getsize(self.file[0]) / float(1 << 20)) < 120:
            time_label.setText('Estimated < 2')
        elif int(os.path.getsize(self.file[0]) / float(1 << 20)) < 240:
            time_label.setText('Estimated < 2.5')
        elif int(os.path.getsize(self.file[0]) / float(1 << 20)) < 460:
            time_label.setText('Estimated < 20s')
        else:
            time_label.setText('Estimated > 20s')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    is_windows()
    sys.exit(app.exec_())
