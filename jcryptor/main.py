# Made By CodeBoard
"""
Encryptor and Decryptor Library
"""
import ast
from random import sample
from typing import get_type_hints
import string


class JCryptor:
    """
    :class:`JCryptor`

    Encrypt and Decrypt Text.

    - Use to encrypt some message, text, string, etc
    - Use to decrypt some message, text, string, etc
    - Can use own or generated key to encrypt/decrypt
    - Can generate new random key
    - Can save or open a key in a file

    Note:
        if character is not in the key dictionary, it will stay the same
        in encryption, the same goes with decryption.
    """

    def __init__(self, generate: bool = True) -> None:
        """Initiliaze the :class:`JCryptor`.

        Args:
            :bool:`generate` (bool, optional): Generate a key. Defaults to True.
        """
        self._key = dict()
        if generate:
            self.generate_new_key()

    def generate_new_key(self):
        """
        Generate New Key.
        - Using ASCII

        Note:
            - Will support more ascii character in future.
        """
        _letters = list(string.ascii_letters)
        _numbers = [str(i) for i in range(10)]
        _special_chr = [i for i in "!@#$%^&*()_+-/}[]|\\~`.,:;\"'<>?"]
        _all_chr = _letters + _numbers + _special_chr
        _key_s_chr = dict(zip(string.ascii_lowercase, sample(_all_chr, 26)))
        _all_chr = [i for i in _all_chr if i not in _key_s_chr.values()]
        _key_b_chr = dict(zip(string.ascii_uppercase, sample(_all_chr, 26)))
        _all_chr = [i for i in _all_chr if i not in _key_b_chr.values()]
        _key_ord = dict(zip(_numbers, sample(_all_chr, len(_numbers))))
        _all_chr = [i for i in _all_chr if i not in _key_ord.values()]
        _key_spc = dict(zip(_special_chr, sample(_all_chr, len(_special_chr))))
        self._key = {**_key_s_chr, **_key_b_chr, **_key_ord, **_key_spc}

    def check_duplicate(self, text: str) -> str:
        """Check if there is a duplicate character in string

        Args:
            :str:`text` (str): String

        Returns:
            :str:`str` Duplicate character | None
        """
        for t in text:
            if text.count(t) > 1:
                return t
        return "None"

    def set_key(self, key: dict):
        """Set key using own dictionary.

        Args:
            :dict:`key` (dict): Key Dict
        """
        self._key = key

    def get_key(self) -> dict:
        """Get the current key.

        Returns:
            :dict:`dict`: Key Dict
        """
        return self._key

    def set_using_file(self, filename: str = "key.txt"):
        """Set the key using a file.

        Args:
            :str:`filename` (str, optional): Filename. Defaults to "key.txt".
        """
        with open(filename, "r") as f:
            self._key = ast.literal_eval(str(f.read()))

    def save_key(self, filename: str = "key.txt"):
        """Save the current key in a file.

        Args:
            :str:`filename` (str, optional): String. Defaults to "key.txt".
        """
        with open(filename, "w") as f:
            f.write(str(self._key))

    def encrypt_text(self, text: str = "Hello World", print_it: bool = False) -> str:
        """Encrypt The Text
        - this will encrypt the text.

        Args:
            :str:`text` (str, optional): String. Defaults to "Hello World".
            :bool:`print_it` (bool, optional): Print the encrypted value. Defaults to False.

        Returns:
            :str:`str`: Encrypted Text
        """
        result = str()
        for t in str(text):
            adder = self._key.get(t) if self._key.get(t) is not None else t
            result += adder
        if print_it:
            print(result)
        return result

    def decrypt_text(self, text: str, print_it: bool = False) -> str:
        """Decrypt The Text
        - this will decrypt the encryted text.

        Args:
            :str:`text` (str): Decrypted Text
            :bool:`print_it` (bool, optional): Print the decrypted value. Defaults to False.

        Returns:
            :str:`str`: Decrypted Text
        """
        result = str()
        all_key = list(self._key.keys())
        all_val = list(self._key.values())
        for t in text:
            try:
                result += all_key[all_val.index(t)]
            except ValueError:
                result += t
        if print_it:
            print(result)
        return result
