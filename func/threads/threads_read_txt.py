#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threads_read_txt
from itertools import islice


def sync_txt(i, content, start_seek, end_seek):
    for line in islice(content, start_seek, end_seek):
        print('%s---%s' % (i, line))


# 大文件时，
# 用多线程分段读取
if __name__ == '__main__':
    with open('1.txt', 'r') as fp:
        content = fp.readlines()
        start_seek = 0
        end_seek = 10
        threads = []
        num = 1
        while True:
            # 启动一个线程
            t = threads_read_txt.Thread(target=sync_txt, args=(num, content, start_seek, end_seek))
            threads.append(t)
            t.start()
            num += 1
            # 接收线程的回参
            if len(content) < end_seek:
                break
            else:
                start_seek += 10
                end_seek += 10

        for t in threads:
            t.join()
