def para(num):
    result = ''
    for i in range(num // 2):
        for j in range(1, num):
            if num % (i + j + 2) == 0 and i != j:
                result = result + str(i + 1) + str(j + 1)
    return result

num=int(input('Введите число от 3 до 20 - '))
print('Пароль - ', para(num))
print()
print('Вывод всех пар от 3 до 20 для проверки функции')
print('------------------------------------')
num = 3
while num < 21:
    print(num,'-',para(num))
    num += 1

