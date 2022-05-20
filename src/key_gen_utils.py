class KeyGenUtilities:
    def __init__(self):
        self.low_primes = set()

    def find_all_primes(self, upper_limit):
        is_prime = [False, False, True]
        for i in range(3, upper_limit+2):
            if i%2 == 0:
                is_prime.append(False)
            else:
                is_prime.append(True)

        i = 3
        while True:
            if i*i >= upper_limit+1:
                break
            if i%2 == 0:
                i += 1
                continue
            if is_prime[i]:
                for j in range(i*i, upper_limit+1, i):
                    is_prime[j] = False
            i += 1

        for i in range(2, upper_limit+1):
            if is_prime[i]:
                self.low_primes.add(i)
