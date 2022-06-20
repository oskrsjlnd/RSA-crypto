from key_gen_utils import KeyGenerator
from crypto import Crypt

class UI:
    def __init__(self, crypt: Crypt, keygen: KeyGenerator):
        self.crypt = crypt
        self.keygen = keygen
        self.encrypted_message = None

    def launch(self):
        print(">>> Welcome to the RSA cryptography program <<<\n")
        key_size = self.select_key_bit_size()
        self.key_pair = self.key_generation(key_size)

    def select_key_bit_size(self):
        print("Select bit size for keys from the following options:\n"
                "1 - 1024\n"
                "2 - 2048")
        while True:
            self.print_lines()
            key_bits = input(">>> ")
            if key_bits == "1":
                key_size = 1024
                break

            elif key_bits == "2":
                key_size = 2048
                break

            else:
                self.print_lines()
                print("Select 1 or 2.")
        self.print_lines()
        print(f"Keys of {key_size} bits generated.")
        return key_size

    def key_generation(self, bits):
        self.keygen.generate_keys(bits)

    def encrypt_user_message(self, public_key):
        while True:
            message = input("* Enter message to encrypt" +
            "\n* Max message length 120 characters" +
            "\n* Enter empty message to choose action again\n\n>>> ")
            message = fr"{message}"
            if len(message) > 120:
                print("\nMessage is too long.")
                self.print_lines()
                continue

            elif message == "":
                break

            else:
                self.print_lines()
                self.encrypted_message = self.crypt.encrypt_message(message, public_key)
                return self.encrypted_message[0]

    def decrypt_previous_message(self, private_key):
        decrypted = self.crypt.decrypt_message(self.encrypted_message, private_key)
        return decrypted

    def select_action(self):
        while True:
            self.print_lines()
            print("Options:\n"
            "enc - Encrypt message\n"
            "dec - Decrypt message\n"
            "showmsg - Show encrypted message\n"
            "gen - Generate new keys\n"
            "spub - Show public key\n"
            "spriv - Show private key\n"
            "quit - Quit program")
            self.print_lines()
            action = input(">>> ")
            self.print_lines()

            if action == "enc":
                encrypted = self.encrypt_user_message(self.keygen.get_public_key())
                if encrypted is not None:
                    print("Encrypted message: "
                    + str(encrypted))
                break

            elif action == "dec" and (self.encrypted_message is not None):
                print("Decrypted message: "
                + self.decrypt_previous_message(self.keygen.get_private_key()))
                break

            elif action == "dec" and (self.encrypted_message is None):
                print("No encrypted message found.\n")

            elif action == "gen":
                self.encrypted_message = None
                self.select_key_bit_size()
                break

            elif action == "quit":
                self.quit()
            
            elif action == "spub":
                public_key = self.keygen.get_public_key()
                print(f"Public key: {public_key}")

            elif action == "spriv":
                private_key = self.keygen.get_private_key()
                print(f"Private key: {private_key}")

            elif action == "showmsg":
                if self.encrypted_message is not None:
                    print(f"Encrypted message:\n> {self.encrypted_message[0]}")
                else:
                    print("No encrypted message to found.")

            else:
                print(">>Choose valid action<<")

    def quit(self):
        print("Shutting down")
        quit()

    def print_lines(self):
        print("----------------")

ui_obj = UI(Crypt(), KeyGenerator())
