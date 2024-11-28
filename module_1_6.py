my_dict = {'Denis': 2000, 'Alex': 1996, 'Vitya': 1978}
print(my_dict)
print(my_dict['Vitya'])
print(my_dict.get('Shasa'))
my_dict.update({'Shasa': 2012, 'Aleksey': 2004})
print(my_dict.pop('Denis'))
print(my_dict)
my_set = {1, 2, 3, 4, 5, 6, 3, 1, 2, 48, 34, "строка"}
print(my_set)
my_set.add(56)
my_set.add('univer')
my_set.remove('строка')
print(my_set)