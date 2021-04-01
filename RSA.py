import math
import random


def is_prime(p):
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


def get_prime(size):
    while True:
        p = random.randrange(size, 2 * size)
        if is_prime(p):
            return p


def lcm(a, b):
    return (a*b)//math.gcd(a, b)


def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False


def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False


def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n//p


# Key generation done by Alice
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated primes", p, q)

# Step 2: Calculate n = p*q
n = p*q
print("Modulus n:", n)

# Step 3: Calculate lambda(n) (lcm(n) = lambda(n) = lcm(lambda(p), lambda(q)), lambda(p)=p-1, lcm(a,b) = |ab|/gcd(a,b)
lambda_n = lcm(p-1, q-1)
print("Lambda n", lambda_n)

# Step 4: Choose an integer e such that 1 < e < lambda(n) and gcd(e, lambda(n)) = 1
e = get_e(lambda_n)
print("Public component:", e)

# Step 5: Solve for d the equation d.e = 1 (mod lambda(n))
d = get_d(e, lambda_n)
print("Secret exponent:", d)

# Done with key generation
print("Public key (e,n):", e, n)
print("Secret key (d):", d)

# Bob wanting to send a message
m = 117
c = m**e % n
print("Bob sends", c)

# Alice decrypting the cipher
m = c**d % n
print("Alice message", m)


# This is Eve
print("Eve sees the following:")
print("   Public key (e, n)", e, n)
print("   Encrypted cipher", c)

p, q = factor(n)
print("Eve: Factors", p, q)

lambda_n = lcm(p-1, q-1)
print("Eve: Lambda n", lambda_n)

d = get_d(e, lambda_n)
print("Eve: Secret exponent:", d)

m = c**d % n
print("Eve: message", m)


# This is Bob not being careful
print("This is Bob not being careful")
message = "Alice is awesome"
for m_c in message:
    c = ord(m_c)**e % n
    print(c, " ", end='')
print()