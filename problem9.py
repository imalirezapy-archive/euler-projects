a_list = []
b_list = []
c_list = []
summ = 1000
for i in range(1,summ//9):
    a2 = 4 * i
    c2 = 5 * i
    a_list.append(a2)
    c_list.append(c2)
for i in range(1,summ//6):
    b2 = 3 * i
    b_list.append(b2)
    
for a in a_list:
    for b in b_list:
        for c in c_list:
            if a**2 + b**2 == c**2:
                if a + b + c == summ:
                    a1, b1, c1 = a, b, c

print(f"a = {a1}    ", f"b = {b1}   ", f"c = {c1}")
print(f"a + b + c = ",a1+b1+c1)
print(f"a * b * c = ",a1*b1*c1)
    
        #31875000
        #a = 200
        #b = 375
        #c = 425