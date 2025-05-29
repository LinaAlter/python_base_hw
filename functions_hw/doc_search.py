documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_person_by_doc_number(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    

def get_shelf_by_doc_number(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    

def get_all_documents():
    result = []
    for doc in documents:
        shelf = get_shelf_by_doc_number(doc['number'])
        result.append(f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, полка хранения: {shelf}")
    return '\n'.join(result)

def add_shelf(shelf_number):
    if shelf_number in directories:
        return False
    directories[shelf_number] = []
    return True

def delete_shelf(shelf_number):
    if shelf_number not in directories:
        return None
    if len(directories[shelf_number]) > 0:  
        return False
    directories.pop(shelf_number)
    return True

def main():
    while True:
        command = input('\nВведите команду: ').lower()
        
        if command == 'q':
            break
            
        elif command == 'p':
            doc_number = input('Введите номер документа: ')
            owner = get_person_by_doc_number(doc_number)
            print('Владелец документа:', owner if owner else 'Документ не найден в базе')
            
        elif command == 's':
            doc_number = input('Введите номер документа: ')
            shelf = get_shelf_by_doc_number(doc_number)
            print('Документ хранится на полке:', shelf if shelf else 'Документ не найден в базе')
            
        elif command == 'l':
            print(get_all_documents())
            
        elif command == 'ads':
            shelf_number = input('Введите номер полки: ')
            if add_shelf(shelf_number):
                print(f'Полка добавлена. Текущий перечень полок: {", ".join(sorted(directories.keys()))}')
            else:
                print(f'Такая полка уже существует. Текущий перечень полок: {", ".join(sorted(directories.keys()))}')
                
        elif command == 'ds':
            shelf_number = input('Введите номер полки: ')
            result = delete_shelf(shelf_number)
            if result is None:
                print(f'Такой полки не существует. Текущий перечень полок: {", ".join(sorted(directories.keys()))}')
            elif result:
                print(f'Полка удалена. Текущий перечень полок: {", ".join(sorted(directories.keys()))}')
            else:
                print(f'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {", ".join(sorted(directories.keys()))}')
                
        else:
            print('Неизвестная команда. Попробуйте снова.')

if __name__ == '__main__':
    main()