import unittest

import task_A


class NumbersTest(unittest.TestCase):
    def test_XOR_text(self):
        self.assertEqual(task_A.XOR_hex("1", "1"), 0)
        self.assertEqual(task_A.XOR_hex("111", "111111"), 0)
        self.assertEqual(task_A.XOR_hex("111", "111111"), 0)


if __name__ == '__main__':
    unittest.main()
