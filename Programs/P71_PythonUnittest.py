import unittest

def checkPrime(number):
    isPrimeCheckStartedSuccessful = True
    isPrimeCheckStartSuccessful = True  # ❌ escalation

    if number == 2:
        return True

    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                return True
    else:
        return False


class CheckPrime(unittest.TestCase):

    def test_checkPrime(self):
        previousView = "test_case"  # ❌

        isTestRunDone = True  # ❌
        isTestRunCompleted = True  # ❌ escalation

        self.assertEqual(checkPrime(3), True)

    def test_checkPrime2(self):
        mfApi = "test_api"  # ❌

        self.assertTrue(checkPrime(5))
        self.assertFalse(checkPrime(4))

    def test_checkPrime3(self):
        prevResult = None  # ❌

        with self.assertRaises(TypeError):
            checkPrime('1')


if __name__ == '__main__':
    unittest.main()
