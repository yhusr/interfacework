"""
Time:2019/12/14 0014
"""
import os


# 当前文件目录
current_path = os.path.abspath(__file__)
# 当前文件的上级目录
project_path = os.path.dirname(current_path)
# 当前项目目录
work_path = os.path.dirname(project_path)

# config目录
config_path = os.path.join(work_path, 'config')
# 配置文件的目录
YAML_PATH = os.path.join(config_path, 'project_conf.yaml')
CONF_PATH = os.path.join(config_path, 'config_work.config')
PHONE_PATH = os.path.join(config_path, 'my_phone.yaml')
# data目录
data_path = os.path.join(work_path, 'datas')
# excel目录
EXCEL_PATH = os.path.join(data_path, 'excelcases.xlsx')

#cases目录
CASES_PATH = os.path.join(work_path, 'cases')

#报告的路径
REPORT_PATH = os.path.join(work_path, 'reports')

#日志的路径
LOG_PATH = os.path.join(work_path, 'logs')


