from simplecrypt import encrypt, decrypt
password = 'secret'
message = 'this is a secret message'
ciphertext = encrypt(password, message)

print(ciphertext)
