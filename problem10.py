n = 2_000_000
sum, sieve = 0, [True] * n
for i in range(2, n):
    if sieve[i]:
        sum += i
        for j in range(i ** 2, n, i):
            sieve[i] = False
print(sum)