from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from zipfile import ZipFile

key = b'mysecretpassword'
with open('myDES3key.key', 'wb') as mykey:
    mykey.write(key)
with open('myDES3key.key', 'rb') as mykey:
    key = mykey.read()

cipher = DES3.new(key, DES3.MODE_CBC)
with open('secret_message_2.txt', 'rb') as text:
    plaintext = text.read()

ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
print(ciphertext)

with open('DES3cipher_file.txt', 'wb') as c_file_aes:
    c_file_aes.write(cipher.iv)
    c_file_aes.write(ciphertext)

zipFileObj = ZipFile('important_file.zip', 'a')
zipFileObj.write('myDES3key.key')
zipFileObj.write('DES3cipher_file.txt')
zipFileObj.close()