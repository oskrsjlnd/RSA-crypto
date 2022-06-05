# Test document
## Unit testing
- Unit tests for KeyGenerator class are located in key_gen_utils_test.py.
- Each functionality is tested separately.
## Test coverage
![coverage_tira](https://user-images.githubusercontent.com/80696138/172052448-1bd1a8ec-8e9e-471a-a7bb-d06fe6a08a99.png)
[![codecov](https://codecov.io/gh/oskrsjlnd/RSA-crypto/branch/main/graph/badge.svg?token=KGXKLCTU0Q)](https://codecov.io/gh/oskrsjlnd/RSA-crypto)

## Test input
The prime test function was tested with a large verified prime number and a composite number.
Same goes for extended euclidean algorithm. Tests were also done for the constructor helper
functions.

## Repeating the tests
Tests can be repeated with:
``poetry install; poetry shell; coverage run --branch -m pytest; coverage report -m``
