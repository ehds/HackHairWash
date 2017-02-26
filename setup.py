#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/25 22:02
# @Author  : hale
# @Site    : 
# @File    : MyLog.py
# @Software: PyCharm

#-*-coding:utf8-*-
from setuptools import setup,find_packages

setup(
    name='hairwash',
    version='0.1',
    license='MIT',
    author_email='grephale@gmail.com',
    url='https://github.com/Ds-Hale/QzoneLike',
    description='Python QQZone',
    platforms=['any'],
    packages = find_packages('src'),
    package_dir = {'' : 'src'},
    entry_points={
        'console_scripts': [
            'hairwash-py= hairwash.__main__:main',
        ],
    },
    install_requires=['requests'],
    include_package_data=True,
)