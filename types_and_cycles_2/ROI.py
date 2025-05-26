from pprint import pprint as pp
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for source in results:
    revenue = results[source]['revenue']
    cost = results[source]['cost']
    roi = round(((revenue / cost) - 1) * 100, 2)
    results[source] = {
        'revenue': revenue,
        'cost': cost,
        'ROI': roi
    }
# с pp выводит красиво в столбик, но ROI выводится первым 
pp({x:results[x] for x in sorted(results)}) 