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

    def test_prime_test_returns_true_for_prime_1(self):
        verified_prime = 2499856796177491763759508785299725842866290120575138470858067744571954165845818765869202092388075475424521345616052888727535565798781930182410281399742821
        exp_and_max_div = self.keygen.exponent_for_prime_test(verified_prime)
        is_prime = True
        for _ in range(40):
            if not self.keygen.prime_test_round(verified_prime, exp_and_max_div):
                is_prime = False
                break
        self.assertTrue(is_prime)

    def test_prime_test_returns_true_for_prime_2(self):
        verified_prime = 64135289477071580278790190170577389084825014742943447208116859632024532344630238623598752668347708737661925585694639798853367
        exp_and_max_div = self.keygen.exponent_for_prime_test(verified_prime)
        is_prime = True
        for _ in range(40):
            if not self.keygen.prime_test_round(verified_prime, exp_and_max_div):
                is_prime = False
                break
        self.assertTrue(is_prime)
    
    def test_prime_test_returns_true_for_prime_3(self):
        verified_prime = 33372027594978156556226010605355114227940760344767554666784520987023841729210037080257448673296881877565718986258036932062711
        exp_and_max_div = self.keygen.exponent_for_prime_test(verified_prime)
        is_prime = True
        for _ in range(40):
            if not self.keygen.prime_test_round(verified_prime, exp_and_max_div):
                is_prime = False
                break
        self.assertTrue(is_prime)

    def test_prime_test_false_for_semiprime_1(self):
        semiprime = 2140324650240744961264423072839333563008614715144755017797754920881418023447140136643345519095804679610992851872470914587687396261921557363047454770520805119056493106687691590019759405693457452230589325976697471681738069364894699871578494975937497937
        exp_and_max_div = self.keygen.exponent_for_prime_test(semiprime)
        is_prime = True
        for _ in range(40):
            if not self.keygen.prime_test_round(semiprime, exp_and_max_div):
                is_prime = False
                break
        self.assertFalse(is_prime)
    
    def test_prime_test_false_for_semiprime_2(self):
        semiprime = 1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413
        exp_and_max_div = self.keygen.exponent_for_prime_test(semiprime)
        is_prime = True
        for _ in range(40):
            if not self.keygen.prime_test_round(semiprime, exp_and_max_div):
                is_prime = False
                break
        self.assertFalse(is_prime)

    def test_prime_test_returns_false_for_composite(self):
        composite = 11794051520578639372735469069180758408079391665362167045751736311657604863408765101046999322821353345357387627280987559870289520921156781759163203476682792
        exp_and_max_div = self.keygen.exponent_for_prime_test(composite)
        is_prime = True
        for _ in range(40):
            if not self.keygen.prime_test_round(composite, exp_and_max_div):
                is_prime = False
                break
        self.assertFalse(is_prime)

    def test_generate_prime_returns_pseudoprime(self):
        pseudoprime = self.keygen.generate_prime()
        self.assertTrue(isprime(pseudoprime))

    def test_function_finds_valid_gcd(self):
        a = 45220
        b = 45530
        gcd = self.keygen.gcd(a, b)
        self.assertEqual(gcd, 10)
