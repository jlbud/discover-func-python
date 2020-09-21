#!/usr/bin/env python
# encoding=utf-8
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import configparser

from jsb.config import Config


def parse_files():
    print("parse_files")


def check_format():
    print("check_format")


def sync_data():
    print("send_data")


def re_sync_data():
    print("send_data")


def loadConf() -> Config:
    env = ''
    try:
        env = str(sys.argv[1])
    except Exception as e:
        print('sys.argv exception:', e)

    if env == 'test.env':
        confPath = curPath + '/config/test.conf'
    elif env == 'publish.env':
        confPath = curPath + '/config/publish.conf'
    else:
        confPath = curPath + '/config/test.conf'

    config = configparser.ConfigParser()
    config.read(confPath, encoding='utf-8')
    staff = config.get('server', 'staff')
    org = config.get('server', 'org')
    return Config(staff=staff, org=org)


def read_file(filepath):
    str = ""
    fp = open(filepath, 'r')
    content = fp.readlines()
    for line in content:
        if line.strip() == '':
            continue
        words = line.split('|')
        for word in words:
            if word.strip() == '':
                continue
            print(word)
            str += word
    fp.close()
    return str


if __name__ == '__main__':
    conf = loadConf()
    ret = read_file('/Users/kevin/github.com/python/discover-func-python/jsb/role.json')
    print(ret)
