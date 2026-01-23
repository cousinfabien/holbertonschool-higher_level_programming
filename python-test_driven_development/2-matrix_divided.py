#!/usr/bin/python3
"""
Module that divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of lists of int/float): matrix to divide
        div (int/float): divisor

    Returns:
        new_matrix (list of lists of float): result of division

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats
        TypeError: if rows are not all the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div == 0
    """
    # Vérification que div est un int ou float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Vérification que matrix est une liste de listes et que chaque élément est int/float
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Création d’une nouvelle matrice avec division arrondie à 2 décimales
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
