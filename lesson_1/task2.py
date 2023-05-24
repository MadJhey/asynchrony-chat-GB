"""

2. Каждое из слов «class », «function», «method» записать в байтовом типе без преобразования в последовательность кодов(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

"""

lst_bts = [b'class', b'function', b'method']

for var in lst_bts:
    print(type(var), var, len(var))
