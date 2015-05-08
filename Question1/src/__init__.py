__author__ = 'fabienlamarque'


def sumfor(listparameter):
    somme = 0
    for i in range(0, len(listparameter) ):
        somme += listparameter[i]
    return somme


def sumwhile(listparameter):
    somme = 0
    i = 0
    while i < len(listparameter):
        somme += listparameter[i]
        i += 1
    return somme

print(sumfor([1, 3, 4, 5]))
print(sumwhile([1, 3, 4, 5]))
