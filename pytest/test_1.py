# module name shd start with test_ or end with _test
# class name shd start with "Test" => TestClass/TestExample
# test methods shd start with test  => test_example()

import pytest

class TestClass:
    def testMethod1(self):
        print("This is my first pytest method")
    def testMethod2(self):
        print("testing ...")


# pytest -v -s pytest\test_1.py  => to run particular module in terminal