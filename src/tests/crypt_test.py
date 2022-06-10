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
        12alkuluku12alkuluku12alkuluk"""
        cipher = self.crypt.encrypt_message(plaintext, public_key)

        private_key = (104814702874370331090619032161718490599524181508127845244251677594602939189776497897327399447466258336136479754269538317230941834678307977128151892594647934461644941830568360535951400021200023871769182539960353422729285052223286117059755939100902858773850302376516742750647549857457064789876021104569249546285, 32043996319497138314717532514338338307399888623172398909224203309359056557461615757066264481581914827087454542572050440576150122825496721390049152692774548766363377153796513136744182415737960080585183495136887944385424330783315658962967446681634672225953745072768257516494678233288502410512571480568851500243)
        decrypted_message = self.crypt.decrypt_message(cipher, private_key)
        self.assertNotEqual(plaintext, decrypted_message)
