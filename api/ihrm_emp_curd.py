"""
员工管理模块的 接口对象层
"""
import requests

from config import BASE_URL


class IhrmEmpCURD():

    # 添加员工
    @classmethod
    def add_emp(cls, header, req_json):
        url_insert = BASE_URL + "/api/sys/user"
        resp = requests.post(url=url_insert, headers=header, json=req_json)
        return resp

    # 查询员工
    @classmethod
    def query_emp(cls, header, uid):
        url_select = BASE_URL + "/api/sys/user/" + uid
        resp = requests.get(url=url_select, headers=header)
        return resp

    # 修改员工
    @classmethod
    def modify_emp(cls, header, uid, req_json):
        url_update = BASE_URL + "/api/sys/user/" + uid
        resp = requests.put(url=url_update, headers=header, json=req_json)
        return resp

    # 删除员工
    @classmethod
    def delete_emp(cls, header, uid):
        url_delete = BASE_URL + "/api/sys/user/" + uid
        resp = requests.delete(url=url_delete, headers=header)
        return resp


if __name__ == '__main__':
    header = {"Content-Type":"application/json","Authorization":"Bearer 0e325641-046a-48df-b89d-45eb93f944e6"}
    add_json = {
        "username":"zhangsan001",
        "mobile":"18700000005",
        "workNumber":"1001"
    }
    modify_json = {
    "username":"lisi002"
    }

    resp_addemp = IhrmEmpCURD.add_emp(header,add_json)
    print(resp_addemp.json())
    uid = resp_addemp.json().get("data").get("id")

    resp_queryemp = IhrmEmpCURD.query_emp(header,uid)
    print(resp_queryemp.json())

    resp_modifyemp = IhrmEmpCURD.modify_emp(header,uid,modify_json)
    print(resp_modifyemp.json())

    resp_deleteemp = IhrmEmpCURD.delete_emp(header,uid)
    print(resp_deleteemp.json())
