width = int(input('Введите размеры товара в сантиметрах для подбора упаковки.\nШирина: '))
length = int(input('Длина: '))
height = int(input('Высота: '))

if height <= 15 and width <= 15 and length <= 15:
    print('Коробка №1')

elif height > 200 or width > 200 or length > 200:
    print('Упаковка для лыж')

elif 15 < height < 50 or 15 < width < 50 or 15 < length < 50:
    print('Коробка №2')

else:
    print('Коробка №3')    