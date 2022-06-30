## Structure
The program consists of three classes:
- User interface
- Key generation
    - k_prime_tests(prime_candidate) tests the given parameter for primality time complexity O(k*log³n)
    - gcd(a,b) returns the greatest common divisor for the two parameters time complexity O(log n)
    - generate_prime(bits) in theory never stops since candidate is randomly picked
    - other functions to help with prime generation
- Encryption / decryption
    - encrypt_message for encrypting the given message with the given public key
    - decrypt message for decrypting the given cipher with the given private key

## Future improvements
- Add OAEP scheme
- Save key pairs to a file

## Sources
[RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
[Carmichael](https://en.wikipedia.org/wiki/Carmichael_function#Carmichael's_theorem)
[Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
[Miller-Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
