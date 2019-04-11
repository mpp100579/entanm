import threading, time

'''
def func(n):
    time.sleep(2)
    print(time.time(),n)
if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=func, args=(1,))
        t.start()
    print('主线程结束')
'''


from time import sleep
import random
import unittest
import json
import requests

a = random.randint(1,10000)
#发送put交易请求


class ETest(unittest.TestCase):
    def setUp(self):
        self.url='http://39.105.77.252:5000'

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('teardown')
    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('begin')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('close')


    def test_transction(self):
        data = {"secret": "race forget pause shoe trick first abuse insane hope budget river enough",
                "amount": a,
                "recipientId": "AMFcPgkRndYVgjMs9gKTKMEwW72yGivw3z"}
        header = {'Content-Type': 'application/json'}
        j = json.dumps(data)  #如果请求参数是json格式，就需要转成json格式再传
        r = requests.put(self.url+'/api/transactions', data=j, headers=header)

        result=r.json() #把响应结果转化为json格式
        print(result)

        #断言
        self.assertEqual(result['success'],True)
        self.assertIsNotNone(result['transactionId'])
        sleep(3)

    def test_undelegate(self):
        data = {"secret": "gentle crawl private include winner paddle october flat spray season axis buffalo"}
        header = {'Content-Type': 'application/json'}
        j = json.dumps(data)  #如果请求参数是json格式，就需要转成json格式再传
        r = requests.put(self.url+'/api/delegates/undelegate', data=j, headers=header)

        result=r.json() #把响应结果转化为json格式
        print(result)
        # 断言
        self.assertEqual(result['success'], True)
        sleep(5)

    def test_delegates(self):
        data = {"secret": "gentle crawl private include winner paddle october flat spray season axis buffalo",
                "username": "krkg"}
        header = {'Content-Type': 'application/json'}
        j = json.dumps(data)  #如果请求参数是json格式，就需要转成json格式再传

        r = requests.put(self.url+'/api/delegates', data=j, headers=header)
        print(r)
        result=r.json() #把响应结果转化为json格式
        print(result)
        # 断言
        self.assertEqual(result['success'],True)

    @unittest.skip("i don't want to run this case. ")
    def test_mpp(self):
        print('我大哥是{name}，今年{age}岁。'.format(name='阿飞', age=20))


    def test_lockvote(self):
        data ={"secret": "latin bid insane galaxy couch rookie nephew hair thumb train rice nest","args": "*[1000]"}
        header = {'Content-Type': 'application/json'}
        j = json.dumps(data)  # 如果请求参数是json格式，就需要转成json格式再传
        r = requests.put(self.url + '/api/lockvote', data=j, headers=header)
        print(r)
        result = r.json()  # 把响应结果转化为json格式
        print(result)
        # 断言
        self.assertEqual(result['success'], True)
        sleep(5)

# 如果想临时跳过某个case：skip装饰器
#     @unittest.skip("i don't want to run this case. ")
    def test_vote(self):
        data ={"secret": "latin bid insane galaxy couch rookie nephew hair thumb train rice nest",
            "delegates": ["+AMFcPgkRndYVgjMs9gKTKMEwW72yGivw3z"]}
        header = {'Content-Type': 'application/json'}
        j = json.dumps(data)  # 如果请求参数是json格式，就需要转成json格式再传

        r = requests.put(self.url + '/api/accounts/delegates', data=j, headers=header)

        result = r.json()  # 把响应结果转化为json格式
        print(result)
        # 断言
        self.assertEqual(result['success'], True)




if __name__ == '__main__':
    # 在main()中加verbosity参数，可以控制输出的错误报告的详细程度
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
