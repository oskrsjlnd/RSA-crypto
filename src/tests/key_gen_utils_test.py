import unittest
from sympy import isprime
from src.key_gen_utils import KeyGenerator

class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self.keygen = KeyGenerator()

    def test_constructor_creates_generator(self):
        self.assertIsNone(self.keygen.public_key)
        self.assertIsNone(self.keygen.private_key)

    def test_primes_are_distinct(self):
        primes = self.keygen.find_distinct_primes()
        self.assertNotEqual(primes[0], primes[1])

    def test_exp_and_max_div_returns_correct_values(self):
        exp_and_max_div = self.keygen.exponent_for_prime_test(199)
        self.assertEqual(exp_and_max_div, (99, 1))

    def test_prime_test_round_returns_true_for_prime(self):
        verified_prime = 2499856796177491763759508785299725842866290120575138470858067744571954165845818765869202092388075475424521345616052888727535565798781930182410281399742821
        exp_and_max_div = self.keygen.exponent_for_prime_test(verified_prime)
        self.assertTrue(self.keygen.prime_test_round(verified_prime, exp_and_max_div))

    def test_prime_test_round_returns_false_for_composite(self):
        composite = 11794051520578639372735469069180758408079391665362167045751736311657604863408765101046999322821353345357387627280987559870289520921156781759163203476682792
        exp_and_max_div = self.keygen.exponent_for_prime_test(composite)
        self.assertFalse(self.keygen.prime_test_round(composite, exp_and_max_div))

    def test_generate_prime_returns_pseudoprime(self):
        pseudoprime = self.keygen.generate_prime()
        self.assertTrue(isprime(pseudoprime))

    def test_function_finds_valid_gcd(self):
        a = 45220
        b = 45530
        gcd = self.keygen.gcd(a, b)
        self.assertEqual(gcd, 10)
