# pyqt-svg-icon-pushbutton
PyQt QPushButton which user can set svg icon (not a low quality)

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git --upgrade```

## Example
Code Sample
```python
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout

from practice.svgPractice.svgPractice import SvgPushButton


class SvgIconPushButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        newButton = SvgPushButton()
        newButton.setIcon('new.svg')

        openButton = SvgPushButton()
        openButton.setIcon('open.svg')

        saveButton = SvgPushButton()
        saveButton.setIcon('save.svg')

        lay = QHBoxLayout()
        lay.addWidget(newButton)
        lay.addWidget(openButton)
        lay.addWidget(saveButton)

        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = SvgIconPushButtonExample()
    ex.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/153802219-ae019e5b-f603-4aad-93ce-035d33edd9a8.mp4

Sorry for the video quality.

![image](https://user-images.githubusercontent.com/55078043/153802633-5517f7ac-3d86-4d7f-b2de-40dbc10a19f8.png)

Image is much better. Above image is slightly bigger than actual size.
