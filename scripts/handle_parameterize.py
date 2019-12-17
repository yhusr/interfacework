"""
Time:2019/12/15 0015
"""

import re
from scripts.handle_config import HandYaml
from scripts.handle_path import PHONE_PATH
from scripts.handle_mysql import HandleMysql


class HandlePara:
    hyaml = HandYaml(PHONE_PATH)

    @classmethod
    def parameterize(cls, data):
        if re.search("{no_exist_phone}", data):
            hm = HandleMysql()
            parameter = re.sub("{no_exist_phone}", hm.get_phone_no_exist(), data)
            hm.close()
            return parameter
        return data
