def silnia(n):
    wynik = 1
    i = 1
    while i < n:
        i += 1
        wynik = wynik * i
    return wynik

def suma_silni(i):
    suma_silni = 0
    for s in range(1, i+1):
        suma_silni = suma_silni + silnia(s)
        #print(silnia(s))
    return suma_silni


print(silnia(4))
print(silnia(5))
print("*****************")

for i in range(3, 6):
    print("{0}: {1:3d}".format(i, suma_silni(i)))

