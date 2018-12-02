pozostala_kwota = 0

nominaly = [20, 10, 5, 2, 1]

def zaplata(kwota):
    for n in nominaly:
        ilosc = kwota // n
        kwota = kwota - ilosc * n
        print("Liczba nominału o wartości {0} zł, to: {1}".format(str(n), str(ilosc)))


zaplata(123)
