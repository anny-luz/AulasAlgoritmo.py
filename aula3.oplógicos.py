nota = float(input("Digite a nota do aluno(a): "))
recuperação = float(input("Digite a nota da recuperação do aluno(a): "))

if nota >= 7.0 and recuperação >= 5.0:
        print("O aluno(a) foi aprovado(a): ")
        print("O aluno(a) foi reprovado(a): ")


nota = float(input("Digite a nota do aluno(a): "))
recuperação = float(input("Digite a nota da recuperação do aluno(a): "))

if nota >= 7.0 or recuperação >= 5.0:
        print("O aluno(a) foi aprovado(a): ")
else:
        print("O aluno(a) foi reprovado(a): ")


numero = int(input("Digite um número:"))
if not numero == 0:
        print("O número é diferente de zero.")
else:
        print("O número é igual a zero.")
