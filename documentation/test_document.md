# Test document
## Unit testing
- Unit tests for KeyGenerator class are located in key_gen_utils_test.py.
- Unit tests for Crypt class are located in crypt_test.py
- Each functionality is tested separately.
- String and int conversion functions were tested separately.

## Test coverage
![coverage_tira](https://user-images.githubusercontent.com/80696138/173233215-faa8d6aa-452d-43a0-9268-669b2fe70137.png)
[![codecov](https://codecov.io/gh/oskrsjlnd/RSA-crypto/branch/main/graph/badge.svg?token=KGXKLCTU0Q)](https://codecov.io/gh/oskrsjlnd/RSA-crypto)

## Test input
The prime test function was tested with several large verified prime numbers to find out if the algorithm
returns True for prime numbers. Tests were also done to verify the prime test returns False for semiprimes
and a composite number.
Greatest common divisor function was tested with 2 numbers and their verified gcd to see whether the returned
value is correct or not.
Encryption was tested to see if the encrypt function actually creates a ciphertext not matching the original
plaintext. The function was also tested to see whether it actually executes correctly with 50 randomly
generated plaintext unicode strings created with code:
![test_data](https://user-images.githubusercontent.com/80696138/173233195-f6f1e3cb-37d2-4533-b819-c50061c16356.png)


Decryption was tested to see if the message matches the original plaintext after decryption when algorithm
is called with the correct private key. Similarly the function was tested to verify that the function
does not decrypt message when called with incorrect private key.

## Repeating the tests
Tests can be repeated with:
``poetry install; poetry shell; coverage run --branch -m pytest; coverage report -m``
