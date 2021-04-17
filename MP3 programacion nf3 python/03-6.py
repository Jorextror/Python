"""Escriviu un programa que donada una llista de strings,
no cal que sigui introduïda per teclat,
ens digui quants elements hi ha a la llista de longitud
més gran o igual que 2, i comencen per ‘a’.
Mostrar per pantalla el resultat.
Per exemple: llista = ['abc', 'xyz', 'aba', '1221', ‘a’],
sortida : “Hi ha 2 elements”
Jordi Oliveda
"""
"""llista"""
ll = ["a","b","c"]
"""filtrem per que entri la llista per (a) i més llarg de un"""
if ll[0] == "a" and len(ll) >= 2:
    print("Hi ha",len(ll),"elements")
else:
    print("el string no comenza per (a) o és més curt de dos elemnts de longitut")