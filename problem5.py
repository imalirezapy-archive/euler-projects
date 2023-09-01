def gcd(x,y): # bmimim
    print(f"y = {int(y)}" ,f"   (gcd)    x = {int(x)}" )
    return y and gcd(y, x % y) or x
def lcm(x,y): # kmimim
    print(f"y = {int(y)}" ,f"   (lcm)    x = {int(x)}" )
    return x * y / gcd(x,y)

n = 1
for i in range(11, 20):
    n = lcm(n, i)
print(n)
