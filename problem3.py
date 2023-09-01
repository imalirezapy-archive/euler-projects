def is_prime(x):
    avval = True
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            avval = False
            break
    return avval

def factors(number):
    primt_factors = 0
    number = int(number)
    for i in range(2,int(number ** 0.5) +1):
        if number % i == 0 and is_prime(i):
            primt_factors = i
    print(primt_factors)
factors(input("enter number: "))
