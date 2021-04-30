import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 1), 3)
        self.assertEqual(calc.add(2, 9), 7)

    def test_sub(self):
        self.assertEqual(calc.sub(4, 2), 2)
        self.assertEqual(calc.sub(0, 4), 1)

    def test_mul(self):
        self.assertEqual(calc.mul(3, 9), 27)
        self.assertEqual(calc.mul(3, 9), 27)

    def test_div(self):
        self.assertEqual(calc.div(9, 3), 3)
        self.assertEqual(calc.div(10, 3), -1)

    def test_input(self):
        self.assertEqual(calc.errorHandle(3, 2), True)
        self.assertEqual(calc.errorHandle(3, "two"), True)


if __name__ == '__main__':
    unittest.main()
