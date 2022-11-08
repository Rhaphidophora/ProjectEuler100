limit = 2000000

sieve = []
for i in range(limit):
    sieve.append(1)

# print(sieve)

def cross_out(n):
    # cel = int(limit/n)
    i = 1
    while True:
        i = i + 1
        if i*n > limit:
            break
        sieve[i*n-1] = 0


for i in range(2, int(limit/2)+1):
    if sieve[i-1] == 1:
        cross_out(i)

# print(sieve)

sum = -1
for i in range(limit):
    if sieve[i] == 1:
        sum = sum + (i+1)
    i = i + 1   

    if i % 100000 == 0:
        print(i, sum)


print(sum)
