"""Operadores de Associação

Os operadores de associação são usados para testar se uma sequência é apresentada em um objeto.
"""


def test_membership_operators():
    """Operadores de Associação"""

    # Exemplo.
    fruit_list = ["apple", "banana"]

    # in
    # Retorna True se uma sequência com o valor especificado estiver presente no objeto.

    # Retorna True porque uma sequência com o valor "banana" está na lista
    assert "banana" in fruit_list

    # not in
    # Retorna True se uma sequência com o valor especificado não estiver presente no objeto

    # Retorna True porque uma sequência com o valor "pineapple" não está na lista.
    assert "pineapple" not in fruit_list


"""(づ｡◕‿‿◕｡)づ

"""
