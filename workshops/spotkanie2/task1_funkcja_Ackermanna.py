def funkcja_Ackermana(m, n):
    if m == 0:
        return n + 1
    elif m > 0:
        if n == 0:
            return funkcja_Ackermana(m - 1, 1)
        elif n > 0:
            return funkcja_Ackermana(m - 1, funkcja_Ackermana(m, n - 1))
    else:
        print("Niepoprawne parametry")
    return ack

print(funkcja_Ackermana(3 , 3))

