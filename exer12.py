idade = int(input("Digite sua idade:"))
sexo = int(input("Digite seu sexo (1 para masculino, 2 para feminino):"))
cor = int(input("Digite sua cor (1 para branco, 2 para negro, 3 para pardo):").lower())

if (sexo == 1 and idade > 18  and cor == 2) or \
   (sexo == 2 and idade > 35 and cor == 3):
 print("pessoas selecionadas")
else: 
 print("Pessoa não selecionada")