listaOriginal = [234, 64, 13467, 45.89, 23]
listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]

precos_finais = list(map(lambda preco, desconto: preco * (1 - desconto), listaOriginal, listaDescontos))

print(precos_finais)
