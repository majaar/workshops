def suma_dzielnikow(liczba):
    suma = 0
    for i in range(liczba):
        if i != 0 and liczba % i == 0:
            suma = suma + i
    return suma

print(suma_dzielnikow(6))