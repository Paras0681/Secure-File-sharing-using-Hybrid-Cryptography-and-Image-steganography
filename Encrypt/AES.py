from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from zipfile import ZipFile

key = b'mysecretpassword'
with open('myAESkey.key', 'wb') as mykey:
    mykey.write(key)
with open('myAESkey.key', 'rb') as mykey:
    key = mykey.read()

cipher = AES.new(key, AES.MODE_CBC)
with open('secret_message_1.txt', 'rb') as text:
    plaintext = text.read()

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print(cipher.iv)
print(ciphertext)

with open('AEScipher_file.txt', 'wb') as c_file_aes:
    c_file_aes.write(cipher.iv)
    c_file_aes.write(ciphertext)

zipFileObj = ZipFile('important_file.zip', 'w')
zipFileObj.write('myAESkey.key')
zipFileObj.write('AEScipher_file.txt')
zipFileObj.close()

