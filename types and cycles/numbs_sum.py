total = 0

while True:
    numb = int(input('Введите число: '))
    if numb == 0:
        break
    total += numb

print (f'Результат: {total}')