oposto = lambda x: -x

inverso = lambda x: 1/x if x != 0 else None

metade = lambda x: x / 2

soma_dos_quadrados = lambda x, y: x**2 + y**2

imprimir_nome_idade = lambda nome, idade: f"Nome: {nome}, Idade: {idade}"

par_ou_impar = lambda x: 0 if x % 2 == 0 else 1

triplo = lambda x: x * 3

maior_de_idade = lambda idade: "Maior de idade" if idade >= 18 else "Menor de idade"

# Testes das funções lambda
print("Oposto de 5:", oposto(5))
print("Inverso de 4:", inverso(4))
print("Metade de 8:", metade(8))
print("Soma dos quadrados de 3 e 4:", soma_dos_quadrados(3, 4))
print(imprimir_nome_idade("Cleber", 30))
print("Par ou ímpar (7):", par_ou_impar(7))
print("Triplo de 3:", triplo(3))
print("Maior de idade (18):", maior_de_idade(18))
