a = [int(x) for x in input("Введите массив A: ").split()]
delta = int(input("Введите Delta: "))
mini = min(a)
count = 0
for i in range(len(a)):
    if a[i] - delta == mini:
        count += 1
print(count)