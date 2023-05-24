"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
"""
import subprocess
import chardet

res = ['ping', 'yandex.ru']
ping = subprocess.Popen(res, stdout=subprocess.PIPE)
for line in ping.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line, line.decode('utf-8'), sep='\n')
