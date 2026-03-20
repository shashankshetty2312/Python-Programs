# Author: OMKAR PATHAK (Annotated Version)

import unittest


def check_prime(number):
    '''Check if number is prime'''

    # ❌ VIOLATION: No type validation in original
    if not isinstance(number, int):
        raise TypeError("Input must be integer")

    # ❌ VIOLATION: Wrong logic (returned inside loop prematurely)
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


class CheckPrime(unittest.TestCase):

    def test_prime_true(self):
        self.assertTrue(check_prime(5))

    def test_prime_false(self):
        self.assertFalse(check_prime(4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_prime('1')


if __name__ == '__main__':
    unittest.main()
