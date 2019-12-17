# -*- coding:utf-8 -*-
# @Time    :2019/12/17 0017 8:42
# @Author  :toy_yh
# @File    :handle_log.py
# @Software:PyCharm

import logging
import time
import os

from scripts.handle_config import hy
from scripts.handle_path import LOG_PATH


class HandleLog:

    @classmethod
    def get_logger(cls):
        logger = logging.getLogger(hy.read_yaml('log', 'name'))
        formater = logging.Formatter(hy.read_yaml('log', 'format'))
        logger.setLevel(hy.read_yaml('log', 'level'))
        # 控制台输出
        sh = logging.StreamHandler()
        sh.setLevel(hy.read_yaml('log', 'level'))
        sh.setFormatter(formater)
        logger.addHandler(sh)

        # 文件输出
        st = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        filepath = os.path.join(LOG_PATH, f'mylog{st}.log')
        fh = logging.FileHandler(filepath, encoding='utf-8')
        fh.setLevel(hy.read_yaml('log', 'level'))
        fh.setFormatter(formater)
        logger.addHandler(fh)

        return logger


hl = HandleLog.get_logger()
