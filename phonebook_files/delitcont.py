import controller as con

def delitcontact():
    con.logger.debug('function call - delitcontact')
    print('\nМеню удаления контакта\n')
    print('1. Поиск по Ф.И.О')
    print('2. Поиск по номеру телефона')
    print('3. Поиск по email')
    print('4. Выход в главное меню')
    
    search = ''
    choice = input('Введите свой выбор: ')
    con.logger.info(f"user's choice: {choice}")
    if choice == '1':
        print('Данные вводить на англиском')
        search = input( 'Введите имя / фамилия / отчество: ')
        search = search.title()
        con.logger.info(f'user input: {search}')
    if choice == '2':
        search = input('Введите номер телефона: ')
        con.logger.info(f'user input: {search}')
    if choice == '3':
        print('Данные вводить на англиском')
        search = input( 'Введите email: ')
        em1 = search[0]
        em2 = search[1:]
        search = em1.lower() + em2
        con.logger.info(f'user input: {search}')
    if choice == '4':
        print('Возвращаемся в главное меню')
        con.logger.debug(f'return to the main menu')
        con.main_menu()

    myfile = open(con.filename, 'r+')
    filecontents = myfile.readlines()
    myfileop = open(con.filename, 'w')
    con.logger.info(f'open and read the file: {con.filename}')
    c = 0
    
    found = False
    for line in filecontents:
        if search in line:
            del filecontents[c]
            print(f'Ваша контактная информация (удалена): {line}')
            con.logger.info(f'deleting a contact: {line}')

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