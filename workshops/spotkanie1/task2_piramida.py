def piramida(wysokosc):
    for i in range(wysokosc):
        print(" " * (wysokosc - i + 1) + "#" * (2 * (i+1) - 1))


piramida(3)



