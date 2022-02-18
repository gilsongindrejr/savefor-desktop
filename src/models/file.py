from PySide2.QtWidgets import QFileDialog


class File:

    def __init__(self):
        self._file = QFileDialog.getOpenFileName()

    def get_file(self):
        """return the file obj"""
        return self._file

    def get_filename(self):
        """return only the filename"""
        return self._file[0].split('/')[-1]

    def get_file_path(self):
        """return the abs path of the file"""
        return self._file[0]
