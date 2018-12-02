def rozmien(portmonetka, kwota):
    wynik = [0]*len(portmonetka)
    zostalo = kwota
    for nominal in reversed(range(len(portmonetka))):
        if zostalo <= 0:
            break
        if portmonetka[nominal] == 0:
            continue

        liczba_nominalow = min(zostalo // nominal, portmonetka[nominal])
        zostalo -= liczba_nominalow * nominal
        portmonetka[nominal] -= liczba_nominalow
        wynik[nominal] = liczba_nominalow

    while zostalo > 0:
        if portmonetka == [0]*len(portmonetka):
            break
        for nominal in reversed(range(len(portmonetka))):
            if portmonetka(nominal) > 0:
                zostalo -= nominal
                portmonetka[nominal] -= 1
                wynik[nominal] += 1
    return wynik


portmonetka = [0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]

print(rozmien(portmonetka, 133))
