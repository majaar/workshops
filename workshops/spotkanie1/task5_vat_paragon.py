zakupy = [0.2, 0.5, 4.59, 6]
# suma_zakupy = 11.29
# vat_indywid = 0.23%  0.046 0.115 1.0557 1.38
# suma vat_indyw = 2.5967

def vat_faktura(lista):
    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23*suma, 2)
    return vat

def vat_paragon(lista):
    suma = 0
    for element in lista:
        vat = round(0.23 * element, 2)
        suma = suma + vat
    return suma

#print(vat_faktura(zakupy))
#print(vat_paragon(zakupy))

