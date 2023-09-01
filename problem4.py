#palindromes' number and his factors list
palindromes_and_factors = []
#the product of tow 3-digits
for i in range(100, 1000):
    for j in range(100, 1000):
        product = j * i
        #if product == revarse product
        if str(product) == str(product)[::-1]:
            palindromes_and_factors.append([i, j, product])
#len palindromes for search in palindromes-list
len_p = len(palindromes)
#the list of palindromes' numbers
palindromes = []
#serch in palindromes_and_factors-list
for n in range(len_p):
    #append palindrome number to palindromes-list
    palindromes.append(palindromes_and_factors[n][2])
#sort palindromes-list for find larges palindrome number
palindromes.sort()
print(palindromes[-1])
for i in range(len_p):
    #find larges palindrome and factors
    if palindromes[-1] == palindromes_and_factors[i][2]:
        print(palindromes_and_factors[i])