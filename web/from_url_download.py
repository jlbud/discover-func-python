import os
import urllib.request
from concurrent.futures.thread import ThreadPoolExecutor


def cbk(a, b, c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print("\r", "进度{:.0f}%".format(per), end="")


def download(url, pwd):
    if url == '':
        return
    dir = os.path.abspath('.' + pwd)
    work_path = os.path.join(dir, 'Python-3.8.5.tgz')
    urllib.request.urlretrieve(url, work_path, cbk)


download('https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz', '/')
