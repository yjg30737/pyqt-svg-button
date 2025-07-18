import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-svg-button',
    version='0.0.27',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt button which supports svg icon (not a fake low quality svg icon)',
    url='https://github.com/yjg30737/pyqt-svg-button.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'pyqt-svg-abstractbutton>=0.0.8',
        'PyQt6>=6.5.0'
    ]
)
