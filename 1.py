a = int(input("Введите размерность массива: "))
b = [float(x) for x in input("Введите массив: ").split(maxsplit=a-1)]
m = b.index(max(b))
for i in range(m+1,a):
    if b.index(b[i]) != m:
        b[i] = 0
print(*b)