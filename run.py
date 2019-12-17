"""
Time:2019/12/14 0014
"""

import unittest
import os
import time

from HTMLTestRunnerNew import HTMLTestRunner
from scripts.handle_path import CASES_PATH,REPORT_PATH


class RunCases:

    @classmethod
    def run_cases(cls):
        test_suits = unittest.defaultTestLoader.discover(CASES_PATH)
        st = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        report_path = os.path.join(REPORT_PATH, f'exporter{st}.html')
        runner = HTMLTestRunner(stream=open(report_path, 'wb'),
                                title= '接口测试',
                                verbosity=2,
                                description="自己写的接口",
                                tester='y.h')
        runner.run(test_suits)


if __name__ == '__main__':
    RunCases.run_cases()

