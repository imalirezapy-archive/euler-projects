def Iseven(x):
    if x % 2 == 0:
        return True
    else:
        return False
l = 0
m = 0
for i in range(830000,837800):
    start_number = i
    sequence_list = []
    while 1 < start_number:
        if Iseven(start_number):
            start_number //= 2
            sequence_list.append(start_number)
        else:
            start_number = start_number * 3 + 1
            sequence_list.append(start_number)
    len_sequence = len(sequence_list)
    if l < len_sequence:
        l = len_sequence
        m = i

print(m,l)