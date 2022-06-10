class Crypt:
    def encrypt_message(self, plaintext, public_key):
        n = public_key[0]
        e = public_key[1]
        bytesize = self.size_as_bytes_for_conversion(plaintext)
        plaintext_as_int = self.str_to_int(plaintext)
        ciphertext = pow(plaintext_as_int, e, n)
        return ciphertext, bytesize

    def decrypt_message(self, cipher, private_key):
        n = private_key[0]
        d = private_key[1]
        ciphertext, size_for_conversion = cipher[0], cipher[1]
        plaintext_as_int = pow(ciphertext, d, n)
        plaintext = self.int_to_str(plaintext_as_int, size_for_conversion)
        return plaintext
    
    def str_to_int(self, text):
        return int.from_bytes(text.encode(), "big")
    
    def int_to_str(self, text, size):
        return text.to_bytes(size, "big").decode()

    def size_as_bytes_for_conversion(self, text):
        return len(text.encode())
