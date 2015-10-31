# -*- coding: utf-8 -*-
__author__ = 'xuanwo'

from setuptools import setup, find_packages

setup(
    name="chineseregion",
    version="0.0.1",
    description = "a chinese region lib for python",
    author = "xuanwo",
    author_email = "xuanwo.cn@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data = True
)
