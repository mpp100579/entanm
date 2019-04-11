import unittest
import time
from BSTestRunner import BSTestRunner
'''
# @Author  : minpanpan
# @Site    :
# @File    : HTMLTestRunner.py
# @Software: PyCharm

__author__ = "minpanpan"
__version__ = "0.8.2.2"


suite = unittest.TestSuite()#创建测试套件
        all_cases = unittest.defaultTestLoader.discover('.','test_*.py')
        #找到某个目录下所有的以test开头的Python文件里面的测试用例
        for case in all_cases:
            suite.addTests(case)#把所有的测试用例添加进来
        fp = open('res.html','wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='all_tests',description='所有测试情况')
        runner.run(suite)
        #运行测试



test_dir='./testcase'
report_dir='./report'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
report_name=report_dir+'/'+now+'report.html'
with open(report_name,'wb')as f:
    runner=BSTestRunner(stream=f,title='ETM Api Test Report',description='All the Etanmo api test')
    runner.run(discover)


'''

import unittest
import HtmlTestRunner
import HTMLTestRunner
import sys
import os


if __name__=='__main__':
    '''
    test_dir = './testcase'
    suite = unittest.TestSuite()  # 创建测试套件
    all_cases = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    f=open('E:\\myreport.html','wb')
    suite.addTests(all_cases)
    # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Report_title', description='Report_description',verbosity=2)  
    runner.run(suite)    
    '''

    test_dir = './testcase'
    report_dir = './report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_name = report_dir + '/' + now + 'report.html'
    with open(report_name, 'wb')as f:
        runner = BSTestRunner(stream=f, title='ETM Api Test Report', description='All the Etanmo api test')
        runner.run(discover)




