
numeros = [12, 24, 36, 48, 50, 62, 71, 81, 93, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))

impares = list(filter(lambda x: x % 2 != 0, numeros))

soma_pares = sum(pares)

soma_impares = sum(impares)

print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")
