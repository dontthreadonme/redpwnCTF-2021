n = 228430203128652625114739053365339856393
e = 65537
crypt = 126721104148692049427127809839057445790
p = 12546190522253739887
q = 18207136478875858439


def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm


totient = compute_lcm((q - 1), (p - 1))
d = pow(e, -1, totient)

plain = pow(crypt, d, n)

print("msg =", plain.to_bytes(16, 'big'))
