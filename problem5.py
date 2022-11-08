def is_prime(n):
    if n < 2:
        return False
    for i in range(2, round(n**1/2)):
        if n % i == 0:
            return False
    return True

common = 1

for i in range(1, 21):
    if is_prime(i):
        common = common * i

for i in range(1, round(20**1/2)):
    
        

