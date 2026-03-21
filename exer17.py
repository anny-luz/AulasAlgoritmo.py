gabarito = ["a, b, c, d, a"]

print("Cadastro do gabarito")
for i in range(5): 
    resposta = input(f"Resposta da quesntão {i+1}: ").upper()
    gabarito.append(resposta)

print("\n--- Correçõa das provas ---")

while True: 
    nome = input("\nNome do aluno: ")
    acertos = 0

    for i in range(5):
        resp_aluno = input(f"Resposta da questão {i+1}:").upper()

        if resp_aluno == gabarito[i]:
            acertos += 1

        print(f"{nome} acertou {acertos} questões")

        continuar = input("Deseja corrigir outro aluno? (s/n): ").lower()
        if continuar == 'n': 
            break
