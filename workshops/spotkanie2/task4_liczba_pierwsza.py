from spotkanie2 import task3_lista_dzielnikow


def pierwsza(n):
    if len(task3_lista_dzielnikow.zwroc_liste_dzielnikow(n)) == 2:
        return True
    return False

print(pierwsza(7))
