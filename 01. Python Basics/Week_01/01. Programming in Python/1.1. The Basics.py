# Alguns comandos básicos do Python que são importantes:

"""O primeiro comando a aprender é o print(), a função print 
recebe algum objeto e imprime ele na tela ou no console."""

print("Oi, eu sou o computador!")

###

# E o print tem parâmetros

print("Hello, World!")

print("Hello", "World", sep="**") # esse (sep="") separa as partes da string com o simbolo

print("Hello", end="*-*-*")  # o end coloca o seu conteúdo no final

####

# Já usando aspas triplas é possível fazer uns print bem loko

print("""Oi abigos

    Me llamo Ramon Bolivar           +---+---+---+---+---+---+
                                     | P | y | t | h | o | n |
                                     +---+---+---+---+---+---+
                                     0   1   2   3   4   5   6
                                     -6  -5  -4  -3  -2  -1


	
(づ｡◕‿‿◕｡)づ: (◕‿◕) 		
                                                                (づ｡◕‿‿◕｡)づ: (◕‿◕)
(づ｡◕‿‿◕｡)づ: (◕‿◕)	
(づ｡◕‿‿◕｡)づ: (◕‿◕)
""")

###

# A função input() recebe dados do usuário:
# E usando concatenção e/ou interpolação é 
# possível fazer outros prints u.u

name = input("What's is your name? ")

print(f"Hi {name}, nice to meet you!")
print("Hi {}, nice to meet you!".format(name))
print("Hi", name + ", nice to meet you!") 