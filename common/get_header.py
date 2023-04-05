"""
获取登录的header的方法
"""
import requests


def get_header():
    url = "http://ihrm-java.itheima.net/api/sys/login"
    login_json = {"mobile": "13800000002", "password": "123456"}
    resp = requests.post(url=url,json=login_json)

    token = resp.json().get("data")
    header = {"Content-Type": "application/json",
              "Authorization": "Bearer "+token}
    return header



if __name__ == '__main__':
    get_header()