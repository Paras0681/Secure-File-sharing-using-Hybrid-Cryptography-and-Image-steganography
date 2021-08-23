from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from zipfile import ZipFile

key = b'mysecretpassword'
with open('myBFishkey.key', 'wb') as mykey:
    mykey.write(key)
with open('myBFishkey.key', 'rb') as mykey:
    key = mykey.read()

cipher = Blowfish.new(key, Blowfish.MODE_CBC)
with open('secret_message_3.txt', 'rb') as text:
    plaintext = text.read()

ciphertext = cipher.encrypt(pad(plaintext, Blowfish.block_size))
print(cipher.iv)
print(ciphertext)

with open('Blowfishcipher_file.txt', 'wb') as c_file_bf:
    c_file_bf.write(cipher.iv)
    c_file_bf.write(ciphertext)

zipFileObj = ZipFile('important_file.zip', 'a')
zipFileObj.write('myBFishkey.key')
zipFileObj.write('Blowfishcipher_file.txt')
zipFileObj.close()


