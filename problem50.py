limit = 1000000

# generate sieve

sieve = []
for i in range(limit):
    sieve.append(1)

sieve[0] = 0 # 1 nie je prvocislo



def cross_out(n):
    i = 1
    while True:
        i = i + 1
        if i*n > limit:
            break
        sieve[i*n-1] = 0


for i in range(2, int(limit/2)+1):
    if sieve[i-1] == 1:
        cross_out(i)



# generates a prime list
primes = []
for i in range(len(sieve)):
    if sieve[i] == 1:
        primes.append(i+1)

#spocita za sebou iducich n prvocisel
def sums(n):
    i = 1
    while True:
        suma = 0
        if i+n-1 > len(primes):
            break
        for j in range(0, n):
            suma += primes[i+j-1]
       
        try:
            if sieve[suma-1] == 1:
                print(f"Pocet: {n} Prvocislo: {suma}, i: {i}")
        except IndexError:
            if suma > limit:
                break
        i = i + 1
        

    return 0


i = 1
while True:
    sums(i)
    i = i + 1

    if ((1+i)*i/2) > limit :
        print("finished")
        break

