def suma(a, b):
    """
    Returns a + b

    >>> suma(5, 7)
    12
    """
    return a + b

def resta(a, b):
    """
    Returns a - b

    >>> resta(10, 7)
    3
    """
    return a - b

def multiplicacion(a, b):
    """
    Returns a * b

    >>> multiplicacion(5, 7)
    35
    """
    return a * b

def division(a, b):
    """
    Returns a / b

    >>> division(10, 5)
    2
    """
    return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)