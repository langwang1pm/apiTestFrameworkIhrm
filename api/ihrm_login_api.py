import requests

from config import BASE_URL


class IhrmLoginApi(object):
    """
    登录结构
    """

    @classmethod
    def login(cls, json_data):
        """
        登录方法
        :param json_data:
        :return:
        """
        url = BASE_URL+'/api/sys/login'
        header_dict = {"Content-Type": "application/json"}
        resp = requests.post(url=url, headers=header_dict, json=json_data)
        return resp


if __name__ == '__main__':
    json_data = {"mobile": "13800000002", "password": "12345678"}
    print(IhrmLoginApi.login(json_data).json())
