def squares_sum(x):
    squares = 0
    Sum = 0
    for i in range(1,x+1):
        squares += i**2
    for i in range(1,x+1):
        Sum += i
    print((Sum**2) - squares)

squares_sum(100)