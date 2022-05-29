"""Operadores de Atribuição

Os operadores de atribuição são usados para atribuir valores a variáveis

"""


def test_assignment_operator():
    """Operadores de Atribuição"""

    # Atribuição: =
    number = 5
    assert number == 5

    # Multiplas Atribuições.
    # As variáveis first_variable e second_variable obtêm simultaneamente os novos valores 0 e 1.
    first_variable, second_variable = 0, 1
    assert first_variable == 0
    assert second_variable == 1

    # Você pode até trocar valores de variáveis usando atribuição múltipla.
    first_variable, second_variable = second_variable, first_variable
    assert first_variable == 1
    assert second_variable == 0


def test_augmented_assignment_operators():
    """Operador de atribuição combinado com operadores aritméticos e bit a bit"""

    # Atribuição: +=
    number = 5
    number += 3
    assert number == 8

    # Atribuição: -=
    number = 5
    number -= 3
    assert number == 2

    # Atribuição: *=
    number = 5
    number *= 3
    assert number == 15

    # Atribuição: /=
    number = 8
    number /= 4
    assert number == 2

    # Atribuição: %=
    number = 8
    number %= 3
    assert number == 2

    # Atribuição: %=
    number = 5
    number %= 3
    assert number == 2

    # Atribuição: //=
    number = 5
    number //= 3
    assert number == 1

    # Atribuição: **=
    number = 5
    number **= 3
    assert number == 125

    # Atribuição: &=
    number = 5  # 0b0101
    number &= 3  # 0b0011
    assert number == 1  # 0b0001

    # Atribuição: |=
    number = 5  # 0b0101
    number |= 3  # 0b0011
    assert number == 7  # 0b0111

    # Atribuição: ^=
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert number == 6  # 0b0110

    # Atribuição: >>=
    number = 5
    number >>= 3
    assert number == 0  # (((5 // 2) // 2) // 2)

    # Atribuição: <<=
    number = 5
    number <<= 3
    assert number == 40  # 5 * 2 * 2 * 2


"""(づ｡◕‿‿◕｡)づ

"""
