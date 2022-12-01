# 1 to n exactly once

def is_prime(n):
    for i in range(2,round(n**(1/2))):
        if n % i == 0:
            return False
    return True

def is_pan(n):
    k = len(str(n))
    a = []
    for i in range(1, k+1):
        a.append(str(i))
    r = set(a)
    s = set(str(n))
    if r == s:
        return True
    else:
        return False
 
for i in range(1,10):
    if ((1+i)*i/2) % 3 == 0:
        continue
    if ((1+i)*i/2) % 9 == 0:
        continue

      
    for j in range(10**(i-1),10**i-1):
        if is_pan(j):
                if is_prime(j):
                    prvocislo = j

                

print(f"The largest pandigital prime: {prvocislo}")


