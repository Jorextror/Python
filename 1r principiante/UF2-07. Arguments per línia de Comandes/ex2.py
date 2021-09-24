"""Jordi Oliveda
"""
import sys
sys.argv.pop(0)

if len((sys.argv)) == 2:
    if (sys.argv[0]).isalpha() and (sys.argv[1]).isdigit():
        print(int((sys.argv[1]))*(sys.argv[0]+"\n"))
    else:
        if (sys.argv[0]).isalpha():
            print("Té de ser text el segon parametre")
        else:
            print("Té de ser text el primer parametre")
else:
    print("Tenen de ser 2 parametres exactes!")
