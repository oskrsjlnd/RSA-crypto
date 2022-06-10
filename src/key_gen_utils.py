from random import randrange, getrandbits

class KeyGenerator:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def find_distinct_primes(self):
        prime_a = self.generate_prime()
        prime_b = self.generate_prime()
        while True:
            if prime_a != prime_b:
                break
            prime_b = self.generate_prime()
        return prime_a, prime_b

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
        max_divisions = exp_and_max_div[1]

        x = pow(a, d, prime_candidate)
        if x in (1, prime_candidate - 1):
            return True

        for _ in range(max_divisions - 1):
            if pow(x, 2, prime_candidate) == prime_candidate - 1:
                return True

        return False

    def gcd(self, a, b):
        gcd, remainder = a, b

        while remainder != 0:
            quotient = gcd//remainder
            gcd, remainder = remainder, gcd-quotient*remainder
        return gcd

    def generate_keys(self):
        primes = self.find_distinct_primes()
        gcd = self.gcd(primes[0]-1, primes[1]-1)
        carmichael_totient = (primes[0]-1)*(primes[1]-1)//gcd
        e = 65537
        d = pow(e, -1, carmichael_totient)
        n = primes[0]*primes[1]
        self.public_key = (n, e)
        self.private_key = (n, d)

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

# if __name__ == "__main__":
#     keygen = KeyGenerator()
#     keygen.generate_keys()
#     print(keygen.get_private_key(), keygen.get_public_key())
