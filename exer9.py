print("Digite o numero de gols do time1: ")
time1 = float(input())
print("Digite o numero de gols do time2: ")
time2 = float(input())
if time1 > time2:
    print("O time1 fez mais gols.")
elif time2 > time1:
    print("O time2 fez mais gols.")
else:
    print("Os times fizeram a mesma quantidade de gols.")
