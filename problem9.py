c = 0
for a in range(500):
    for b in range(500):
        c = 1000 - a - b
        if  c*c == a*a + b*b:
            print("{0}, {1}, {2}".format(a, b, c))
            print(a*b*c)
