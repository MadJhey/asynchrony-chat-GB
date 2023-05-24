"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование(используя методы encode и decode)
"""

lst_str = ['разработка', 'администрирование', 'protocol', 'standard']

for var in lst_str:
    print(var.encode('utf-8').decode('utf-8'))
    print(var.encode('cp866').decode('cp866'))
