import unittest
from src.crypt import Crypt
from src.key_gen_utils import KeyGenerator

class TestCrypt(unittest.TestCase):
    def setUp(self):
        self.crypt = Crypt()
        self.gen = KeyGenerator()
        self.gen.generate_keys()
    
    def test_str_conversion_to_int_works(self):
        result = self.crypt.str_to_int("This is a test")
        self.assertIsInstance(result, int)

    def test_encrypted_message_is_not_plaintext(self):
        public_key = self.gen.get_public_key()
        plaintext = """Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, 
        consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. 
        Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet."""
        int_ptext = self.crypt.str_to_int(plaintext)
        cipher = self.crypt.encrypt_message(plaintext, public_key)
        ciphertext = cipher[0]
        self.assertNotEqual(ciphertext, int_ptext)
    
    def test_message_decrypted_right_private_key_matches_original_plaintext(self):
        public_key = self.gen.get_public_key()
        plaintext = """alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku
        12alkuluku12alkuluku12alkuluk"""
        cipher = self.crypt.encrypt_message(plaintext, public_key)

        private_key = self.gen.get_private_key()
        decrypted_message = self.crypt.decrypt_message(cipher, private_key)
        self.assertEqual(plaintext, decrypted_message)

    def test_message_decrypted_wrong_private_key_not_matching_original(self):
        public_key = self.gen.get_public_key()
        plaintext = """alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku
        12alkuluku12alkuluku12"""
        cipher = self.crypt.encrypt_message(plaintext, public_key)

        private_key = self.gen.get_private_key()
        private_key = (private_key[0]-1, private_key[1])
        decrypted_message = self.crypt.decrypt_message(cipher, private_key)
        self.assertNotEqual(plaintext, decrypted_message)
