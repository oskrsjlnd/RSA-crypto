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

    def generate_prime(self, bits=1024, rounds=40):
        while True:
            # p*q results in 1024 bit number so half of the bits required
            # for each prime
            prime_candidate = getrandbits(bits//2)

            # prime numbers after 2 must be odd
            if prime_candidate ^ 1 == prime_candidate + 1:
                prime_candidate += 1
            
            if self.k_prime_tests(prime_candidate, rounds):
                break

        return prime_candidate

    def k_prime_tests(self, prime_candidate, rounds):
        
        def prime_test(prime_candidate):
            # choose random integer 1 < a < prime_candidate
            a = randrange(2, prime_candidate-1)
            d = prime_candidate - 1
            max_div = 0

            # factor powers of 2 out from d and increase max divisions
            # to count the times d can be squared for the later loop
            while d ^ 1 != d + 1:
                d >>= 1
                max_div += 1
            
            b = pow(a, d, prime_candidate)
            # Fermat's little theorem if b is 1 or -1 then candidate is prime
            # (write -1 as prime_candidate-1)
            if b in (1, prime_candidate-1):
                return True

            # keep squaring d until it is larger than or equal to candidate - 1
            for _ in range(max_div-1):
                b = pow(a, d, prime_candidate)

                # remainder must be -1 atleast once or candidate is not prime
                if b == prime_candidate - 1:
                    return True
                d *= d
            return False

        # run Miller-Rabin for the determined amount of rounds to reach
        # higher probability of the probable prime being prime
        for _ in range(rounds):
            is_prime = prime_test(prime_candidate) 
            if not is_prime:
                return False
        return True
    
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
