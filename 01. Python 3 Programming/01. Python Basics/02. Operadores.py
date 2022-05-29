"""
02. Operadores de Identidade e Associação

    * Operadores Aritméticos;
    
    * Operadores Bitwise (Bit-a-Bit);

    * Operadores de Atribuição;

    * Operadores de Comparação;

    * Operadores Lógicos;

    * Operadores de Identidade e Associação.

"""


"""Operadores Bitwise

Operadores bit a bit manipulam números em nível de bit.

"""


def test_bitwise_operators():
    """Operadores Bitwise"""

    # AND
    # Define cada bit como 1 se ambos os bits forem 1.
    #
    # Exemplo:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 & 3 == 1  # 0b0001

    # OR
    # Define cada bit como 1 se um dos dois bits for 1.
    #
    # Exemplo:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 | 3 == 7  # 0b0111

    # NOT
    # Inverte todos os bits.
    assert ~5 == -6

    # XOR
    # Define cada bit como 1 se apenas um dos dois bits for 1.
    #
    # Exemplo:
    # 5 = 0b0101
    # 3 = 0b0011
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110

    # Deslocamento à direita assinado
    # Desloque para a direita empurrando as cópias do bit mais à esquerda da esquerda e deixe o mais à direita
    # bits caem.
    #
    # Exemplo:
    # 5 = 0b0101
    assert 5 >> 1 == 2  # 0b0010
    assert 5 >> 2 == 1  # 0b0001

    # Deslocamento à esquerda de preenchimento zero
    # Desloque para a esquerda pressionando zeros da direita e deixe os bits mais à esquerda caírem.
    #
    # Exemplo:
    # 5 = 0b0101
    assert 5 << 1 == 10  # 0b1010
    assert 5 << 2 == 20  # 0b10100


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


"""Operadores de comparação

Os operadores de comparação são usados para comparar dois valores.
"""


def test_comparison_operators():
    """Operadores de comparação"""

    # Igual.
    number = 5
    assert number == 5

    # Diferente.
    number = 5
    assert number != 3

    # Maior que.
    number = 5
    assert number > 3

    # Menor que.
    number = 5
    assert number < 8

    # Maior ou Igual que
    number = 5
    assert number >= 5
    assert number >= 4

    # Menor ou Igual que
    number = 5
    assert number <= 5
    assert number <= 6


"""Logical operators

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
