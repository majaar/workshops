def zwroc_liste_dzielnikow(liczba):
    lista_dzielnikow = []
    for i in range(liczba+1):
        if i != 0 and liczba % i == 0:
            lista_dzielnikow.append(i)
    return lista_dzielnikow


#print(zwroc_liste_dzielnikow(15))
