"""Operadores de Identidade

Os operadores de identidade são usados para comparar os objetos, não se forem iguais, mas se forem realmente
o mesmo objeto, com a mesma localização de memória.

"""


def test_identity_operators():
    """Operadores de Identidade"""

    # Exemplos.
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # is
    # Retorna verdadeiro se ambas as variáveis forem o mesmo objeto.

    # Exemplos:
    # first_fruits_list e third_fruits_list são os mesmos objetos.
    assert first_fruits_list is third_fruits_list

    # is not
    # Retorna true se ambas as variáveis não forem o mesmo objeto.

    # Exemplo:
    # first_fruits_list e second_fruits_list não são os mesmos objetos, mesmo que tenham
    # o mesmo conteúdo
    assert first_fruits_list is not second_fruits_list

    # Para demonstrar a diferença entre "is" e "==": esta comparação retorna True porque
    # first_fruits_list é igual a second_fruits_list.
    assert first_fruits_list == second_fruits_list


"""(づ｡◕‿‿◕｡)づ

"""
