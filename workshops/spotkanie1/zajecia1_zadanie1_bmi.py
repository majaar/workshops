wskaznik_BMI = 0


def BMI(masa , wzrost):
    wskaznik_BMI = round(masa / (wzrost * wzrost), 2)
    return wskaznik_BMI


def komentarz(BMI):
    print("Twój wskaźnik BMI wynosi: " + str(wskaznik_BMI))
    if wskaznik_BMI < 18.5:
        print("Twój wskaźnik BMI wskazuje na niedowagę.")
    elif wskaznik_BMI < 24.99:
        print("Twój wskaźnik BMI jest prawidłowy.")
    else:
        print("Twój wskaźnik BMI wskazuje na nadwagę.")

# Niedowaga
wskaznik_BMI = BMI(50, 1.84)
komentarz(wskaznik_BMI)

# Wartość prawidłowa
wskaznik_BMI = BMI(80, 1.84)
komentarz(wskaznik_BMI)

# Nadwaga
wskaznik_BMI = BMI(160, 1.84)
komentarz(wskaznik_BMI)