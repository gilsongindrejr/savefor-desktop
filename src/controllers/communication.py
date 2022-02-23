from PySide2.QtCore import QObject, Signal


class Communicate(QObject):
    """ Signals so the secondary thread can communicate with the primary thread """
    started = Signal(object)
    ended = Signal(object)
    update = Signal(object)
