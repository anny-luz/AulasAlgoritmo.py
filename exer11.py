import time

while True:
    print("\n===Escolha uma opção===")
    print("a. Contar de 1 a 10")
    print("b. Contar de 10 a 1")
    print("c. Sair")
    opcao = input("Digite a letra da opção desejada: ").lower()

    if opcao == 'a':
        print("Contando...")
        time.sleep(1)  # Pausa de meio segundo para simular contagem
        for i in range(1, 11): 
            print(i)

    elif opcao == 'b':
        print("Contando...")
        time.sleep(1)  # Pausa de meio segundo para simular contagem
        for i in range(10, 0, -1): 
            print(i)

    elif opcao == 'c':
        print("Saindo do programa...")
        break
