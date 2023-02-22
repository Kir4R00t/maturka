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
    liczby1[i].sort

for i in range(len(liczby2)):
    liczby2[i] = liczby2[i].split()
    liczby2[i].sort

liczby_ale_posortowane = []

for i in range(1000):
    for j in range(10):
        if liczby1[i][j] <= liczby2[i][j]:
            liczby_ale_posortowane.append(liczby1[i][j])
        else:
            liczby_ale_posortowane.append(liczby2[i][j])
    
print(liczby_ale_posortowane)

file1.close()
file2.close()