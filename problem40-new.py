import math

def get_nth_number(n):
    
    
    i = 1
    number = n
    while True:
        expression = number - i*9*10**(i-1)
        if expression < 0:
            break
        else:
            number = expression
            i += 1

    cislo = 0
    for j in range(1, i):
        cislo = cislo + 9*10**(j-1)
    cislo = cislo + math.ceil(number / i)

    cislica_z_cisla = number % i
    if cislica_z_cisla == 0:
        cislica_z_cisla = i

    cislo_string = str(cislo)
    cislica = cislo_string[cislica_z_cisla-1]
    print(cislo, cislica_z_cisla, cislica)
    return int(cislica)


if __name__ == "__main__":
    vysledok = 1
    for i in range(0,7):
        vysledok = vysledok * get_nth_number(10**i)

    print("vysledok je", vysledok)
        
