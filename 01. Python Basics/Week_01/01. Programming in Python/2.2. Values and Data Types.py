# Data Types - Números

"""

Existem três tipos numéricos principais em Python:

    int (e.g. 2, 4, 20);
    bool (e.g. Falso e Verdadeiro, agindo como 0 e 1);
    float (e.g. 5.0, 1.6);
    complex (e.g. 5+6j, 4-3j), para matemática bizarra.

Na verdade são quatro (tipos primitivos), mas vou falar que eu só descobri o complex porque pesquisei, 
mas nunca usei pra nada, e acho que a menos que eu comece a fazer umas matemáticas bizarras, 
provavelmente não vou usar mesmo!

"""

# Int:

def test_integer_numbers():
    """Integer type

    Int, ou inteiro, é um número inteiro, positivo ou negativo,
    sem decimais, e de comprimento ilimitado.
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


# Bool:

"""
Booleanos representam os valores de Verdadeiro e Falso em Python. 
E são os únicos objetos são os únicos objetos booleanos. 

O tipo booleano é um subtipo do tipo inteiro, e valores booleanos se comportam 
como os valores 0 e 1, respectivamente, em quase todos os contextos.
Com exceção de que quando convertido para uma string, as strings "False" ou "True" 
são retornadas, respectivamente.

"""

def test_booleans():
    """Boolean
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Convertendo o bool para string.
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


# Float:

"""
Float, ou "número de ponto flutuante" é um número, positivo ou negativo,
contendo um ou mais decimais.
     
"""

def test_float_numbers():
    """Float type
    """

    float_number = 7.0
    # Outra forma de declarar um float é usando a função float().
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # Float também pode ser números científicos com um "e" para indicar
    # a potência de 10.
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


# Complex - Números Imaginários:

def test_complex_numbers():
    """Complex Type"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j