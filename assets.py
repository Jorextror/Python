"""Jordi Oliveda
"""
def requadre(a,b):
    for i in range(a):
        print('*' * b)
        
def de_hores_a_segons(hores):
    segons = hores*3600
    return 'en segons son', segons