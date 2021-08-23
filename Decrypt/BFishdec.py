from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad

with open('myBFishkey.key', 'rb') as mykey:
    key = mykey.read()

with open('Blowfishcipher_file.txt', 'rb') as dec_file:
    iv = dec_file.read(8)
    ciphertext = dec_file.read()

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
with open('secret_message.txt', 'ab') as cipher_file:
    message = cipher_file.write(plaintext)
    print("Data received in the file!!")
