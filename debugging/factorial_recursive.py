#!/usr/bin/python3
"""Calcula el factorial de un número entero no negativo.

    Args:
        n (int): El número entero no negativo del cual se calculará el factorial.

    Returns:
        int: El factorial de n. Devuelve 1 si n es 0.
    """
import sys

def factorial(n):
        if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
