def enumerate_prime(n):
    prime = [2]
    for i in range(2,n):
        count = 0
        for j in prime:
            if i % j == 0:
                count += 1
                break
        if count == 0:
            prime.append(i)
    return prime


print(enumerate_prime(201))