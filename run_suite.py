"""
1. 创建一个测试套件实例  suite
2. 添加测试类
3. 创建HTMLTestReport 类实例  run
4. 调用run方法 ，传入suite
"""

import unittest
from htmltestreport import HTMLTestReport

from config import BASE_PATH
from scripts.test_ihrm_add_emp_param import TestIhrmAddEmpParam
from scripts.test_ihrm_login import TestIhrmLogin

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestIhrmLogin))
suite.addTest(unittest.makeSuite(TestIhrmAddEmpParam))

runner = HTMLTestReport(BASE_PATH+"/report/ihrm_report.html",description="描述信息",title="报告标题")

runner.run(suite)


