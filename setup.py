# -*- coding: utf-8 -*-
__author__ = 'xuanwo'

from setuptools import setup, find_packages
import chineseregion

entry_points = {
    "console_scripts": [
        "chineseregion = chineseregion.main:main",
    ]
}

setup(
    name="chineseregion",
    version= chineseregion.__version__,
    description="a chinese region lib for python",
    author="xuanwo",
    author_email="xuanwo.cn@gmail.com",
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True
)
