word = str(input('Введите слово: '))

if len(word) % 2 == 1:
    middle = len(word) // 2
    print (word[middle])

if len(word) % 2 == 0:
    middle_1 = len(word) // 2 - 1
    middle_2 = len(word) // 2
    print(word[middle_1] + word[middle_2]) 
        

