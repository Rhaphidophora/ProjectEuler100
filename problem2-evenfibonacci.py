
total = 0

p1 = 1
p2 = 2
p3 = 3

total = total + p2

while p3 < 4e6:

    p3 = p1 + p2
    if p3 > 4e6:
        break
    print(p3)    
    p1 = p2
    p2 = p3

    if p3 % 2 == 0:
        total = total + p3

print(total)
