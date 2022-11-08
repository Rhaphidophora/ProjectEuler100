
def is_palindrome(number):
    n = str(number)
    m = n[::-1]
    if m == n:
        return True
    else:
        return False

print(is_palindrome(90709))
print(is_palindrome(432))



i = 999
j = 999
number = 0
for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        number = i * j
        if is_palindrome(number):
            print("{0} is a palindrome".format(number))
    print(i)
    

