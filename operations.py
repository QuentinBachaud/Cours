def add(a, b):
    """
    Additionne deux nombres et retourne le résultat.
    
    Args:
        a: Le premier nombre
        b: Le deuxième nombre
    
    Returns:
        La somme de a et b
    """
    return a + b


def sub(a, b):
    """
    Soustrait deux nombres et retourne le résultat.
    
    Args:
        a: Le premier nombre
        b: Le deuxième nombre
    
    Returns:
        La différence entre a et b
    """
    return a - b


def div(a, b):
    """
    Divise deux nombres et retourne le résultat.

    Args:
        a: Le nombre à diviser
        b: Le diviseur

    Returns:
        Le résultat de la division de a par b
    """

    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro.")

    return a / b
