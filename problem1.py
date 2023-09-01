def sum_multiples_3_5(x):#TODO: find and sum muliples 3 & 5 
    sum = 0
    for i in range(1, int(x)):       
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
sum_multiples_3_5(input("enter number: "))