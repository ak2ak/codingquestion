def repeated_string(s, n):
    s = list(s)
    if 'a' not in s:
        return 0
    di = {'a': 0}
    temp = n // len(s)
    di['a'] = s.count('a') * temp
    if n % len(s):
        temp = n % len(s)
        for i in range(temp):
            if i != 'a':
                continue
            di[s[i]] += 1
    return di['a']


print(repeated_string('cea', 817723))

