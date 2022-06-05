from random import randrange, getrandbits

class KeyGenerator:
    def __init__(self):
        self.coefficients = None
        self.gcd = None
        self.prime_pair = None
    
    def find_distinct_primes(self):
        prime_a = self.generate_prime()
        prime_b = self.generate_prime()
        while True:
            if prime_a != prime_b:
                break
            prime_b = self.generate_prime()
        self.prime_pair = (prime_a, prime_b)
    
    def exponent_for_prime_test(self, prime_candidate):
        d = prime_candidate - 1
        max_divisions = 0
        while d ^ 1 == d + 1:
            d >>= 1
            max_divisions += 1
        return (d, max_divisions)

    def generate_prime(self, bits=1024, rounds=40):
        while True:
            prime_candidate = getrandbits(bits//2)
            if prime_candidate % 2 == 0:
                prime_candidate += 1
            is_prime = True
            exp_and_max_div = self.exponent_for_prime_test(prime_candidate)

            for _ in range(rounds):
                if not self.prime_test_round(prime_candidate, exp_and_max_div):
                    is_prime = False

            if is_prime:
                return prime_candidate          
    
    def prime_test_round(self, prime_candidate, exp_and_max_div):
        a = randrange(2, prime_candidate-1)
        d = exp_and_max_div[0]
        max_div_by_two = exp_and_max_div[1]

        x = pow(a, d, prime_candidate)
        if x == 1 or x == prime_candidate - 1:
            return True

        for _ in range(max_div_by_two - 1):
            if pow(x, 2, prime_candidate) == prime_candidate - 1:
                return True
                
        return False
    
    def extended_euclidean_algorithm(self, a, b):
        gcd, remainder = a, b
        coefficient_1, s = 1, 0
        coefficient_2, t = 0, 1

        while remainder != 0:
            quotient = gcd//remainder
            gcd, remainder = remainder, gcd-quotient*remainder
            coefficient_1, s = s, coefficient_1-quotient*s
            coefficient_2, t = t, coefficient_2-quotient*t
        
        self.coefficients = (coefficient_1, coefficient_2)
        self.gcd = gcd

    def get_gcd(self):
        return self.gcd
    
    def get_coefficients(self):
        return self.coefficients
    
    def get_prime_pair(self):
        return self.prime_pair
