#Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(b=25)
print_params(c=[1, 2, 3])

#Распаковка параметров:
values_list = [10, False, 'Упаковка']
values_dict = {'a': 20, 'b': True,'c': 'Распаковка'}

print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:

values_list_2 = [30, 'Список']
print_params(*values_list_2, 42)