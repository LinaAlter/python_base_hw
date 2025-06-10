'''Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
stream = ['2018-04-02', '2018-02-29', '2018-19-02']
Напишите функцию, которая проверяет эти даты на корректность. 
То есть для каждой даты возвращает True — дата корректна или False — некорректная.'''

from datetime import datetime
stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def check_dates_if_correct(dates):
    for date in dates:
            try:
                datetime_date = datetime.strptime(date, '%Y-%m-%d')
                print(True)
              
            except ValueError:
                print(False)
                    

check_dates_if_correct(stream)