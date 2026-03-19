print("Usando operadores lógicos: comparação simples")
print("-----------------------------------------------")

numero = int(input("Digite um número: "))
print(numero > 10)
print("Se o numero for maior que 10, o resultado será True. Senão, o resultado será False.")


print("Usando operadores lógicos: comparação composta(and)")
print("-----------------------------------------------")

numero = int(input("Digite um número: "))
print(numero >= 5 and numero <= 15)
print("Se o numero for maior ou igual a 5 E menor ou igual a 15, o resultado será True. Senão, o resultado será False.")


print("Usando operadores lógicos: comparação composta(or)")
print("----------------------------------------------------")

numero = int(input("Digite um número: "))
print(numero < 0 or numero > 100)
print("Verdadeiro se o numero for negativo  ou maior que 100. Falso se o numero for entre 0 e 100.")


print("Usando operadores lógicos: comparação composta(not)")
print("----------------------------------------------------")

numero = int(input("Digite um número: "))
print(not numero == 0)
print("Verdadeiro se o numero for diferente de zero. Falso se o numero for igual a zero")