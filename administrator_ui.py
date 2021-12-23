from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class AdministratorUi(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('administrator.ui', self)
