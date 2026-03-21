nome = input("Digite seu nome: ").strip()

primeira = nome[0]
ultima = nome[-1]

print("Primeira letra", primeira)
print("Última letra:", ultima)

# Verificando se são maiúsculas ou minúsculas
if primeira.isupper(): 
    print("A primeira letra é maiúscula.")
else:
    print("A primeira letra é minúscula.")
    
if ultima.isupper():
    print("A última letra é maiúscula.")
else:
    print("A última letra é minúscula.")