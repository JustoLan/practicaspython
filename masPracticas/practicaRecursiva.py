def sumaDigitos(n):
    """
    Esta funcion suma los digitos de un numero

    Args:
        n: int

    Returns:
        int

    """
    if n < 10:
        return n
    else:
        return n%10 + sumaDigitos(n//10)
    
print(sumaDigitos(12345))