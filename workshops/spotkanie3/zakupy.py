from spotkanie1 import task5_vat_paragon

def zakupy(cennik, lista_zakupow):
    suma = 0
    lista_cen = []
    for produkt in lista_zakupow:
        suma += lista_zakupow[produkt] * cennik[produkt]
        lista_cen.append(lista_zakupow[produkt] * cennik[produkt])
    return suma, lista_cen

cennik = {
    'kawa': 14.99,
    'pomarańcze': 3.49,
    'olej': 4.99
}

lista_zakupow = {'olej': 2, 'kawa': 1}

suma = zakupy(cennik, lista_zakupow)[0]
lista_cen = zakupy(cennik, lista_zakupow)[1]
vat_faktura = task5_vat_paragon.vat_faktura(lista_cen)
vat_paragon = task5_vat_paragon.vat_paragon(lista_cen)

print("Suma: " + str(suma))
print("Vat faktura: " + str(vat_faktura))
print("Vat paragon: " + str(vat_paragon))

