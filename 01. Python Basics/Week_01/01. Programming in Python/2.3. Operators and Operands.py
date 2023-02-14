# Soma: 

1 + 1   # Não é necessário por parentêses no (-1).
5 + -1  # O python já sabe que é um valor negativo.
       

# Subtração:

1 - 1
-5 - 9

# DIvisão:

10 / 5 # Divisão sempre retorna um Float
10 / 9

# Multiplicação:

5 * 0
10 * 110

# Resto:

10 % 7 # 10 dividido por 7 da um sobra, 3 logo essa operação dá 3
20 % 2 # Essa operação é útil para encontrar pares e ímpares
10 % 3 # Pois todo número par dividido por outro par dá resto 0

# Divisão inteira:

10 // 7 # 10 dividido por 7 da um sobra 3, logo essa operação dá 1

# Exp:

2 ** 2
2 ** 3

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
    assert 5 ** 2 == 25  # 5 squared
    assert 2 ** 7 == 128  # 2 to the power of 7

    # Há suporte completo para ponto flutuante; operadores com
    # operandos de tipo misto convertem o operando inteiro em ponto flutuante.
    assert 4 * 3.75 - 1 == 14.0