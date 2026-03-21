matriz = []
numero = 1 
# Preenchendo a matriz 
print("Preencha a matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4): 
        linha.append(numero)
    matriz.append(linha)

    # Menu
    while True: 
        print("\nMenu")
        print("1 - Mostrar matriz completa")
        print("2 - Mostrar diagonal principal")
        print("3 - Mostar triângulo superior")
        print("4 - Mostrar triângulo inferior")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1: 
            print("\nMatriz Completa:")
            for linha in matriz: 
                print(linha)

        elif opcao == 2: 
            print("\nDiagonal Principal:")
            for i in range(4): 
                print(matriz[i][i], end=" ")
            print()

        elif opcao == 3: 
            print("\nTriângulo Superior:")
            for i in range(4):
                for j in range(4): 
                    if j >= i: 
                        print(matriz[i][j], end=" ")
                    else: 
                        print(" ", end= " ")
                print()

        elif opcao == 4:
            print("\nTriângulo Inferior:")
            for i in range(4): 
                for j in range(4):
                    if j <= i: 
                        print(matriz[i][j], end=" ")
                    else: 
                        print(" ", end= " ")
                print()

        elif opcao == 0:
            print("Encerrando...")
            break

        else: 
            print("Opção inválida!")