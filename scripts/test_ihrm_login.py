import unittest

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import ihrm_login_assert
from parameterized import parameterized

from common.read_json_util import ihrm_get_data
from config import BASE_PATH


class TestIhrmLogin(unittest.TestCase):
    file = BASE_PATH + "/data/ihrm_login_data.json"
    login_data_list = ihrm_get_data(file)

    @parameterized.expand(login_data_list)
    def test_ihrm_login(self, desc,req_data, status_code, success, code, message):
        json_data = req_data
        resp = IhrmLoginApi.login(json_data)
        ihrm_login_assert(self, resp, status_code, success, code, message)


    # def test_01_login_success(self):
    #     json_data = {"mobile": "13800000002", "password": "123456"}
    #     resp = IhrmLoginApi.login(json_data)
    #
    #     ihrm_login_assert(self,resp,200,True,10000,"操作成功")
    #
    #
    # def test_02_login_faild(self):
    #     json_data = {"mobile": "13800000002", "password": "123456789"}
    #     resp = IhrmLoginApi.login(json_data)
    #
    #     ihrm_login_assert(self, resp, 200, False, 20001, "用户名或密码错误")
    #
    # def test_03_login_faild(self):
    #     json_data = {"mobile": "", "password": "123456789"}
    #     resp = IhrmLoginApi.login(json_data)
    #
    #     ihrm_login_assert(self, resp, 200, False, 20001, "用户名或密码错误")


if __name__ == '__main__':
    unittest.main()
