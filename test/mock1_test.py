import unittest
from mock1 import *

class TestReverseList(unittest.TestCase):

    def test_case1(self):
        user_input = [1,2,3,4,5]
        output = [5,4,3,2,1]
        self.assertEqual(func_test(user_input), output)
    
    def test_case2(self):
        user_input = [1]
        output = [1]
        self.assertEqual(func_test(user_input), output)
    
    def test_case3(self):
        user_input = [1,2]
        output = [2,1]
        self.assertEqual(func_test(user_input), output)

if __name__ == '__main__':
    unittest.main()