# 添加员工

import requests

from config import BASE_URL

# url_insert = BASE_URL + "/api/sys/user"
# headers_insert = {"Content-Type":"application/json","Authorization":"Bearer 90122ec0-5b50-4540-8dca-b791cf9c40f0"}
# req_insert = {
#     "username":"zhangsan001",
#     "mobile":"18700000002",
#     "workNumber":"1001"
# }
#
# resp_insert = requests.post(url=url_insert,headers= headers_insert,json=req_insert)
# print(resp_insert.json())

# 查询员工
url_select = BASE_URL + "/api/sys/user/1641101417332617216"
headers_select = {"Authorization":"Bearer 90122ec0-5b50-4540-8dca-b791cf9c40f0"}

resp_select = requests.get(url=url_select,headers=headers_select)
print(resp_select.json())


# 修改员工
url_update = BASE_URL + "/api/sys/user/1641101417332617216"
headers_update = {"Content-Type":"application/json","Authorization":"Bearer 90122ec0-5b50-4540-8dca-b791cf9c40f0"}
req_update = {
    "username":"lisi002"
}
resp_update = requests.put(url=url_select,headers=headers_select,json=req_update)
print(resp_update.json())

# 删除员工
url_delete = BASE_URL + "/api/sys/user/1641101417332617216"
headers_delete = {"Content-Type":"application/json","Authorization":"Bearer 90122ec0-5b50-4540-8dca-b791cf9c40f0"}
resp_delete = requests.delete(url=url_delete,headers=headers_delete)
print(resp_delete.json())