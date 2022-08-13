# JCryptor

* `JCryptor` is used to `Encrypt` and `Decrypt`.
* `JCryptor` latest version [0.1.50](https://github.com/ScripNewbie/JCryptor/tree/main)


# How to Use?

## Encrypting:
### Code
```python
from jcryptor import JCryptor

cryptor = JCryptor()

encrypt = cryptor.encrypt_text(original_text, print_it=True)
```
### Result
```python
>> %tpp9 !9>pF
```

## Decrypting:
### Code
```python
from jcryptor import JCryptor

cryptor = JCryptor()
original_text = "Hello World"
encrypt = cryptor.encrypt_text(original_text)
decrypt = cryptor.decrypt_text(encrypt, print_it=True)
```
### Result
```
>> Hello World
```
 
# How to install?
 
**On Windows:**
```
$ pip install JCryptor
$ pip install jcryptor==[0.1.50](https://github.com/ScripNewbie/JCryptor/tree/main)
```
