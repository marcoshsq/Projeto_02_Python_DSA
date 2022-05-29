"""Operadores Aritméticos.

Operadores Aritméticos são usados para realizar operações matemáticas simples, alguns pode 
ser usados com outros tipos de dados para realizar concatenação e etc.

"""


def testar_operadores_aritméticos():
    """Operadores Aritméticos"""

    # Adição.
    assert 5 + 3 == 8

    # Subtração.
    assert 5 - 3 == 2

    # Multiplicação.
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # Divisão.
    # O resultado pode ser um float.
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # Módulo, ou resto da divisão.
    assert 5 % 3 == 2

    # Potenciação.
    assert 5**3 == 125
    assert 2**3 == 8
    assert 2**4 == 16
    assert 2**5 == 32
    assert isinstance(5**3, int)

    # Divisão inteira.
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)


"""(づ｡◕‿‿◕｡)づ

"""
