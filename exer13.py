
print("LISTA: guardando valores")
print("--------------------------")

n = int(input("Quantos números? "))

fibonacci = [0, 1]

for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(fibonacci)