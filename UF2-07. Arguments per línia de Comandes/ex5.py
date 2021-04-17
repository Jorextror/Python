"""Jordi Oliveda
"""
import sys
import datetime

Teclat=sys.argv[1]
try :
    dia,mes,año = Teclat.split('/')
    valid = True
    datetime.datetime(int(año),int(mes),int(dia))
except ValueError:
    valid = False

if(valid):
    print ("el format de la date esta valid(DD/MM/YYY):",Teclat)
else:
    print ("el format de la date no és valid(DD/MM/YYY):",Teclat)