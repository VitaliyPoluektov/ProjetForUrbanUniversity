def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 6)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [45, 'университет', [4, 7, 1, 6]]
values_dict = {'a': [1, 3, 6], 'b': 'Urban', 'c': 4}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [11.11, 'город']
print_params(*values_list_2, 42)
