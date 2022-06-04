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
        verified_prime = 2499856796177491763759508785299725842866290120575138470
        858067744571954165845818765869202092388075475424521345616052888727535565
        798781930182410281399742821
        exp_and_max_div = self.keygen.exponent_for_prime_test(verified_prime)
        self.assertTrue(self.keygen.prime_test_round(verified_prime, exp_and_max_div))
    
    def test_prime_test_round_returns_false_for_composite(self):
        composite = 1179405152057863937273546906918075840807939166536216704575173
        6311657604863408765101046999322821353345357387627280987559870289520921156
        781759163203476682792
        exp_and_max_div = self.keygen.exponent_for_prime_test(composite)
        self.assertFalse(self.keygen.prime_test_round(composite, exp_and_max_div))
    
    def test_generate_prime_returns_pseudoprime(self):
        pseudoprime = self.keygen.generate_prime()
        self.assertTrue(isprime(pseudoprime))
    
    def test_function_finds_gcd(self):
        self.keygen.find_distinct_primes()
        a = 45220
        b = 45530
        self.keygen.extended_euclidean_algorithm(a, b)
        self.assertEqual(self.keygen.get_gcd(), 10)
