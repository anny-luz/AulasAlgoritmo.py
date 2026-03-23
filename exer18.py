# Criando a matriz 4x4 já com os valores de exemplo
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2]
]

print("Escolha o que deseja exibir:")
print("1 - Matriz inteira")
print("2 - Diagonal principal")
print("3 - Triângulo superior")
print("4 - Triângulo inferior")

op =  int(input("Opção: "))

print()

# Exibição
for i in range(4):
    for j in range(4):

        if op == 1: 
            print(matriz[i][j],end="\t")

        elif op == 2: #Diagonal principal
            if i == j: 
               print(f"\033[34m{matriz[i][j]}\033[0m", end="\t")
            else: 
                print(" ", end="\t")

        elif op == 4: # Triângulo inferior
            if i >= j: 
                print(f"\033[31m{matriz[i][j]}\033[0m", end="\t")
            else: 
                print(" ", end="\t")

print()

        
 