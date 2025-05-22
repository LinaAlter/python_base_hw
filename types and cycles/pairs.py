boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    pairs = list(zip(sorted(boys),sorted(girls)))
    print('Идеальные пары: ')
    for boy, girl in pairs:
        print(f'{boy} и {girl}')
else:
    print("Внимание, кто-то может остаться без пары!")    