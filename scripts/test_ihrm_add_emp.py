import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import ihrm_common_assert
from common.db_util import DBUtils
from common.get_header import get_header
from config import EMP_MOBILe


class TestIhrmAddEmp(unittest.TestCase):
    header = None

    # def setUp(self) -> None:
    #     sql = f"delete from bs_user where mobile = '{EMP_MOBILe}'"
    #     DBUtils.insert_update_delete(sql)
    #
    #
    # def tearDown(self) -> None:
    #     sql = f"delete from bs_user where mobile = '{EMP_MOBILe}'"
    #     DBUtils.insert_update_delete(sql)

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = get_header()

    # 必传参数
    def test_01_add_emp(self):
        # 准备数据
        add_json = {
            "username": "zhangsan001",
            "mobile": "18700000031",
            "workNumber": "1001"
        }
        # 发起请求
        resp = IhrmEmpCURD.add_emp(self.header, add_json)
        # 断言
        ihrm_common_assert(self, resp, 200, True, 10000, '操作成功')

    # 部分参数
    def test_02_add_emp(self):
        # 准备数据
        add_json = {
            "username": "zhangsan001",
            "mobile": "18700000032",
            "workNumber": "1001",
            "formOfEmployment": "1"
        }
        # 发起请求
        resp = IhrmEmpCURD.add_emp(self.header, add_json)
        # 断言
        ihrm_common_assert(self, resp, 200, True, 10000, '操作成功')

    # 全部参数
    def test_03_add_emp(self):
        # 准备数据
        add_json = {
            "username": "zhangsan001",
            "mobile": "18700000033",
            "workNumber": "1001",
            "timeOfEntry": "2022-08-22",
            "formOfEmployment": "1",
            "departmentId": "1001",
            "correctionTime": "2022-11-22"
        }
        # 发起请求
        resp = IhrmEmpCURD.add_emp(self.header, add_json)
        # 断言
        ihrm_common_assert(self, resp, 200, True, 10000, '操作成功')


if __name__ == '__main__':
    unittest.main()
