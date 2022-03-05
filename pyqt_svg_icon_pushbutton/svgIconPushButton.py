import os, inspect

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QPushButton, qApp, QGraphicsColorizeEffect, QWidget
from python_get_absolute_resource_path.getAbsoulteResourcePath import get_absolute_resource_path


class SvgIconPushButton(QPushButton):
    def __init__(self, base_widget: QWidget = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initVal(base_widget)
        self.__styleInit()

    def __initVal(self, base_widget):
        font = qApp.font()
        self.__size = font.pointSize() * 2
        self.__padding = self.__border_radius = self.__size // 10
        self.__icon = ''
        if base_widget:
            self.__baseWidget = base_widget
            self.__baseWidget.installEventFilter(self)
            self.__baseWidget.setObjectName('base_widget')

            base_color = self.__baseWidget.palette().color(QPalette.Base)
            self.__hover_color = base_color.lighter(150).name()
            self.__pressed_color = base_color.lighter(200).name()
            self.__checked_color = base_color.lighter(100).name()
        else:
            self.__hover_color = '#DDDDDD'
            self.__pressed_color = '#FFFFFF'
            self.__checked_color = '#CCCCCC'

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
        background-color: {self.__hover_color};
        border-radius: {self.__border_radius};
        }}
        QPushButton:pressed
        {{
        background-color: {self.__pressed_color};
        border-radius: {self.__border_radius};
        }}
        QPushButton:checked
        {{
        background-color: {self.__checked_color};
        border-radius: {self.__border_radius};
        border: none;
        }}
        '''

        self.setStyleSheet(self.__btn_style)

    def setIcon(self, icon: str):
        self.__icon = get_absolute_resource_path(icon)
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

    def eventFilter(self, obj, e):
        if obj.objectName() == 'base_widget':
            # catch the StyleChange event of base widget
            if e.type() == 100:
                base_color = self.__baseWidget.palette().color(QPalette.Base)
                self.__hover_color = base_color.lighter(150).name()
                self.__pressed_color = base_color.lighter(200).name()
                self.__checked_color = base_color.lighter(100).name()
                self.__styleInit()
        return super().eventFilter(obj, e)