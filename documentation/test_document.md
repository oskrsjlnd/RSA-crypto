# Test document
## Unit testing
- Unit tests for KeyGenerator class are located in key_gen_utils_test.py.
- Unit tests for Crypt class are located in crypt_test.py
- Each functionality is tested separately.
- String and int conversion functions were tested separately.

## Test coverage
![coverage report](https://user-images.githubusercontent.com/80696138/176777060-c5df1c01-94c8-4610-b674-a87767a93821.png)
[![codecov](https://codecov.io/gh/oskrsjlnd/RSA-crypto/branch/main/graph/badge.svg?token=KGXKLCTU0Q)](https://codecov.io/gh/oskrsjlnd/RSA-crypto)

## Test input
The prime test function was tested with 100 large primenumbers generated using the sympy library to find out
if the algorithm returns True for prime numbers. Tests were also done to verify the prime test returns False
for 100 composite numbers generated with the help of the same library. Few tests were also done to check the
algorithm works for verified primes and for semiprimes.
Greatest common divisor function was tested with 8 pairs and their verified gcd to see whether the returned
value is correct or not.
Encryption was tested to see if the encrypt function actually creates a ciphertext not matching the original
plaintext. The function was also tested to see whether it actually executes correctly with 50 randomly
generated plaintext ASCII -strings. The case of too long message was also tested.
Decryption was tested to see if the message matches the original plaintext after decryption when algorithm
is called with the correct private key. Similarly the function was tested to verify that the function
does not decrypt message when called with incorrect private key.

## Performance tests
![performance](https://user-images.githubusercontent.com/80696138/174592098-02ff3549-d6c1-45b0-bcbd-3a3f9fbb0053.png)
- Performance tests for Miller-Rabin implementation was done with 50 generated 512-bit prime numbers to get the average speed.
- generate_prime() -method was run and timed 50 times to get the average speed of the algorithm.
- gcd() was tested with 25 prime pairs.
These tests show that the performance is at the expected level.

## Repeating the tests
Tests can be repeated with:
``poetry install; poetry shell; coverage run --branch -m pytest; coverage report -m``
