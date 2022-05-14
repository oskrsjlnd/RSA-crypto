# Design document
## Subject and language
The purpose of this project is to implement the RSA cryptosystem with Python as the programming language of choice. The project language will be English.
## Algorithms and datastructures
The algorithms implemented for this project are:
- To generate secret keys we need to find out if a number is a prime number Miller-Rabin primality test is used as the time complexity is O(k log³ n).
- Prime numbers up to n must be generated and for this Sieve of Eratosthenes is used as the time complexity of this algorithm is O(n log log n) and space complexity O(n).
- For finding the greatest common divisor Extended Euclidean algorithm is used as the time complexity is O(log N) and the space complexity O(1).

No specific data structures will be used in this project since they would not have a notable impact on the efficiency of this program.

## Input
User has the options to input a message to be decrypted or the option to decrypt an encrypted message.

## Sources
[Extended Euclidean algorithm](https://iq.opengenus.org/extended-euclidean-algorithm/)
[RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
[Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

Currently a BSc Computer Science student.
