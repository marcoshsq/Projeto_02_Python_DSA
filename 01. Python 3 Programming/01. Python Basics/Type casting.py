"""Type casting.

Pode haver momentos em que você deseja especificar um tipo para uma variável. Isso pode ser feito com fundição.
Python é uma linguagem orientada a objetos e, como tal, usa classes para definir tipos de dados,
incluindo seus tipos primitivos.

A conversão em python é, portanto, feita usando funções construtoras:

- int() - constrói um número inteiro a partir de um literal inteiro, um literal float (arredondando para baixo
para o número inteiro anterior) literal, ou um literal de string (desde que a string represente um
número inteiro)

- float() - constrói um número float a partir de um literal inteiro, um literal float ou um literal de string
(desde que a string represente um float ou um inteiro)

- str() - constrói uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, integer
literais e literais flutuantes

"""


def test_type_casting_to_integer():
    """Type casting para integer"""

    assert int(1) == 1
    assert int(2.8) == 2
    assert int("3") == 3


def test_type_casting_to_float():
    """Type casting para float"""

    assert float(1) == 1.0
    assert float(2.8) == 2.8
    assert float("3") == 3.0
    assert float("4.2") == 4.2


def test_type_casting_to_string():
    """Type casting para string"""

    assert str("s1") == "s1"
    assert str(2) == "2"
    assert str(3.0) == "3.0"
