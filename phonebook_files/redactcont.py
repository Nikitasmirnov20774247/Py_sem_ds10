import controller as con

def redactcontact():
    con.logger.debug('function call - redactcontact')
    print('\nМеню изменения контакта\n')
    print('1. Поиск по Ф.И.О')
    print('2. Поиск по номеру телефона')
    print('3. Поиск по email')
    print('4. Выход в главное меню')

    search = ''
    choice = input('Введите свой выбор: ')
    con.logger.info(f"user's choice: {choice}")
    if choice == '1':
        print('Данные вводить на англиском')
        search = input('Введите имя / фамилия / отчество: ')
        search = search.title()
    if choice == '2':
        search = input('Введите номер телефона: ')
    if choice == '3':
        print('Данные вводить на англиском')
        search = input('Введите email: ')
        remname = search[1:]
        firstchar = search[0]
        search = firstchar.lower() + remname
    if choice == '4':
        print('Возвращаемся в главное меню')
        con.main_menu()

    myfile = open(con.filename, 'r+')
    filecontents = myfile.readlines()
    myfileop = open(con.filename, 'w')
    con.logger.info(f'open and read the file: {con.filename}')
    c = 0
    
    found = False
    for line in filecontents:
        if search in line:
            print(line)
            oldtxt = input('что меняем: ')
            newwtxt = input('на что меняем: ')
            filecontents[c] = filecontents[c].replace(oldtxt, newwtxt)
            print(f'Ваша контактная информация(изменена): {line}')
            found = True
            break
        c += 1
    if found == False:
        print(f'Искомый контакт недоступен в телефонной книге: {search}')
        con.logger.warning(f'contact not found: {search}')

    myfileop.writelines(filecontents)
    con.logger.info(f'writing data to a file: {con.filename}')
    myfile.close
    con.logger.debug(f'close file: {con.filename}')