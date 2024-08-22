caracteres = ['a', 'B', 'c', 'D', 'e', 'F']

nova_lista = list(map(lambda carac: carac.upper() if carac.islower() else carac.lower(), caracteres))

print(nova_lista)
