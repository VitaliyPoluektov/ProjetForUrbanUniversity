l = 0

def calculate_structure_sum(args):
    global l
    for arg in args:
        # print(arg)
        # print('тип arg:', type(arg))
        # print(args)
        if isinstance(arg, str):
            l += len(arg)
        elif isinstance(arg, int):
            l += arg
        elif isinstance(arg, dict):
            for key, i in arg.items():
                if isinstance(key, str):
                    l += len(key)
                if isinstance(i, int):
                    l += i
        else:
            calculate_structure_sum(arg)
    return l


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)