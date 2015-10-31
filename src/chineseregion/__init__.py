# -*- coding: utf-8 -*-
__author__ = 'xuanwo'

import os, sys
import json

with open('region.json') as fp:
        data = json.load(fp)

def find(str, data):
    city = []
    for i in sorted(data.keys()):
        if str.find(data[i]) != -1:
            city.append(data[i])
    return city

def main(argv):
    for i in range(0, len(argv)):
        answer = find(argv[i], data)
        if(len(answer)==0):
            print("Not Found")
        else:
            print(answer)


if __name__ == '__main__':
    main(sys.argv[1:])
