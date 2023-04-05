import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import ihrm_common_assert
from common.db_util import DBUtils
from common.get_header import get_header
from common.read_json_util import ihrm_get_data
from config import EMP_MOBILe, BASE_PATH
from parameterized import parameterized


class TestIhrmAddEmpParam(unittest.TestCase):
    file = BASE_PATH + "/data/ihrm_add_emp_data.json"
    header = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = get_header()

    def setUp(self) -> None:
        sql = f"delete from bs_user where mobile = '{EMP_MOBILe}'"
        DBUtils.insert_update_delete(sql)

    def tearDown(self) -> None:
        sql = f"delete from bs_user where mobile = '{EMP_MOBILe}'"
        DBUtils.insert_update_delete(sql)

    @parameterized.expand(ihrm_get_data(file))
    def test_add_emp(self, desc, add_json, status_code, success, code, message):
       # 发起请求
        resp = IhrmEmpCURD.add_emp(self.header, add_json)
        # 断言
        ihrm_common_assert(self, resp, status_code, success, code, message)


if __name__ == '__main__':
    unittest.main()
