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


"""(づ｡◕‿‿◕｡)づ

"""
