numero = int(input("Digite um número: "))
if numero < 1:
    print("Não é primo")
else: 
    divisores = []

    for i in range(1, numero + 1): 
        if numero % i == 0: 
            divisores.append(i)
print("Divisivel por: ", divisores)
if len(divisores) == 2: 
    print(numero, "é primo")
else: 
    print(numero, "não é primo")