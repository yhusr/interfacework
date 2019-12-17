"""
Time:2019/12/15 0015
"""
from scripts.handle_mysql import HandleMysql
from scripts.handle_request import HandleRequest
from scripts.handle_config import HandYaml, hy
from scripts.handle_path import PHONE_PATH


class HandlePhone:

    @staticmethod
    def send_register_phone_request(username, type_num, password='12345678'):
        hm = HandleMysql()
        hr = HandleRequest()
        hr.common_heads(hy.read_yaml('myphone', 'head'))
        url = ''.join((hy.read_yaml('api', 'load'), hy.read_yaml('api', 'register')))

        while True:
            phone_num = hm.get_phone_no_exist()
            data = {"mobile_phone": phone_num,
                    "pwd": password,
                    "type": type_num,
                    "reg_name": username}
            res = hr.send(url, data=data)
            if res:
                user_id = hm.get_mysql_result(hy.read_yaml('mysql', 'sql'), phone_num)[0]['id']
                break
        phone_data = {username: {
                            "user_Id": user_id,
                            "userPhone": phone_num,
                            "type": type_num,
                            "reg_name": username
                           }}
        hr.close()
        hm.close()
        return phone_data

    @classmethod
    def generate_phone(cls):
        hyaml = HandYaml(PHONE_PATH)
        admin_request = HandlePhone.send_register_phone_request('admin', 0)
        borrow_request = HandlePhone.send_register_phone_request('borrow', 1)
        invest_request = HandlePhone.send_register_phone_request('invest', 1)
        phone_dic = {}
        phone_dic.update(invest_request)
        phone_dic.update(borrow_request)
        phone_dic.update(admin_request)
        hyaml.write_yaml(phone_dic)


if __name__ == '__main__':
    HandlePhone.generate_phone()
