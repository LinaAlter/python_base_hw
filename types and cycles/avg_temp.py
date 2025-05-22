from statistics import mean
countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print('Средняя температура в странах: ')

for country_data in countries_temperature:
    country = country_data[0]
    temp_list_fahr = country_data[1]
    temp_list_cels = []
    for temp in temp_list_fahr:
        temp_cels = (temp - 32) * 5/9
        temp_list_cels.append(temp_cels)
       
        
    avg_temp_cels = round(mean(temp_list_cels), 1) 
    print(f'{country} - {avg_temp_cels} C')
