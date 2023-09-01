def power_digits_sum(power):
    power_of = str(2 ** power)
    digits_sum = 0
    for i in power_of:
        digits_sum += int(i)
    print(digits_sum)
power_digits_sum(int(input("enter number: ")))