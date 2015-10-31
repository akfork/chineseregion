# -*- coding: utf-8 -*-
__author__ = 'xuanwo'

import json


def find(str):
    pass


def main():
    with open('region.json') as fp:
        data = json.load(fp)
        print(list(data.values()))


if __name__ == '__main__':
    main()
