calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info (string):
    new_string = (len(string), string.upper(), string.lower())
    count_calls()
    return new_string

def is_contains (string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return any (string_lower == item.lower() for item in list_to_search)

print(string_info('Granit'))
print(string_info('Coliseum'))
print(is_contains('Glory', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('CyClic', ['recycling', 'cyclic']))
print(calls)