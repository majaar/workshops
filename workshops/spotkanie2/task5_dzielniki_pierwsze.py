from spotkanie2 import task3_lista_dzielnikow, task4_liczba_pierwsza


def dzielniki_pierwsze(n):
    lista_dzielnikow_pierwszych = []
    for element in task3_lista_dzielnikow.zwroc_liste_dzielnikow(n):
        if task4_liczba_pierwsza.pierwsza(element):
            lista_dzielnikow_pierwszych.append(element)
    return lista_dzielnikow_pierwszych


print(dzielniki_pierwsze(14))
