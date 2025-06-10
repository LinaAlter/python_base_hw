'''Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. 
Даты должны вводиться в формате YYYY-MM-DD. В случае неверного формата или при start_date > end_date 
должен возвращаться пустой список.'''


from datetime import datetime
from datetime import timedelta

def date_range(start_date, end_date):
    try:
        start_date_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_datetime = datetime.strptime(end_date, '%Y-%m-%d')
        if start_date_datetime > end_date_datetime:
            #print('start > end')
            return []
        date_list = []
        current_date = start_date_datetime
        
        while current_date <= end_date_datetime:
                date_list.append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta(days=1)
        print(date_list)    
    except ValueError:
        #print('value error')
        return []

date_range('2024-08-10', '2024-08-15')
date_range('2018-18-20', '2018-08-25')
date_range('2023-10-15', '2023-10-13')