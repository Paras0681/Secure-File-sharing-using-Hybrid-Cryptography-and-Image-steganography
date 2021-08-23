from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

with open('myAESkey.key', 'rb') as mykey:
    key = mykey.read()

with open('AEScipher_file.txt', 'rb') as dec_file:
    iv = dec_file.read(16)
    ciphertext = dec_file.read()

cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
with open('secret_message.txt', 'ab') as cipher_file:
    message = cipher_file.write(plaintext)
    print("Data received in the file!!")