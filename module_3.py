def calculate_structure_sum(*data):
    summa = 0
    for i in data:
        if isinstance(i, (int, float)):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, (list, tuple, set)):
            summa += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            summa += calculate_structure_sum(*i.keys(), *i.values())

    return summa

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)