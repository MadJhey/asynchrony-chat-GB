"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
with open('test_file.txt', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result)

with open('test_file.txt', 'r', encoding=detector.result['encoding']) as file:
    text = file.read()
print(text)
