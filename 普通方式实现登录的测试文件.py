import unittest
import requests

class TestLogin(unittest.TestCase):
    def test_01_login_success(self):
        """
        登录成功（正确的用户名+密码）
        :return:
        """
        resp = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                             headers={"Content-Type": "application/json"},
                             json={"mobile": "13800000002", "password": "123456"})

        print(resp.json())
        self.assertEqual(200,resp.status_code)
        self.assertEqual(True,resp.json().get("success"))
        self.assertEqual(10000,resp.json().get("code"))
        self.assertIn("操作成功！",resp.json().get("message"))

    def test_02_login_faild(self):
        """
        登录失败（错误的密码）
        :return:
        """
        resp = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                             headers={"Content-Type": "application/json"},
                             json={"mobile": "13800000002", "password": "123456789"})

        print(resp.json())
        self.assertEqual(200,resp.status_code)
        self.assertEqual(False,resp.json().get("success"))
        self.assertEqual(20001,resp.json().get("code"))
        self.assertIn("用户名或密码错误",resp.json().get("message"))

    def test_03_login_faild(self):
        """
        登录失败（手机号为空）
        :return:
        """
        resp = requests.post(url="http://ihrm-java.itheima.net/api/sys/login",
                             headers={"Content-Type": "application/json"},
                             json={"mobile": "", "password": "123456789"})

        print(resp.json())
        self.assertEqual(200,resp.status_code)
        self.assertEqual(False,resp.json().get("success"))
        self.assertEqual(20001,resp.json().get("code"))
        self.assertIn("用户名或密码错误",resp.json().get("message"))