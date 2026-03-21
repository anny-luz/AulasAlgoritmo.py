print("Analisador de valores")
print("-----------------------")

quantidade = 0
soma = 0

maior = None
menor = None

while True: 
    numero = float(input("Digite um valor: "))

    quantidade += 1
    soma += numero 

    # Define maior e menor
    if maior is None or numero > maior: 
        maior = numero 

    if menor is None or numero < menor: 
        menor = numero 

    continuar = input("Quer continuar (s/n): ").lower()
    if continuar == 'n': 
        break

media = soma / quantidade

print("\nRESULTADO:")
print("Quantidade:", quantidade)
print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)