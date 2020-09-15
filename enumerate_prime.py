from datetime import datetime


def enumerate_prime(n):
    prime = [2]
    for i in range(2, n):
        count = 0
        temp = int(i ** (1 / 2)) + 1
        for j in prime:
            if j > temp:
                break
            if i % j == 0:
                count += 1
                break
        if count == 0:
            prime.append(i)
    return prime


def generate_prime(n):
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]
    if_prime = [True] * size
    for i in range(size):
        if if_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            for j in range(2 * i ** 2 + 6 * i + 3, size, p):
                if_prime[j] = False
    return primes


a = datetime.now()
print(len(enumerate_prime(1878)))
print((datetime.now() - a))

b = datetime.now()
print(len(generate_prime(1878)))
print(datetime.now()-b)
