import unittest
from CipherAlphabet import CipherAlphabet
from VigenereCipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        # Setup a default CipherAlphabet and VigenereCipher before each test
        self.alphabet = CipherAlphabet('a', 'z')  # Assuming ASCII range for simplicity
        self.cipher = VigenereCipher(self.alphabet)

    def test_encrypt_single_character(self):
        # Test encryption of a single character
        encrypted = self.cipher.encrypt('a', 'b')
        self.assertEqual(encrypted, 'b')

    def test_decrypt_single_character(self):
        # Test decryption of a single character
        decrypted = self.cipher.decrypt('b', 'b')
        self.assertEqual(decrypted, 'a')

    def test_encrypt_with_wraparound(self):
        # Test encryption with wraparound (e.g., 'z' with key 'b' wraps to 'a')
        encrypted = self.cipher.encrypt('z', 'b')
        self.assertEqual(encrypted, 'a')

    def test_decrypt_with_wraparound(self):
        # Test decryption with wraparound
        decrypted = self.cipher.decrypt('a', 'b')
        self.assertEqual(decrypted, 'z')

    def test_encrypt_phrase(self):
        # Test encryption of a phrase
        encrypted = self.cipher.encrypt('abc', 'bc')
        self.assertEqual(encrypted, 'bdd')

    def test_decrypt_phrase(self):
        # Test decryption of a phrase
        decrypted = self.cipher.decrypt('bdd', 'bc')
        self.assertEqual(decrypted, 'abc')

    def test_encrypt_with_non_alphabet_characters(self):
        # Test encryption ignoring non-alphabet characters
        encrypted = self.cipher.encrypt('abc!', 'bc')
        self.assertEqual(encrypted, 'bdd')

    def test_decrypt_with_non_alphabet_characters(self):
        # Test decryption ignoring non-alphabet characters
        decrypted = self.cipher.decrypt('bdd!', 'bc')
        self.assertEqual(decrypted, 'abc')


if __name__ == '__main__':
    unittest.main()
