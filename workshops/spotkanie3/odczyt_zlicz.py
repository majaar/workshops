def statystyka(nazwa_pliku):
    with open(nazwa_pliku, 'r') as fh:
        tekst = fh.read()
        liczba_znakow = len(tekst)
        liczba_slow = len(tekst.split())
        liczba_zdan = len(tekst.split('.'))-1
    return liczba_znakow, liczba_slow, liczba_zdan


liczba_znakow = statystyka('litwo.txt')[0]
liczba_slow = statystyka('litwo.txt')[1]
liczba_zdan = statystyka('litwo.txt')[2]

print("Liczba znakow: {0}. Liczba slow: {1}. Liczba zdan: {2}".format(liczba_znakow, liczba_slow, liczba_zdan))

