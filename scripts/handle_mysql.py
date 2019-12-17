"""
Time:2019/12/15 0015
"""
import pymysql
import random

from scripts.handle_config import hy


class HandleMysql:

    def __init__(self):
        self.conn = pymysql.connect(host=hy.read_yaml('mysql', 'host_name'),
                                    user=hy.read_yaml('mysql', 'user_name'),
                                    password=hy.read_yaml('mysql', 'password'),
                                    port=hy.read_yaml('mysql', 'port'),
                                    db=hy.read_yaml('mysql', 'db'),
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def get_mysql_result(self, sql, args=None, is_more=True):
        """
        :param sql:传入的sql语句
        :param args:
        :param is_more:是否获取多条数据
        :return:
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    @staticmethod
    def get_random_phone():
        return hy.read_yaml('myphone', 'prefix_phone') + ''.join((random.sample('0123456789', 8)))

    def assert_exist_phone(self, phone_num):
        """
        确认查询的数据能否查询成功
        :param phone_num:
        :return:布尔值
        """
        result = self.get_mysql_result(hy.read_yaml('mysql', 'sql'), args=phone_num, is_more=False)
        if result:
            return True
        else:
            return False

    def get_phone_no_exist(self):
        """
        获取数据库中不存在的电话号码
        :return: 返回数据库中不存在的电话号码
        """
        while True:
            phone = self.get_random_phone()
            result_data = self.assert_exist_phone(phone)
            if not result_data:
                break
        return phone

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    hm = HandleMysql()
    print(HandleMysql.get_random_phone())
    print(hm.get_phone_no_exist())
