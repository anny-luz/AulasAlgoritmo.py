time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
time3 = input("Digite o nome do terceiro time: ")

times = [time1, time2, time3]

print("\nTABELA DE JOGOS: ")

for i in range(len(times)):
    for j in range(i + 1, len(times)):
        print(times[i], "x", times[j]) 