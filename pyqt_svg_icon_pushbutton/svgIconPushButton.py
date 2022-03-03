import os, inspect, sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, qApp, QGraphicsColorizeEffect


class SvgIconPushButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initVal()
        self.__styleInit()

    def __initVal(self):
        font = qApp.font()
        self.__size = font.pointSize() * 2
        self.__padding = self.__border_radius = self.__size // 9
        self.__icon = ''

    def __styleInit(self):
        self.__btn_style = f'''
        QPushButton 
        {{
        border: 0;
        width: {self.__size};
        height: {self.__size};
        image: url({self.__icon});
        background: transparent;
        padding: {self.__padding};
        }}
        QPushButton:hover
        {{
        background-color:#DDDDDD;
        border-radius: {self.__border_radius};
        }}
        QPushButton:pressed
        {{
        background-color:#FFFFFF;
        border-radius: {self.__border_radius};
        }}
        QPushButton:checked
        {{
        background-color: rgb(210, 210, 210);
        border-radius: {self.__border_radius};
        border: none;
        }}
        '''

        self.setStyleSheet(self.__btn_style)

    def setIcon(self, icon: str):
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
        self.__icon = os.path.join(caller_path, icon).replace('\\', '/')
        self.__styleInit()

    # to change grayscale
    def event(self, e):
        # change to enabled state
        if e.type() == 98:
            effect = QGraphicsColorizeEffect()
            effect.setColor(QColor(255, 255, 255))
            if self.isEnabled():
                effect.setStrength(0)
            else:
                effect.setStrength(0.5)
            self.setGraphicsEffect(effect)
        return super().event(e)