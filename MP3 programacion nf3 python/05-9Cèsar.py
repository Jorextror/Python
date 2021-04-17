"""Jordi Oliveda
Programa l’algorisme del xifratge del Cèsar. Fes dues versions en Python: amb llistes i amb cadenes.
Prova’l amb la frase “m’agraden els algorismes classics”.
"""

texto = 'm’agraden els algorismes classics'.upper()#.upper per fer ho tot mayuscules
# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
# Guardar mensaje
descifrado = ""
for l in texto:
    # Si la letra está en el abecedario reemplazamos
    if l in abc:
        pos_letra = abc.index(l)
        # Restamos para movernos a la izquierda
        nueva_pos = (pos_letra - 1) % len(abc)
        descifrado += abc[nueva_pos]
    else:
        descifrado+= l
print(descifrado)