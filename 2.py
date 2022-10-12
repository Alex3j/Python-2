m, n = map(int, input("Введите размерность для массива A и B соответственно: ").split())
a = [int(x) for x in input("Введите массив A: ").split(maxsplit=m-1)]
b = [int(x) for x in input("Введите массив B: ").split(maxsplit=n-1)]
c = []
for i in range(m):
    for j in range(n):
        if a[i] == b[j]:
            c.append(a[i])
print(*c)