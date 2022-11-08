def get_divisorsum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    return sum


pairsum = 0
for a in range(1, 10001):
    b = get_divisorsum(a)
    if b < 10001:
        c = get_divisorsum(b)
        if a != b:
            if a == c:
                # we have an amicable pair
                print(a,b)
                pairsum = pairsum + a + b


print(pairsum/2)

