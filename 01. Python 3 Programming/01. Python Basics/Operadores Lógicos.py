"""Operadores Lógicos

Operadores lógicos são usados com declarações condicionais.

A lógica é simples:

and | V com V da V
or  | F com F da F
not | Inverte o valor lógico

"""


def test_logical_operators():
    """Operadores lógicos"""

    # Exemplos.
    first_number = 5
    second_number = 10

    # and
    # Retorna True se ambos forem True.
    assert first_number > 0 and second_number < 20

    # or
    # Retorna True se apenas um for True
    assert first_number > 5 or second_number < 20

    # not
    # Inverte o valor lógico.
    # pylint: disable=unneeded-not
    assert not first_number == second_number
    assert first_number != second_number


"""(づ｡◕‿‿◕｡)づ

"""
