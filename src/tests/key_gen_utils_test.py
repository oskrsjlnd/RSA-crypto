import unittest
from sympy import primerange
from src.key_gen_utils import KeyGenUtilities

class TestKeyGenUtilities(unittest.TestCase):
    def setUp(self):
        self.keygen_utils = KeyGenUtilities()

    def test_constructor_creates_keygen_utils(self):
        self.assertSetEqual(self.keygen_utils.low_primes, set())

    def test_find_all_primes_gives_correct_primes(self):
        self.keygen_utils.find_all_primes(8000)
        primes = set(primerange(0, 8000))
        self.assertSetEqual(self.keygen_utils.low_primes, primes)
    
    def test_get_low_primes_returns_set(self):
        self.keygen_utils.find_all_primes(20)
        low_primes = self.keygen_utils.get_low_primes()
        self.assertIsInstance(low_primes, set)
