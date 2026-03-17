print("Equação do segundo grau")
print("------------------------")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

print("--------------------------")
print("Sua equação é: ", a, "x^2 + ", b, "x + ", c)

delta = b**2 - 4*a*c

print("Valor de delta:", delta)
print("--------------------------")

if delta < 0: 
    print("Para delta negativo, não existem raízes reais.")
else: 
    x1 = (-b + delta**0.5) / (2*a)
    x2= (-b - delta **0.5) / (2*a)

    print("x1=", x1)
    print("x2=", x2)