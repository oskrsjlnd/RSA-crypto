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

    def generate_prime(self, bits=1024, rounds=40):
        while True:
            prime_candidate = getrandbits(bits//2)
            if prime_candidate % 2 == 0:
                prime_candidate += 1
            is_prime = True

            d = prime_candidate - 1
            max_div_by_two = 0
            while d ^ 1 == d + 1:
                d >>= 1
                max_div_by_two += 1

            for _ in range(rounds):
                if not self.prime_test_round(prime_candidate, d, max_div_by_two):
                    is_prime = False

            if is_prime:
                return prime_candidate          
    
    def prime_test_round(self, prime_candidate, d, max_div_by_two):
        a = randrange(2, prime_candidate-1)
        x = pow(a, d, prime_candidate)
        if x == 1 or x == prime_candidate - 1:
            return True

        for _ in range(max_div_by_two - 1):
            if pow(x, 2, prime_candidate) == prime_candidate - 1:
                return True
                
        return False
    
    def extended_euclidean_algorithm(self, a, b):
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1

        while r != 0:
            quotient = old_r//r
            old_r, r = r, old_r-quotient*r
            old_s, s = s, old_s-quotient*s
            old_t, t = t, old_t-quotient*t
        
        self.coefficients = (old_s, old_t)
        self.gcd = old_r

    def get_gcd(self):
        return self.gcd
    
    def get_coefficients(self):
        return self.coefficients
    
    def get_prime_pair(self):
        return self.prime_pair
