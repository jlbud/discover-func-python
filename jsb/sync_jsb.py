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


def loadConf(cmd) -> Config:
    config = configparser.ConfigParser()

    if cmd == 'test.env':
        confPath = curPath + '/config/test.conf'
    elif cmd == 'publish.env':
        confPath = curPath + '/config/publish.conf'
    else:
        confPath = curPath + '/config/test.conf'

    config.read(confPath, encoding='utf-8')
    staff = config.get('server', 'staff')
    org = config.get('server', 'org')
    return Config(staff=staff, org=org)


def read_file(filepath):
    str = ""
    fp = open(filepath)
    content = fp.readlines()
    for c in content:
        str += c.replace('\n', ' ')
    fp.close()
    return str


if __name__ == '__main__':
    env = ''
    try:
        env = str(sys.argv[1])
    except Exception as e:
        print('sys.argv exception:', e)

    conf = loadConf(env)

    ret = read_file('/Users/kevin/test/role.json')
    print(ret)
