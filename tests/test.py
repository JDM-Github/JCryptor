from jcryptor import JCryptor

cryptor = JCryptor(generate=True)

encrypted_text = cryptor.encrypt_text(print_it=True)
decrypted_text = cryptor.decrypt_text(encrypted_text, print_it=True)
