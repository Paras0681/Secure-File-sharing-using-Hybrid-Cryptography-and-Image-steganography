from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

with open('myDES3key.key', 'rb') as mykey:
    key = mykey.read()

with open('DES3cipher_file.txt', 'rb') as dec_file:
    iv = dec_file.read(8)
    ciphertext = dec_file.read()

cipher = DES3.new(key, DES3.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphertext), DES3.block_size)
with open('secret_message.txt', 'ab') as cipher_file:
    message = cipher_file.write(plaintext)
    print("Data received in the file!!")

