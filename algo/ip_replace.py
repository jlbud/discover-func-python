#!/usr/bin/python
# coding:utf-8

"""
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
"""


def failure_ip_addr(address: str) -> str:
    return address.replace(".", "[.]")


if __name__ == '__main__':
    result = failure_ip_addr("192.168.1.1")
    print(result)
