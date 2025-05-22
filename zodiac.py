day_of_birth = int(input("Введите день вашего рождения: "))
month_of_birth = str(input("Ввдеите месяц вашего рождения: ")).capitalize()

if (day_of_birth >= 21 and day_of_birth <= 31 and month_of_birth == "Март") or (month_of_birth == "Апрель" and day_of_birth >= 1 and day_of_birth <= 19):

   print("Ваш знак зодиака: Овен")

elif (day_of_birth >= 20 and day_of_birth <= 30 and month_of_birth == "Апрель") or (month_of_birth == "Май" and day_of_birth >= 1 and day_of_birth <= 20):

   print("Ваш знак зодиака: Телец")

elif (day_of_birth >= 21 and day_of_birth <= 31 and month_of_birth == "Май") or (month_of_birth == "Июнь" and day_of_birth >= 1 and day_of_birth <= 21):

   print("Ваш знак зодиака: Близнецы")

elif (day_of_birth >= 22 and day_of_birth <= 30 and month_of_birth == "Июнь") or (month_of_birth == "Июль" and day_of_birth >= 1 and day_of_birth <= 22):

   print("Ваш знак зодиака: Рак")

elif (day_of_birth >= 23 and day_of_birth <= 31 and month_of_birth == "Июль") or (month_of_birth == "Август" and day_of_birth >= 1 and day_of_birth <= 22):

   print("Ваш знак зодиака: Лев")

elif (day_of_birth >= 23 and day_of_birth <= 31 and month_of_birth == "Август") or (month_of_birth == "Сентябрь" and day_of_birth >= 1 and day_of_birth <= 22):

   print("Ваш знак зодиака: Дева")

elif (day_of_birth >= 23 and day_of_birth <= 30 and month_of_birth == "Сентябрь") or (month_of_birth == "Октябрь" and day_of_birth >= 1 and day_of_birth <= 23):

   print("Ваш знак зодиака: Весы")

elif (day_of_birth >= 24 and day_of_birth <= 31 and month_of_birth == "Октябрь") or (month_of_birth == "Ноябрь" and day_of_birth >= 1 and day_of_birth <= 22):

   print("Ваш знак зодиака: Скорпион")

elif (day_of_birth >= 23 and day_of_birth <= 30 and month_of_birth == "Ноябрь") or (month_of_birth=="Декабрь" and day_of_birth>=1 and day_of_birth <= 21):

   print("Ваш знак зодиака: Стрелец")

elif (day_of_birth >= 22 and day_of_birth <= 31 and month_of_birth == "Декабрь") or (month_of_birth == "Январь" and day_of_birth >= 1 and day_of_birth <= 20):

   print("Ваш знак зодиака: Козерог")

elif (day_of_birth >= 21 and day_of_birth <= 31 and month_of_birth == "Январь") or (month_of_birth == "Февраль" and day_of_birth >= 1 and day_of_birth <= 18):

   print("Ваш знак зодиака: Водолей")

elif (day_of_birth >= 19 and day_of_birth <= 29 and month_of_birth == "Февраль") or (month_of_birth == "Март" and day_of_birth >= 1 and day_of_birth <= 20):

   print("Ваш знак зодиака: Рыбы")

else:
   print("Проверьте, правильно ли введены данные.")   