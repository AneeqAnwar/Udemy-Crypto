import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

# Alice and Bob share a secret key
secret_key = "secret key".encode()


# Alice wants to compute a MAC
m = "Hey Bob. You are still awesome".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
print(m, hmac)

# This is Eve
m = modify(m)

# Bob receives and valudates the HMAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
print(m, hmac)