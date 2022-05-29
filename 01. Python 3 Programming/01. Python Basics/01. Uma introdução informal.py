"""
01. Uma introdução informal ao Python＼(^ω^＼).

1. print() e input()
2. Mais sobre a função print()
3. help()
4. Variáveis
5. Números
6. Data Types - Numbers
7. Type casting
8. Python Keywords
9. Python Buit-in Functions

# 1. print() e input()


"""

# Alguns comandos básicos do Python que são importantes:

"""O primeiro comando a aprender é o print(), a função print 
recebe algum objeto e imprime ele na tela ou no console."""

print("Oi, eu sou o computador!")

# E o print tem parâmetros

print("Hello, World!")

print(
    "Hello", "World", sep="**"
)  # esse (sep="") separa as partes da string com o simbolo

print("Hello", end="*-*-*")  # o end coloca o seu conteúdo no final

# Já usando aspas triplas é possível fazer uns print bem loko

print(
    """Oi abigos

    Me llamo Ramon Bolivar           +---+---+---+---+---+---+
                                     | P | y | t | h | o | n |
                                     +---+---+---+---+---+---+
                                     0   1   2   3   4   5   6
                                     -6  -5  -4  -3  -2  -1


	
(づ｡◕‿‿◕｡)づ: (◕‿◕) 		
                                                                (づ｡◕‿‿◕｡)づ: (◕‿◕)
(づ｡◕‿‿◕｡)づ: (◕‿◕)	
(づ｡◕‿‿◕｡)づ: (◕‿◕)
"""
)

# A função input() recebe dados do usuário, e usando concatenção
# e/ou interpolação é possível fazer outros prints u.u

name = input("What's is your name? ")

print(f"Hi {name}, nice to meet you!")
print("Hi {}, nice to meet you!".format(name))
print("Hi", name + ", nice to meet you!")

"""# 2. Mais sobre a função print() 


"""

# String é texto, e no python não há diferença de string e char's
# Uma string de apenas 1 character é uma string pequenininha u.u

"Podemos declarar string com aspas duplas"
"Ou com aspas simples"
"Como a maioria dos textos são em inglês e usa-se muito o ', eu vou usar aspas duplas"

# existem operações que podem ser feitas com strings e a função print()
print("Por exemplo, colocar \ngera uma nova linha")
print("Na verdade o contra barra é um character especial")
# E dependendo com quem ele está, ele gera um comando diferente
# \n pula linha
# \a coloca um ponto na frase, tipo para lista

# Para evitar isso coloca-se um r antes das aspas, dizendo para o python que
# essa string é uma raw string u.u
print("O\n babaiaga")
print("O\a babaiaga")
print(r"O\n babaiaga")
print(r"O\a babaiaga")

# Existem outras formas de fazer um print que são muito hacker man!
print(
    "Essa forma aqui, "
    "a frase ainda vai "
    "printada na mesma linha "
    r"caso eu não use \n por exemplo"
)

# Dá para fazer concatenação de strings:

a = "Bola falando: "
b = "Karalho Zé... "
c = "Vai ser pai de novo..."
print(a + b + c)  # Não a diferença entre o mais e a virgula,
print(a, b, c)  # Mas, para concatenação, vou continuar usando o sinal de mais

# Também é possível multiplicar carácteres:

print("Oi " * 10)
print("-=-" * 25)

# String index: Strings podem ser indexadas (subscritos),
# com o primeiro caractere tendo índice 0:

teste = "123456789"
teste[1]

# Os índices também podem ser números negativos, para começar a contar da direita:

teste[-1]

# Além da indexação, o fatiamento também é suportado.
# Enquanto a indexação é usada para obter caracteres individuais,
# o fatiamento permite obter a substring:

teste[1:5]

(
    teste[:3] + teste[3:]
)  # Observe como o início é sempre incluído e o fim sempre excluído.
# Isso garante que s[:i] + s[i:] seja sempre igual a s:

# Strings são imutáveis, não é possível adicionar caracteres depois
# pra isso crie uma nova string u,u

# A função len da o tamanho de uma string:

nome = "Marcos"
len(nome)

"""# 3. help()

"""

# A função help recebe um objeto como parâmetro
# e devolve as funcionalidades do objeto
help(str)

help(tuple)

""" 4. Variáveis"""

"""

Python é completamente orientado a objetos e não "digitado estaticamente".
Não é necessário declarar variáveis antes de usá-las, graças a deus por isso,
ou declarar seu tipo. Cada variável em Python é um objeto.

Ao contrário de outras linguagens de programação, Python não tem comando para
declarando uma variável. Uma variável é criada no momento em que você atribui pela primeira vez
um valor para isso.

Uma variável pode ter um nome curto (como x e y) ou um nome mais descritivo
(idade, carname, total_volume).

Regras para variáveis Python:

- Um nome de variável deve começar com uma letra ou o caractere sublinhado.

- Um nome de variável não pode começar com um número.

- Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (A-z, 0-9 e _ ).

- Os nomes das variáveis diferenciam maiúsculas de minúsculas 
(idade, idade e IDADE são três variáveis diferentes).

"""

# Já em relação à estilo: “Explícito é melhor que implícito.” - The Zen of Python.

# Para nomear variáveis tem duas diretrizes :
# 1. Use uma única letra minúscula, palavra ou palavras. Separe as
# palavras com sublinhados para melhorar a legibilidade. Exemplo:

x = 1
y = 2
z = x + y

# 2. Use nomes simples, descritivos e memoráveis:

num_01 = 1
num_02 = 2
soma_num = num_01 + num_02

# Agora sobre como atribuir, usamos o sinal de "=".
x = 10

# É possível atribuir varios valores, e de tipos diferentes:

x, y, z = 10, 20, 30

a, b, c = 10, True, "Batata"

# Se haver só uma variável à esquerda, o resultado é uma tupla:

x = 10, 20, 30

# Se o número à esqueda e o número à direita forem diferentes, ocorre um erro (ValueError):

x, y = 10, 20, 30
x, y, z = 10, 20

# Porém se usarmos o * na frente do nome da variável, ela vira uma lista:

x, *y = 10, 20, 30
*x, y = 10, 20, 30

"""# 5. Números

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


"""# 06. Data Types - Números:

Existem três tipos numéricos principais em Python:

- int (e.g. 2, 4, 20);
- bool (e.g. Falso e Verdadeiro, agindo como 0 e 1);
- float (e.g. 5.0, 1.6);
- complex (e.g. 5+6j, 4-3j), para matemática bizarra.

Na verdade são quatro (tipos primitivos), mas vou falar que eu só descobri o complex porque pesquisei, mas nunca usei pra nada, e acho que a menos que eu comece a fazer umas matemáticas bizarras, provavelmente não vou usar mesmo!
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


"""# 07. Type casting"""

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


"""True e False: 

São valores lógicos em Python. 

Eles são os resultados de operações de comparação
ou operações lógicas (booleanas) em Python.
"""

1 == 1  # Retorna True
2 == 1  # Retorna False
True and False  # Retorna False

"""None 

É uma constante especial em Python que representa a 
ausência de um valor ou valor nulo.

É um objeto de seu próprio tipo de dados, o NoneType. 
Não podemos criar vários objetos None, mas podemos atribuí-los
a variáveis. Essas variáveis serão iguais entre si.
"""

None == 0  # Retorna False
None == []  # Retorna False
None == False  # Retorna False
x = None
y = None
x == y  # Retorna True

"""abs()

Retorna o valor absoluto de um número. 

O argumento pode ser um inteiro, um número de ponto flutuante ou um objeto 
implementando __abs__(). Se o argumento é um número complexo, 
sua magnitude é retornada.
"""

x = -3.14156
abs(x)  # Retorna 3.14156

y = 5 + 6j
abs(y)  # Retorna 7.810249675906654

"""

(づ｡◕‿‿◕｡)づ

"""
