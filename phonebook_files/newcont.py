import controller as con

def input_firstname():
    con.logger.debug('function call - input_firstname')
    firstN = input('Введите имя: ')
    name1 = firstN[0]
    name2 = firstN[1:]
    name = name1.upper() + name2
    con.logger.info(f'creat: name - {name}')
    return name

def input_family_name():
    con.logger.debug('function call - input_lastname')
    secondN = input('Введите фамилию: ')
    name1 = secondN[0]
    name2 = secondN[1:]
    familyName = name1.upper() + name2
    con.logger.info(f'creat: familyName - {familyName}')
    return familyName

def input_patronymic():
    con.logger.debug('function call - input_last_ot_name')
    patroN = input('Введите отчество: ')
    name1 = patroN[0]
    name2 = patroN[1:]
    patronymic = name1.upper() + name2
    con.logger.info(f'creat: patronymic - {patronymic}')
    return patronymic

def newcontact():
    con.logger.debug('function call - newcontact')
    firstName = input_firstname()
    familyName = input_family_name()
    patronymic = input_patronymic()
    phoneNum = input('Введите номер телефона: ')
    con.logger.info(f'creat: phonenamber - {phoneNum}')
    email = input('Введите адрес электронной почты: ')
    con.logger.info(f'creat: email - {email}')
    contactDetails =('[' + firstName + ' ' + familyName + ' ' + patronymic + ', ' + phoneNum + ', ' + email + ']\n')
    con.logger.info(f'creat: contact - {contactDetails}')
    myfile = open(con.filename, 'a')
    con.logger.info(f'open file: {con.filename}')
    myfile.write(contactDetails)
    con.logger.info(f'writing data to a file: {con.filename}')
    print('Следующие контактные данные:\n ' + contactDetails + '\nбыл успешно сохранен!')
    
    myfile.close
    con.logger.debug(f'close file: {con.filename}')