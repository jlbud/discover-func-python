#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading


class Thread(threading.Thread):
    def __init__(self, func, args=()):
        super(Thread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            # 如果子线程不使用join方法，此处可能会报没有self.result的错误
            return self.result
        except Exception:
            return None
