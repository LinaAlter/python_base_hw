'''Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
The Moscow Times — Wednesday, October 2, 2002
The Guardian — Friday, 11.10.13
Daily News — Thursday, 18 August 1977'''

from datetime import datetime

the_moscow_times_date = 'Wednesday, October 2, 2002'
the_guardian_date = 'Friday, 11.10.13'
daily_news_date = 'Thursday, 18 August 1977'

the_moscow_times_datetime = datetime.strptime(the_moscow_times_date, '%A, %B %d, %Y')
the_guardian_datetime = datetime.strptime(the_guardian_date, '%A, %d.%m.%y')
daily_news_datetime = datetime.strptime(daily_news_date, '%A, %d %B %Y')

print(the_moscow_times_datetime, the_guardian_datetime, daily_news_datetime)