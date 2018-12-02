import random
from spotkanie2 import zajecia2_zadanie2_losuj_zapalki


def zapalki_gra(il_zap):
    while il_zap > 0:
        print("Ilość zapałek: " + str(il_zap))
        we = int(input("Podaj swój ruch: "))
        il_zap = il_zap - we
        if il_zap <= 0:
            print("*** Przegrałeś! ***")
        else:
            ruch_komputera = random.randint(1, 3)
            print("Ruch komputera to: " + str(ruch_komputera))
            il_zap = il_zap - ruch_komputera
            if il_zap <= 0:
                print("*** Wygrales! ***")

wylosowana_ilosc_zapalek = zajecia2_zadanie2_losuj_zapalki.losuj_zapalki()

zapalki_gra(wylosowana_ilosc_zapalek)


