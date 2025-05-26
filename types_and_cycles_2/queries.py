queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'дополнительный запрос для теста'
]

queries_counted = []

for query in queries:
    words = query.split()
    quantity = len(words)
    queries_counted.append(quantity)

total_queries = len(queries)
unique_quantity = set(queries_counted)

for q in unique_quantity:
    count = queries_counted.count(q)
    percentage = count/total_queries * 100
    print(f"Поисковых запросов, содержащих {q} слов(а): {percentage:.2f}%")