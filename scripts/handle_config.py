"""
Time:2019/12/14 0014
"""

import yaml
import configparser

from scripts.handle_path import YAML_PATH, CONF_PATH


class HandYaml:
    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    def read_yaml(self, section_name, option_name):
        with open(self.yaml_path, encoding='utf-8') as w:
            yaml_data = yaml.full_load(w)
        res_data = yaml_data[section_name][option_name]
        return res_data

    def write_yaml(self,json_data):
        with open(self.yaml_path, mode='a', encoding='utf-8') as f:
            yaml.dump(json_data, f, allow_unicode=True)


hy = HandYaml(YAML_PATH)


class HandleConf:
    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.conf = configparser.ConfigParser()

    def read_conf(self, section_name, option_name):
        conf_read = self.conf.read(self.conf_path, encoding='utf-8')
        conf_data = conf_read[section_name][option_name]
        try:
            para_data = eval(conf_data)
        except Exception as e:
            return conf_data
        else:
            return para_data

    def write_conf(self, data_conf):
        for data in data_conf:
            self.conf[data] = data_conf[data]
        with open(self.conf_path, mode='a', encoding='utf-8') as o:
            self.conf.write(o)


hc = HandleConf(CONF_PATH)