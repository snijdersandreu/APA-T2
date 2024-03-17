"""
Adrián Fernández i Andreu Snijders

Tests unitarios:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> primos(8)
(2, 3, 5, 7)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(820, 630, 1050, 1470)
210

"""

def esPrimo(numero):
    return #True or False

def primos(numero):
    return #tupla con todos los numeros primos menores que su argumento

def descompon(numero):
    return #tupla con la descomposición en factores primos de su argumento

def mcm(numero1, numero2):
    return #num min comu mult.

def mcd(numero1, numero2):
    return #num max comu div.

def mcmN(*numeros):
    # fot lo mateix que mcm() però *numeros és una tupla
    return #num min comu mult.

def mcdN(*numeros):
    # fot lo mateix que mcd() però *numeros és una tupla
    return # num max comu div.

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

