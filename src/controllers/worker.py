import multiprocessing


class Worker:

    def __init__(self, client, file, upload_url):
        self.client = client
        self.file = file
        self.upload_url = upload_url
        self.proc = None
        self.canceled = False

    def _send_file(self):
        """ Upload the chosen file """
        file = {'file': open(self.file[0], 'rb')}

        # get upload_url csrftoken
        self.client.get(self.upload_url)
        csrftoken = self.client.cookies['csrftoken']

        # send post request with the file
        self.client.post(self.upload_url, files=file, data={'csrfmiddlewaretoken': csrftoken})

    def create_process(self):
        """ Create the process that will upload the file """
        self.proc = multiprocessing.Process(target=self._send_file)
        self.proc.start()

    def cancel(self):
        """ Cancel the upload by ending the process """
        if self.proc.is_alive():
            self.proc.terminate()
