def rozmien(portfel, kwota):
    zaplata = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index in range(len(portfel)-1, 0, -1):
        if portfel[index] != 0:
            ilosc = kwota // index
            kwota -= index * min(ilosc, portfel[index])
            zaplata[index] = min(ilosc, portfel[index])
            portfel[index] = portfel[index] - min(ilosc, portfel[index])
    if kwota != 0:
        for index in range((len(portfel))):
            if portfel[index] > 0 and kwota < index:
                zaplata[index] += 1
                portfel[index] -= 1
                break
            else:
                zaplata[index] = 0
    return zaplata

ilosc_nominalow = [0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]

zaplata = rozmien(ilosc_nominalow, 37)
for index in range(len(ilosc_nominalow)-1, 0, -1):
    if zaplata[index] != 0:
        print("Ilość nominału o wartości {0} to {1}".format(index, zaplata[index]))


