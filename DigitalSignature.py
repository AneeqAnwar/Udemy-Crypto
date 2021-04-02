import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


# These are Alice's RSA keys
# Public key (e,n): 3 209683
# Secret key (d): 34795
n = 209683
e = 3
d = 34795

message = "Bob you are awesome".encode()

# Step 1: Hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, 'big') % n
print("Hash value", h)
# Step 2: decrypt the hash value (use secret component)
sign = h**d % n
# Step 3: send message with signature to Bob
print(message, sign)


# This is Eve, modifying message
message = modify(message)
print(message)

# Bob verifying the signature
# Step 1: calculate the hash value of the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, 'big') % n
print("Hash value", h)
# Step 2: verify the signature
verification = sign**e % n
print("Verification value", verification)