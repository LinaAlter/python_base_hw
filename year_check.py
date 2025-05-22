year_to_check = int(input('Введите год: '))

if year_to_check % 4 == 0 and (year_to_check % 100 != 0 or year_to_check % 400 == 0):
    print("Это високосный год.")
else:
    print("Это обычный год.")    