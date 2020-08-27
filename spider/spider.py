import json
import os
import re

import requests
from requests import RequestException


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(html) -> str:
    pattern = re.compile(
        '<!DOCTYPE html><!--STATUS OK--><html><head><meta name=".*?" content="(.*?)"/><meta name=".*?" content=.*?',
        re.S | re.M)
    items = re.findall(pattern, html)
    return items[0]


def write_to_file(content):
    print(os.path.abspath('../spider'))
    # encoding="utf-8"设置编码为utf-8
    with open(os.path.abspath('../spider') + "/spider.txt", "a", encoding="utf-8") as f:
        # 将对象转为json字符串，ensure_ascii=false设置不是ascii编码
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    url = "https://tieba.baidu.com/"
    html = get_page(url)
    txt = parse_page(html)
    write_to_file(txt)


if __name__ == "__main__":
    main()
