kw = 1000

def odsetki(oproc, czas, kwota):
    return round(kwota * (oproc / 100) * (czas / 12), 2)

def odnawianie(oproc, czas, kwota, odn):
    for odnowienie in range(odn):
        kwota = kwota + odsetki(oproc, czas, kwota)
    return round(kwota - kw, 2)

print("Na lokacie 12 miesiecznej zarobisz: ", odsetki(3, 12, kw))
print("Na 4 lokatach 3 miesięcznych zarobisz: ", odnawianie(3, 3, kw, 4))
