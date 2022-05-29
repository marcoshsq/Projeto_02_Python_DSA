"""Números

O Python é uma ótima Calculadora, mas como meu PC é super lento, ela
não é uma calculadora muito prática u.u

"""

# Soma:

1 + 1  # Não é necessário por parentêses no (-1).
5 + -1  # O python já sabe que é um valor negativo.


# Subtração:

1 - 1
-5 - 9

# DIvisão:

10 / 5  # Divisão sempre retorna um Float
10 / 9

# Multiplicação:

5 * 0
10 * 110

# Resto:

10 % 7  # 10 dividido por 7 da um sobra, 3 logo essa operação dá 3
20 % 2  # Essa operação é útil para encontrar pares e ímpares
10 % 3  # Pois todo número par dividido por outro par dá resto 0

# Divisão inteira:

10 // 7  # 10 dividido por 7 da um sobra 3, logo essa operação dá 1

# Exp:

2**2
2**3

# A precedência de operadores é:
# parênteses, expoentes, multiplicação/divisão, adição/subtração

# Exemplos


def operações(x):
    print(f"O número anterior é: {x - 1}")
    print(f"O número posterior é: {x + 1}")
    print(f"O dobro é: {x * 2}")
    print(f"O triplo é: {x * 3}")
    print(f"E sua raiz quadrada é: {x ** 0.5}")


operações(int(input("Insira um número:\n")))


def test_number_operators():
    """Basic operations"""

    # Adição.
    assert 2 + 4 == 6

    # Multiplicação.
    assert 2 * 4 == 8

    # A divisão sempre retorna um número de ponto flutuante.
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # O operador de módulo retorna o restante da divisão.
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # A divisão do piso descarta a parte fracionária.
    assert 17 // 3 == 5

    # Elevando o número a uma potência específica.
    assert 5**2 == 25  # 5 squared
    assert 2**7 == 128  # 2 to the power of 7

    # Há suporte completo para ponto flutuante; operadores com
    # operandos de tipo misto convertem o operando inteiro em ponto flutuante.
    assert 4 * 3.75 - 1 == 14.0


###


""" Data Types - Números:

Existem três tipos numéricos principais em Python:

- int (e.g. 2, 4, 20);
- bool (e.g. Falso e Verdadeiro, agindo como 0 e 1);
- float (e.g. 5.0, 1.6);
- complex (e.g. 5+6j, 4-3j), para matemática bizarra.

Na verdade são quatro (tipos primitivos), mas vou falar que eu só 
descobri o complex porque pesquisei, mas nunca usei pra nada, e acho 
que a menos que eu comece a fazer umas matemáticas bizarras, 
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
    """Boolean"""

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Convertendo o bool para string.
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


1 == 1  # Retorna True
2 == 1  # Retorna False
True and False  # Retorna False

# Float:

"""
Float, ou "número de ponto flutuante" é um número, positivo ou negativo,
contendo um ou mais decimais.
     
"""


def test_float_numbers():
    """Float type"""

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
    float_with_big_e = 12e4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12e4, float)
    assert isinstance(-87.7e100, float)


# Complex - Números Imaginários:


def test_complex_numbers():
    """Complex Type"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


"""(づ｡◕‿‿◕｡)づ

"""
