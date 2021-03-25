def generateKey(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    counter = 0
    for c in letters:
        key[c] = letters[(counter + n) % len(letters)]
        counter += 1
    return key

def get_decryption_key(key):
    decryptionKey = {}
    for c in key:
        decryptionKey[key[c]] = c
    return decryptionKey

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

# this is done by your enemy
key = generateKey(3)
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)

# this is us breaking the cipher
print(cipher)
for i in range(26):
    decryptionKey = generateKey(i)
    message = encrypt(decryptionKey, cipher)
    print(message)