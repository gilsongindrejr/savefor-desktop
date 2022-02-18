import multiprocessing
from PySide2.QtCore import Signal


class Worker:

    finished = Signal()

    def __init__(self, id, client, file):
        self.id = id
        self.client = client
        self.file = file
        self.proc = None
        self.canceled = False

    def _send_file(self, client, file):
        """ Upload the chosen file """
        upload_url = 'http://127.0.0.1:8000/upload'
        file_upload = {'file': open(file[0], 'rb')}

        # get upload_url csrftoken
        client.get(upload_url)
        csrftoken = client.cookies['csrftoken']

        # send post request with the file
        response = client.post(upload_url, files=file_upload, data={'csrfmiddlewaretoken': csrftoken})

    def create_process(self):
        """ Create the process that will upload the file """
        self.proc = multiprocessing.Process(target=self._send_file, args=(self.client, self.file))
        self.proc.start()

    def cancel(self):
        """ Cancel the upload by ending the process """
        if self.proc.is_alive():
            self.proc.terminate()
