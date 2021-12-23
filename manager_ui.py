from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ManagerUi(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('manager.ui', self)
