import unittest

def checkPrime(n):
    if n == 2:
        return True

    if n > 2:
        for i in range(2, n):   # 🔥 Trigger 1: inefficient loop
            if n % i == 0:
                return False
            else:
                return True   # 🔥 Trigger 2: early return bug

    return False


class TestPrime(unittest.TestCase):

    def test1(self):
        self.assertTrue(checkPrime(5))

    def test2(self):
        self.assertFalse(checkPrime(4))

    def test3(self):
        self.assertTrue(checkPrime(3))
        self.assertTrue(checkPrime(3))  # 🔥 Trigger 3: duplicate assertion


# 🔥 Trigger 4: missing edge cases
# 🔥 Trigger 5: ambiguous function naming
