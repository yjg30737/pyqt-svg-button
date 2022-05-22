from PyQt5.QtWidgets import QPushButton, QWidget
from pyqt_svg_abstractbutton import SvgAbstractButton


class SvgButton(QPushButton, SvgAbstractButton):
    def __init__(self, base_widget: QWidget = None, *args, **kwargs):
        super().__init__(*args, **kwargs)