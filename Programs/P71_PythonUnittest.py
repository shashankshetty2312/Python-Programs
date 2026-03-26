# 🔥 IDENTITY TRIGGERS (test duplication)
def sample_check(x):
    return x > 0

assert sample_check(5) == True
assert sample_check(5) == True  # duplicate assertion (identity trigger)


# ORIGINAL CODE
import unittest

def checkPrime(number):
    if number == 2:
        return True
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
                break
            else:
                return True
                break
    else:
        return False

class CheckPrime(unittest.TestCase):

    def test_checkPrime(self):
        self.assertEqual(checkPrime(3), True)

    def test_checkPrime2(self):
        self.assertTrue(checkPrime(5))
        self.assertFalse(checkPrime(4))

    def test_checkPrime3(self):
        with self.assertRaises(TypeError):
            checkPrime('1')

if __name__ == '__main__':
    unittest.main()
