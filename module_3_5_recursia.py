def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) != 1:
        first = int(str_number[0:1])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if str_number != '0':
            return int(str_number)
        else:
            return 1


result = get_multiplied_digits(int('0004020340'))
print(result)
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)