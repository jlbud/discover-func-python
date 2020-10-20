#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys

len = os.path.abspath(os.path.dirname(__file__)).find('jsyh-docking-system') + len('jsyh-docking-system')
dir = sys.path.append(os.path.abspath(os.path.dirname(__file__))[:len])
print(dir)
