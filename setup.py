#!/usr/bin/env python

from distutils.core import setup

setup(name='ComputerInfo',
      version='1.0',
      description='Tool for obtain compute name and ip interfaces',
      author='Loonaire',
      author_email='loonairefr@gmail.com',
      url='https://www.github.com/loonaire',
      packages=['distutils', 'distutils.command','sys', 'PySide6.QtNetwork','PySide6.QtWidgets'],
     )
