"""
单元测试 - 针对程序中最小的功能模块进行的测试
在Python程序中最小的功能模块是函数和方法(写在类里面的函数)

白盒测试 - 写测试的人知道代码内部结构 - 程序自己写
黑盒测试 - 写测试的人不知道代码内部结构 - 测试(QA)人员
功能性测试
"""
from unittest import TestCase

from example01 import seq_search
from example01 import bin_search


# python3 -m unittest test_example01.py
class TestExample01(TestCase):
    """测试类"""

    def setUp(self):
        """每个测试之前要执行的方法"""
        print('开始执行测试...')

    def tearDown(self):
        """每个测试之后要执行的方法"""
        print('测试结束...')

    def test_seq_search(self):
        """测试顺序查找"""
        items = [34, 99, 52, 11, 47, 68, 50, 84]
        self.assertEqual(0, seq_search(items, 34))
        self.assertEqual(1, seq_search(items, 99))
        self.assertEqual(4, seq_search(items, 47))
        self.assertEqual(7, seq_search(items, 84))
        self.assertEqual(-1, seq_search(items, 66))

    def test_bin_search(self):
        """测试二分查找"""
        items = [12, 30, 47, 50, 68, 73, 84, 99]
        self.assertEqual(0, bin_search(items, 12))
        self.assertEqual(1, bin_search(items, 30))
        self.assertEqual(4, bin_search(items, 68))
        self.assertEqual(7, bin_search(items, 99))
        self.assertEqual(-1, bin_search(items, 55))
