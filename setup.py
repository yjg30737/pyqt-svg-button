from setuptools import setup, find_packages

setup(
    name='pyqt-svg-icon-pushbutton',
    version='0.3.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QPushButton which user can set svg icon (not a low quality)',
    url='https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git',
    install_requires=[
        'PyQt5>=5.8',
        'python-get-absolute-resource-path @ git+https://git@github.com/yjg30737/python-get-absolute-resource-path.git@main'
    ]
)