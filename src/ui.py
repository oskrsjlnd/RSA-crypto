from src.key_gen_utils import KeyGenerator
from src.crypto import Crypt

class UI:
    def __init__(self, crypt: Crypt, keygen: KeyGenerator):
        self.crypt = crypt
        self.keygen = keygen
        self.key_pair = None
        self.encrypted_message = None

    def launch(self):
        print(">>> Welcome to the RSA cryptography program <<<\n")
        key_size = self.select_key_bit_size()
        self.key_pair = self.key_generation(key_size)

    def select_key_bit_size(self):
        print("Select bit size for keys from the following options:\n"
                "1 - 1024\n"
                "2 - 2048\n")
        while True:
            key_bits = input("Select 1 or 2 and press Enter: ")
            if key_bits == "1":
                key_size = 1024
                break

            elif key_bits == "2":
                key_size = 2048
                break

            else:
                print("Invalid input.\n")

        print(f"Key size is {key_size} bits.\n")
        return key_size

    def key_generation(self, bits):
        keys = self.keygen.generate_keys(bits)
        return keys

    def encrypt_user_message(self, public_key):
        while True:
            message = input("Enter message to encrypt, max length 120"
            + "characters or type back to choose action again:\n")

            if len(message) > 120:
                continue

            elif message == "back":
                return None

            else:
                print("Encrypting message...")
                self.encrypted_message = self.crypt.encrypt_message(message, public_key)
                return self.encrypted_message[0]

    def decrypt_previous_message(self, private_key):
        print("Decrypting message...")
        decrypted = self.crypt.decrypt_message(self.encrypted_message, private_key)
        return decrypted

    def select_action(self):
        while True:
            print("Options:\n"
            "1 - Encrypt message\n"
            "2 - Decrypt message\n"
            "3 - Generate new keys\n"
            "quit - Quit program\n")
            action = input("Action: ")

            if action == "1":
                print("\nEncrypted message: "
                + str(self.encrypt_user_message(self.keygen.get_public_key()))
                + "\n")
                break

            elif action == "2" and (self.encrypted_message is not None):
                print("\nDecrypted message: "
                + self.decrypt_previous_message(self.keygen.get_private_key())
                + "\n")
                break

            elif action == "3":
                self.select_key_bit_size()
                break

            elif action == "quit":
                self.quit()

            print("Choose valid action.\n")

    def quit(self):
        print("Shut down...")
        quit()

if __name__ == "__main__":
    io = IO(Crypt(), KeyGenerator())
    io.launch()
    while True:
        io.select_action()
