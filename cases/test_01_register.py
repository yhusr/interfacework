# -*- coding:utf-8 -*-
# @Time    :2019/12/16 0016 16:02
# @Author  :toy_yh
# @File    :test_01_register.py
# @Software:PyCharm

import unittest
from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_parameterize import HandlePara
from scripts.handle_config import hy
from scripts.handle_request import HandleRequest
from scripts.handle_log import hl


@ddt
class TestRegister(unittest.TestCase):
    he = HandleExcel('register')
    excel_data = he.read_excel()

    @classmethod
    def setUpClass(cls):
        cls.hr = HandleRequest()
        cls.hr.common_heads(hy.read_yaml('myphone', 'head'))

    @data(*excel_data)
    def testRegister(self, excel_data):
        para_data = HandlePara.parameterize(excel_data.data)
        url = ''.join((hy.read_yaml('api', 'load'), hy.read_yaml('api', 'register')))
        res = self.hr.send(url, data=para_data)
        actual_result = res.json().get('code')
        actual_msg = res.json().get('msg')
        try:
            self.assertListEqual([actual_result, actual_msg], [excel_data.expected, excel_data.msg],
                                 msg=f'此{excel_data.title}已执行完毕')
        except AssertionError as a:
            self.he.write_excel(int(excel_data.caseId) + 1, 7, 'fail')
            hl.error(a)
            raise a
        else:
            self.he.write_excel(int(excel_data.caseId) + 1, 7, 'success')
            hl.info(excel_data.title)

    @classmethod
    def tearDownClass(cls):
        cls.hr.close()
