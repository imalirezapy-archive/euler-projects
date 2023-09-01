def is_prime(x):
    avval = True
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            avval = False
            break
    return avval
def nom_prime():
    x = int(input("enter number: "))
    primes = 0
    i = 0
    while  True:
        i += 1
        if is_prime(i):
            primes += 1
            if primes > x:
                print(i)
                break

nom_prime()