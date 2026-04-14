# test_prime.py

import unittest


def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be integer")

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class TestPrime(unittest.TestCase):

    def test_prime_true(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_prime_false(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_prime("abc")


if __name__ == "__main__":
    unittest.main()
