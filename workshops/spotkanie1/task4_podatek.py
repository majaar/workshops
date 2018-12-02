def podatek(kwota):
    prog_19 = 44490
    prog_40 = 85528

    if kwota <= prog_19:
        podatek = 0.19 * kwota
    elif kwota <= prog_40:
        podatek = 0.19 * prog_19 + 0.3 * (kwota - prog_19)
    else:
        podatek = 0.19 * prog_19 + 0.3 * (prog_40 - prog_19) + 0.4 * (kwota - prog_40)
    return podatek

print(podatek(105528))

# podatek maks prog_1 = 8453.1
# podatek maks prog_2 = 12311.4
# suma prog_1 i prog_2 = 20764.5