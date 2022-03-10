from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QPushButton, QGraphicsColorizeEffect, QWidget
from python_get_absolute_resource_path.getAbsoulteResourcePath import get_absolute_resource_path


class SvgIconPushButton(QPushButton):
    def __init__(self, base_widget: QWidget = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initVal(base_widget)
        self.__styleInit()

    def __initVal(self, base_widget):
        self.__size = self.font().pointSize() * 2
        self.__padding = self.__border_radius = self.__size // 10
        self.__icon = ''
        self.installEventFilter(self)
        if base_widget:
            self.__baseWidget = base_widget
            self.__baseWidget.installEventFilter(self)
            self.__baseWidget.setObjectName('base_widget')
            self.__initColorByBaseWidget()
        else:
            self.__hover_color = '#DDDDDD'
            self.__pressed_color = '#FFFFFF'
            self.__checked_color = '#CCCCCC'

    def __initColorByBaseWidget(self):
        base_color = self.__baseWidget.palette().color(QPalette.Base)
        if base_color.name() == '#ffffff':
            self.__hover_color = base_color.darker(120).name()
            self.__pressed_color = base_color.darker(140).name()
            self.__checked_color = base_color.darker(130).name()
        else:
            self.__hover_color = base_color.lighter(120).name()
            self.__pressed_color = base_color.lighter(140).name()
            self.__checked_color = base_color.lighter(130).name()

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

    def event(self, e):
        return super().event(e)

    def eventFilter(self, obj, e):
        if obj == self:
            # to change grayscale when button gets disabled
            # if button get enabled/disabled EnableChange will emit
            # so catch the EnabledChange
            if e.type() == 98:
                # change to enabled state
                effect = QGraphicsColorizeEffect()
                effect.setColor(QColor(255, 255, 255))
                if self.isEnabled():
                    effect.setStrength(0)
                else:
                    effect.setStrength(0.5)
                self.setGraphicsEffect(effect)
        if obj.objectName() == 'base_widget':
            # catch the StyleChange event of base widget
            if e.type() == 100:
                self.__initColorByBaseWidget()
                self.__styleInit()
        return super().eventFilter(obj, e)