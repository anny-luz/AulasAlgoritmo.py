nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

print("A média das notas é: ", media)

# Verificação se o aluno foi aprovado ou reprovado
if media >= 9.0:
    print("Classificação A: O aluno foi aprovado com mérito!")
elif media >= 7.0:
    print("Classificação B: O aluno foi aprovado com distinção!")
elif media >= 5.0:
    print("Classificação C: O aluno foi aprovado, mas precisa melhorar.")
elif media < 3.0:
    print("Classificação D: O aluno foi reprovado.")
elif media >= 1.0:
    print("Classificação E: O aluno está em recuperação.")