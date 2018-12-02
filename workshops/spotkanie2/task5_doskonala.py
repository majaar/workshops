# WORK IN PROGRESS

def suma_dzielnikow(liczba):
    suma = 0
    for i in range(liczba + 1):
        if i != 0 and liczba % i == 0:
            #print(i)
            suma = suma + i
    return suma

print(suma_dzielnikow(6))

#def doskonala(n):
