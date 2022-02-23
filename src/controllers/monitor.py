import threading


class Monitor:

    def __init__(self, worker, comm, file_frame):
        self.worker = worker
        self.comm = comm
        self.file_frame = file_frame

    def _start(self):
        """Instantiate a worker and monitor its task"""
        self.worker.create_process()
        self.comm.started.emit(self.file_frame)
        while True:
            try:
                if self.worker.proc.is_alive():
                    self.comm.update.emit(self.file_frame)
                    continue
                else:
                    if self.worker.canceled:
                        self.worker.cancel()
                        self.comm.canceled.emit(self.file_frame)
                        break
                    self.comm.ended.emit(self.file_frame)
                    break
            except Exception:
                # Using broad exception just to know if the process is not created
                break

    def create_thread(self):
        """Create a thread to run the _start method"""
        thread = threading.Thread(target=self._start)
        thread.start()
        self.comm.started.emit(self.file_frame)
