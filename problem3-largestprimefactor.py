number = 600851475143

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
i = 2
while True:
    if is_prime(i):
        if number % i == 0:
            print("{0} is a prime factor".format(i))
            number = number / i
            print(number)
    i = i + 1
    if i > number:
        break
