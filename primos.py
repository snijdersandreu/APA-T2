"""
Adrián Fernández i Andreu Snijders

Tests unitarios:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

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
    """Determina si un número es primo."""
    if numero < 2:
        return False
    for n in range(2, int(numero**0.5) + 1):
        if numero % n == 0:
            return False
    return True

def primos(numero):
    """Devuelve una tupla con todos los números primos menores que su argumento."""
    return tuple(numero for numero in range(2, numero) if esPrimo(numero))

def descompon(numero):
    """Devuelve una tupla con la descomposición en factores primos de su argumento."""
    i = 2
    factores = []
    while i * i <= numero:
        if numero % i:
            i += 1
        else:
            numero //= i   ## se usa //= en lugar de /= para assegurarse que la variable es de tipo entero y no se transforma a float, mas eficiente ya que siempre serà un entero
            factores.append(i)
    if numero > 1:
        factores.append(numero)
    return tuple(factores)

def mcd(numero1, numero2):
    """Devuelve el número máximo común divisor."""
    return ###

def mcm(numero1, numero2):
    """Devuelve el número mínimo común múltiplo."""
    return ###

def mcmN(*numeros):
    """Devuelve el mínimo común múltiplo de sus argumentos."""
    return ###

def mcdN(*numeros):
    """Devuelve el máximo común divisor para un número arbitrario de argumentos."""
    return ###

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


