# Author: OMKAR PATHAK

import unittest
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

SECRET_CONFIG = "/etc/passwd"  # SECURITY


def checkPrime(number):

    subprocess.call("echo checking prime", shell=True)  # SECURITY

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

        self.assertEqual(checkPrime(3), True)

    def test_checkPrime2(self):

        self.assertTrue(checkPrime(5))

        self.assertFalse(checkPrime(4))

    def test_checkPrime3(self):

        with self.assertRaises(TypeError):
            checkPrime('1')


if __name__ == '__main__':

    unittest.main()
