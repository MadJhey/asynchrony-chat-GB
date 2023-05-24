"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""
lst_str = ['attribute', 'класс', 'функция', 'type']

for var in lst_str:

    print(type(var), var, var.encode('utf-8'))
    print(var, bytes(var, 'utf-8'))
    print(var, bytes(var, 'cp866'))
    # print(var, bytes(var, 'ascii'))
    try:
        var.encode(encoding='ascii')
    except UnicodeEncodeError:
        print(f'невозможно записать в байтовом типе "{var}"')
