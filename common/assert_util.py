
# 登录的断言代码
def ihrm_login_assert(self,resp,status_code,success,code,message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(success, resp.json().get("success"))
    self.assertEqual(code, resp.json().get("code"))
    self.assertIn(message, resp.json().get("message"))

# 用户管理的的断言代码
def ihrm_emp_assert(self,resp,status_code,success,code,message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(success, resp.json().get("success"))
    self.assertEqual(code, resp.json().get("code"))
    self.assertIn(message, resp.json().get("message"))

# 通用的断言代码
def ihrm_common_assert(self,resp,status_code,success,code,message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(success, resp.json().get("success"))
    self.assertEqual(code, resp.json().get("code"))
    self.assertIn(message, resp.json().get("message"))