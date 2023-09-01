def IsEven(x):#TODO check is that nummber even or not
    if x % 2 == 0:
        return True
    else:
        return False
first = 1
seccond = 2

sum = 0 

while first < 4*10**6:
    if IsEven(first):
        sum += first
    new = first + seccond
    first = seccond
    seccond = new
print(sum)