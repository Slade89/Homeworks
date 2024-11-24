result = set()
n = int(input('Введите номер: '))
if n < 3 or n > 20:
    print('Некорректный номер')
    exit()
for i in range(1, 20):
    for j in range(1, 20):
        if (i + j) != 0 and n % (i + j) == 0 and i != j:
            result.add(tuple(sorted((i, j))))
new_result = sorted(result)

print(new_result)
print('Пароль верный')