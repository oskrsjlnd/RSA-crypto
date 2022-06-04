import unittest
from sympy import isprime
from src.key_gen_utils import KeyGenerator

class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.keygen = KeyGenerator()
    
    def test_constructor_creates_generator(self):
        self.assertEqual(self.keygen.prime_pair, None)
        self.assertEqual(self.keygen.gcd, None)
        self.assertEqual(self.keygen.coefficients, None)
    
    def test_primes_are_distinct(self):
        self.keygen.find_distinct_primes()
        prime_a = self.keygen.prime_pair[0]
        prime_b = self.keygen.prime_pair[1]
        self.assertNotEqual(prime_a, prime_b)
    
    def test_prime_test_round_returns_true_for_prime(self):
        verified_prime_1 = """249985679617749176375950878529972584286629012057
        5138470858067744571954165845818765869202092388075475424521345616052888
        727535565798781930182410281399742821"""
        self.assertTrue(self.keygen.prime_test_round(int(verified_prime_1)))
    
    def test_prime_test_round_returns_false_for_composite(self):
        composite = """11794051520578639372735469069180758408079391665362167045
        75173631165760486340876510104699932282135334535738762728098755987028952
        0921156781759163203476682792"""
        self.assertFalse(self.keygen.prime_test_round(int(composite)))
    
    def test_generate_prime_returns_pseudoprime(self):
        pseudoprime = self.keygen.generate_prime()
        self.assertTrue(isprime(pseudoprime))
    
    def test_function_finds_gcd(self):
        self.keygen.find_distinct_primes()
        a = 45220
        b = 45530
        gcd = self.keygen.extended_euclidean_algorithm(a, b)
        self.assertEqual(gcd, 10)
