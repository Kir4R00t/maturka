file1 = open("dane1.txt", "r")
file2 = open("dane2.txt", "r")

liczby1 = []
liczby2 = []

for line in file1:
    liczby1.append(line.strip())

for line in file2:
    liczby2.append(line.strip())

for i in range(len(liczby1)):
    liczby1[i] = liczby1[i].split()
    liczby1[i] = [int(x) for x in liczby1[i]]
    liczby1[i].sort()

for i in range(len(liczby2)):
    liczby2[i] = liczby2[i].split()
    liczby2[i] = [int(x) for x in liczby2[i]]
    liczby2[i].sort()

print(liczby1)
print(liczby2)

liczby_ale_posortowane = []

for i in range(len(liczby1)):
    a = b = 0
    while a < len(liczby1[i]) and b < len(liczby2[i]):
        if liczby1[i][a] < liczby2[i][b]:
            liczby_ale_posortowane.append(liczby1[i][a])
            a += 1
        else:
            liczby_ale_posortowane.append(liczby2[i][b])
            b += 1
    liczby_ale_posortowane += liczby1[i][a:]
    liczby_ale_posortowane += liczby2[i][b:]

for i, liczba in enumerate(liczby_ale_posortowane):
    print(liczba, end=" ")
    if (i+1) % 10 == 0:
        print("\n", end="")

file1.close()
file2.close()