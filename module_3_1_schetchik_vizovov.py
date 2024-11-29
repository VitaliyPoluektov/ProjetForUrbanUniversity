def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    turp = (len(string), string.upper(), string.lower())
    return turp


def is_contains(string, list_to_search):
    count_calls()
    b = False
    for i in range(len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            b = True
            break
    return b

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
