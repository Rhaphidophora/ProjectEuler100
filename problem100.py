b = 15
n = 21
target = 1000000000000

while n < target:
    bt = 3*b + 2*n - 2
    nt = 4*b + 3*n - 3
    b = bt
    n = nt

print(b, n)
