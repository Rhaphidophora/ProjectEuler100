def is_prime(n):
    if n < 2:
        return False
    for i in range (2,round(n**1/2)+1):
        if n % i == 0:
            return False
    return True



n = 0
i = 0
while n < 10001:
    i = i + 1
    if is_prime(i):
        n = n + 1
        print (n, ": ",i)


print(i)
