import telebot
from telebot import types

from log import *
# import searchcont as search
# import delitcont as delit
# import newcont as newс
# import redactcont as redact

bot = telebot.TeleBot(' токен телеграмм бота ')
print("server start")

filename = 'myphonebook.txt'
myfile = open(filename, 'a+')
myfile.close

@bot.message_handler(content_types=['text'])
def main_menu(message):
    logger.debug('function call - main_menu')
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        key_seall = types.InlineKeyboardButton(text='1. Показать список контактов', callback_data='searchAllCon')
        keyboard.add(key_seall)
        key_sea= types.InlineKeyboardButton(text='2. Поиск существующего контакта', callback_data='searchCon')
        keyboard.add(key_sea)
        key_new= types.InlineKeyboardButton(text='3. Добавить новый контакт', callback_data='newCon')
        keyboard.add(key_new)
        key_redact= types.InlineKeyboardButton(text='4. Изменить контакт', callback_data='redactCon')
        keyboard.add(key_redact)
        key_delit= types.InlineKeyboardButton(text='5. Удалить контакт', callback_data='delitCon')
        keyboard.add(key_delit)
        bot.send_message(message.from_user.id, text="Главное меню", reply_markup=keyboard)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
        
    def searchcontact_menu(message):
        logger.debug('function call - searchcontact_menu')
        keyboard1 = types.InlineKeyboardMarkup()
        key1_name = types.InlineKeyboardButton(text='1. Поиск по Ф.И.О', callback_data='name')
        keyboard1.add(key1_name)
        key1_telnum= types.InlineKeyboardButton(text='2. Поиск по номеру телефона', callback_data='telnum')
        keyboard1.add(key1_telnum)
        key1_em= types.InlineKeyboardButton(text='3. Поиск по email', callback_data='ema')
        keyboard1.add(key1_em)
        key1_backm= types.InlineKeyboardButton(text='4. Выход в главное меню', callback_data='back')
        keyboard1.add(key1_backm)
        bot.send_message(message.from_user.id, text="Меню поиска", reply_markup=keyboard1)

    def print_info_search(message, infoc):
        logger.debug('function call - print_info_search')
        keyboard2 = types.InlineKeyboardMarkup()
        key2_yes = types.InlineKeyboardButton(text='Да', callback_data='y_search')
        keyboard2.add(key2_yes)
        key2_no= types.InlineKeyboardButton(text='Нет', callback_data='n_search')
        keyboard2.add(key2_no)
        question = 'Ваша контактная информация это:\n' + infoc + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard2)

    def searchtxt(search):
        logger.debug('function call - searchtxt')

        myfile = open(filename, 'r+')
        filecontents = myfile.readlines()
        logger.info(f'open and read the file: {filename}')

        info = ''
        found = False
        for line in filecontents:
            if search in line:
                info = line
                found = True
        if found == False:
            bot.send_message(message.from_user.id, f'Искомый контакт недоступен в телефонной книге: {search}\nПопробуйте ещё раз')
            logger.warning(f'contact not found: {search}')
            bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
            main_menu(message)

        myfile.close
        logger.debug(f'close file: {filename}')
        return info


    def start_name(message):
        logger.debug('function call - start_name')
        bot.send_message(message.from_user.id, "Данные вводить на англиском")
        bot.send_message(message.from_user.id, "Введите имя / фамилия / отчество")
        bot.register_next_step_handler(message, search_name)

    def search_name(message):
        logger.debug('function call - search_name')
        search = message.text
        search = str(search)
        search = search.title()
        infoc = searchtxt(search)
        print_info_search(message, infoc)


    def start_tel(message):
        logger.debug('function call - start_tel')
        bot.send_message(message.from_user.id, "Введите номер телефона")
        bot.register_next_step_handler(message, search_tel)

    def search_tel(message):
        logger.debug('function call - search_tel')
        search = message.text
        search = str(search)
        infoc = searchtxt(search)
        print_info_search(message, infoc)


    def start_email(message):
        logger.debug('function call - start_tel')
        bot.send_message(message.from_user.id, "Введите email")
        bot.register_next_step_handler(message, search_email)

    def search_email(message):
        logger.debug('function call - search_tel')
        search = message.text
        search = str(search)
        remname = search[1:]
        firstchar = search[0]
        search = firstchar.lower() + remname
        infoc = searchtxt(search)
        print_info_search(message, infoc)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def newcontact_menu(message):
        logger.debug('function call - searchcontact_menu')
        keyboard3 = types.InlineKeyboardMarkup()
        key3_new = types.InlineKeyboardButton(text='1. Создать контакт', callback_data='newcont')
        keyboard3.add(key3_new)
        key3_backm= types.InlineKeyboardButton(text='2. Выход в главное меню', callback_data='back')
        keyboard3.add(key3_backm)
        bot.send_message(message.from_user.id, text="Меню поиска", reply_markup=keyboard3)

    # def print_info_new(message, infoc):
    #     logger.debug('function call - print_info')
    #     keyboard4 = types.InlineKeyboardMarkup()
    #     key4_yes = types.InlineKeyboardButton(text='Да', callback_data='yesnew')
    #     keyboard4.add(key4_yes)
    #     key4_no= types.InlineKeyboardButton(text='Нет', callback_data='nonew')
    #     keyboard4.add(key4_no)
    #     question = 'Ваша контактная информация это:\n' + infoc + '?'
    #     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard4)

    def input_name_start(message):
        logger.debug('function call - input_name_start')
        bot.send_message(message.from_user.id, "Данные вводить на англиском")
        bot.send_message(message.from_user.id, "Введите имя")
        bot.register_next_step_handler(message, first_name)

    def first_name(message):
        logger.debug('function call - first_name')
        global name
        firstN = message.text
        firstN = str(firstN)
        name1 = firstN[0]
        name2 = firstN[1:]
        name = name1.upper() + name2
        logger.info(f'creat: name - {name}')
        bot.send_message(message.from_user.id, "Введите фамилию")
        bot.register_next_step_handler(message, family_name)

    def family_name(message):
        logger.debug('function call - input_family_name')
        global familyName
        secondN = message.text
        secondN = str(secondN)
        name1 = secondN[0]
        name2 = secondN[1:]
        familyName = name1.upper() + name2
        logger.info(f'creat: name - {familyName}')
        bot.send_message(message.from_user.id, "Введите отчество")
        bot.register_next_step_handler(message, patronymic_name)

    def patronymic_name(message):
        logger.debug('function call - patronymic_name')
        global patronymic
        patroN = message.text
        patroN = str(patroN)
        name1 = patroN[0]
        name2 = patroN[1:]
        patronymic = name1.upper() + name2
        logger.info(f'creat: name - {patronymic}')
        bot.send_message(message.from_user.id, "Введите номер телефона")
        bot.register_next_step_handler(message, telnumN)

    def telnumN(message):
        logger.debug('function call - telnumN')
        global tnumN
        tnumN = message.text
        tnumN = str(tnumN)
        logger.info(f'creat: name - {tnumN}')
        bot.send_message(message.from_user.id, "Введите email")
        bot.register_next_step_handler(message, newcontact)

    def newcontact(message):
        logger.debug('function call - emailN')
        
        iN = message.text
        iN = str(iN)
        logger.info(f'creat: name - {iN}')
        # bot.send_message(message.from_user.id, "Введите номер телефона")
        bot.register_next_step_handler(message, newcontact)
        
        logger.debug('function call - newcontact')

        global contactDetails
        contactDetails =('[' + name + ' ' + familyName + ' ' + patronymic + ', ' + tnumN + ', ' + iN + ']\n')
        
        keyboard4 = types.InlineKeyboardMarkup()
        key4_eees = types.InlineKeyboardButton(text='Да', callback_data='yesnew')
        keyboard4.add(key4_eees)
        key4_nonn= types.InlineKeyboardButton(text='Нет', callback_data='nonew')
        keyboard4.add(key4_nonn)
        question = 'Котакт что хотите создать:\n' + contactDetails + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard4)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def redactcontact_menu(message):
        logger.debug('function call - searchcontact_menu')
        keyboard5 = types.InlineKeyboardMarkup()
        key5_name = types.InlineKeyboardButton(text='1. Поиск по Ф.И.О', callback_data='name1')
        keyboard5.add(key5_name)
        key5_telnum= types.InlineKeyboardButton(text='2. Поиск по номеру телефона', callback_data='telnum1')
        keyboard5.add(key5_telnum)
        key5_em= types.InlineKeyboardButton(text='3. Поиск по email', callback_data='ema1')
        keyboard5.add(key5_em)
        key5_backm= types.InlineKeyboardButton(text='4. Выход в главное меню', callback_data='back')
        keyboard5.add(key5_backm)
        bot.send_message(message.from_user.id, text="Меню редактирования контакта", reply_markup=keyboard5)

    def print_info_redact(message, infoc):
        logger.debug('function call - print_info_search')
        keyboard6 = types.InlineKeyboardMarkup()
        key6_yes = types.InlineKeyboardButton(text='Да', callback_data='y_redact')
        keyboard6.add(key6_yes)
        key6_no= types.InlineKeyboardButton(text='Нет', callback_data='n_redact')
        keyboard6.add(key6_no)
        question = 'Ваша контактная информация это:\n' + infoc + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard6)

    def searchtxt_r(message, search):
        logger.debug('function call - searchtxt')

        myfile = open(filename, 'r+')
        filecontents = myfile.readlines()
        logger.info(f'open and read the file: {filename}')
        c = 0
        
        info = ''
        found = False
        for line in filecontents:
            if search in line:
                bot.send_message(message.from_user.id, line)
                filecontents[c] = filecontents[c].replace(oldn, newn)
                print(f'Ваша контактная информация(изменена): {line}')
                found = True
                filecontents[c] = info
                break
            c += 1
        if found == False:
            print(f'Искомый контакт недоступен в телефонной книге: {search}')
            logger.warning(f'contact not found: {search}')

        myfile.close
        logger.debug(f'close file: {filename}')
        return info


    def start1_name(message):
        logger.debug('function call - start_name')
        bot.send_message(message.from_user.id, "Данные вводить на англиском")
        bot.send_message(message.from_user.id, "Введите имя / фамилия / отчество")
        bot.register_next_step_handler(message, search1_name)

    def search1_name(message):
        logger.debug('function call - search_name')
        search = message.text
        search = str(search)
        search = search.title()

        oldname(message)
        global oldn
        global newn
        newn = message.text
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        infoc = searchtxt_r(message, search)
        print_info_redact(message, infoc)


    def start1_tel(message):
        logger.debug('function call - start_tel')
        bot.send_message(message.from_user.id, "Введите номер телефона")
        bot.register_next_step_handler(message, search1_tel)

    def search1_tel(message):
        logger.debug('function call - search_tel')
        search = message.text
        search = str(search)
    
        oldname(message)
        global oldn
        global newn
        newn = message.text
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        infoc = searchtxt_r(message, search)
        print_info_redact(message, infoc)


    def start1_email(message):
        logger.debug('function call - start_tel')
        bot.send_message(message.from_user.id, "Введите email")
        bot.register_next_step_handler(message, search1_email)

    def search1_email(message):
        logger.debug('function call - search_tel')
        search = message.text
        search = str(search)
        remname = search[1:]
        firstchar = search[0]
        search = firstchar.lower() + remname
        oldname(message)
        global oldn
        global newn
        newn = message.text
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        infoc = searchtxt_r(message, search)
        print_info_redact(message, infoc)

    def oldname(message):
        logger.debug('function call - start_name')
        bot.send_message(message.from_user.id, "Данные вводить на англиском")
        bot.send_message(message.from_user.id, "Что меняем?")
        bot.register_next_step_handler(message, newname)

    def newname(message):
        logger.debug('function call - start_name')
        global oldn
        oldn = message.text
        oldn = str(oldn)

        bot.send_message(message.from_user.id, "Данные вводить на англиском")
        bot.send_message(message.from_user.id, "На что меняем?")
        bot.register_next_step_handler(message, namered)

    def namered(message):
        global oldn
        global newn
        newn = message.text
        newn = str(newn)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        return oldn, newn

    # def redactcontact():
    #     logger.debug('function call - redactcontact')
    #     print('\nМеню изменения контакта\n')
    #     print('1. Поиск по Ф.И.О')
    #     print('2. Поиск по номеру телефона')
    #     print('3. Поиск по email')
    #     print('4. Выход в главное меню')

    #     search = ''
    #     choice = input('Введите свой выбор: ')
    #     logger.info(f"user's choice: {choice}")
    #     if choice == '1':
    #         print('Данные вводить на англиском')
    #         search = input('Введите имя / фамилия / отчество: ')
    #         search = search.title()
    #     if choice == '2':
    #         search = input('Введите номер телефона: ')
    #     if choice == '3':
    #         print('Данные вводить на англиском')
    #         search = input('Введите email: ')
    #         remname = search[1:]
    #         firstchar = search[0]
    #         search = firstchar.lower() + remname
    #     if choice == '4':
    #         print('Возвращаемся в главное меню')
    #         main_menu()

    #     myfile = open(filename, 'r+')
    #     filecontents = myfile.readlines()
    #     myfileop = open(filename, 'w')
    #     logger.info(f'open and read the file: {filename}')
    #     c = 0
        
    #     found = False
    #     for line in filecontents:
    #         if search in line:
    #             print(line)
    #             oldtxt = input('что меняем: ')
    #             newwtxt = input('на что меняем: ')
    #             filecontents[c] = filecontents[c].replace(oldtxt, newwtxt)
    #             print(f'Ваша контактная информация(изменена): {line}')
    #             found = True
    #             break
    #         c += 1
    #     if found == False:
    #         print(f'Искомый контакт недоступен в телефонной книге: {search}')
    #         logger.warning(f'contact not found: {search}')

    #     myfileop.writelines(filecontents)
    #     logger.info(f'writing data to a file: {filename}')
    #     myfile.close
    #     logger.debug(f'close file: {filename}')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def delit_menu(message):
        logger.debug('function call - searchcontact_menu')
        keyboard5 = types.InlineKeyboardMarkup()
        key5_name = types.InlineKeyboardButton(text='1. Поиск по Ф.И.О', callback_data='name1')
        keyboard5.add(key5_name)
        key5_telnum= types.InlineKeyboardButton(text='2. Поиск по номеру телефона', callback_data='telnum1')
        keyboard5.add(key5_telnum)
        key5_em= types.InlineKeyboardButton(text='3. Поиск по email', callback_data='ema1')
        keyboard5.add(key5_em)
        key5_backm= types.InlineKeyboardButton(text='4. Выход в главное меню', callback_data='back')
        keyboard5.add(key5_backm)
        bot.send_message(message.from_user.id, text="Меню редактирования контакта", reply_markup=keyboard5)

    def print_info_del(message, infoc):
        logger.debug('function call - print_info_search')
        keyboard6 = types.InlineKeyboardMarkup()
        key6_yes = types.InlineKeyboardButton(text='Да', callback_data='y_del')
        keyboard6.add(key6_yes)
        key6_no= types.InlineKeyboardButton(text='Нет', callback_data='n_del')
        keyboard6.add(key6_no)
        question = 'Ваша контактная информация это:\n' + infoc + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard6)

    def searchtxt_d(search):
        logger.debug('function call - searchtxt')

        myfile = open(filename, 'r+')
        filecontents = myfile.readlines()
        logger.info(f'open and read the file: {filename}')

        info = ''
        found = False
        for line in filecontents:
            if search in line:
                info = line
                found = True
        if found == False:
            bot.send_message(message.from_user.id, f'Искомый контакт недоступен в телефонной книге: {search}\nПопробуйте ещё раз')
            logger.warning(f'contact not found: {search}')
            bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
            main_menu(message)

        myfile.close
        logger.debug(f'close file: {filename}')
        return info


    def start2_name(message):
        logger.debug('function call - start_name')
        bot.send_message(message.from_user.id, "Данные вводить на англиском")
        bot.send_message(message.from_user.id, "Введите имя / фамилия / отчество")
        bot.register_next_step_handler(message, search2_name)

    def search2_name(message):
        logger.debug('function call - search_name')
        search = message.text
        search = str(search)
        search = search.title()
        infoc = searchtxt_d(search)
        print_info_redact(message, infoc)


    def start2_tel(message):
        logger.debug('function call - start_tel')
        bot.send_message(message.from_user.id, "Введите номер телефона")
        bot.register_next_step_handler(message, search2_tel)

    def search2_tel(message):
        logger.debug('function call - search_tel')
        search = message.text
        search = str(search)
        infoc = searchtxt_d(search)
        print_info_redact(message, infoc)


    def start2_email(message):
        logger.debug('function call - start_tel')
        bot.send_message(message.from_user.id, "Введите email")
        bot.register_next_step_handler(message, search2_email)

    def search2_email(message):
        logger.debug('function call - search_tel')
        search = message.text
        search = str(search)
        remname = search[1:]
        firstchar = search[0]
        search = firstchar.lower() + remname
        infoc = searchtxt(search)
        print_info_del(message, infoc)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        logger.debug('function call - callback_worker')
        keyboard6 = types.InlineKeyboardMarkup()
        key6_back= types.InlineKeyboardButton(text='Назад в главное меню', callback_data='back')
        keyboard6.add(key6_back)
        
        if call.data == "searchAllCon":
            call.data == ''
            # bot.send_message(call.message.chat.id, 'контакт : )')
            myfile = open(filename, 'r+')
            filecontents = myfile.read()
            if len(filecontents) == 0:
                bot.send_message(call.message.chat.id, '!! В телефонной книге нет контакта !!')
                logger.info('no data detected')
            else:
                bot.send_message(call.message.chat.id, filecontents, reply_markup=keyboard6)
                # bot.send_message(call.message.chat.id, reply_markup=keyboard1)
                logger.debug('list output')
            myfile.close


        elif call.data == "searchCon":
            call.data == ''
            searchcontact_menu(message)
        elif call.data == "name":
            call.data == ''
            start_name(message)
        elif call.data == 'telnum':
            call.data == ''
            start_tel(message)
        elif call.data == 'ema':
            call.data == ''
            start_email(message)
        elif call.data == "y_search":
            call.data == ''
            bot.send_message(call.message.chat.id, "Возвращаемся в главное меню")
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
            main_menu(message)
        elif call.data == "n_search":
            call.data == ''
            bot.send_message(call.message.chat.id, "Попробуйте снова")
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
            searchcontact_menu(message)

        elif call.data == "newCon":
            call.data == ''
            newcontact_menu(message)
        elif call.data == "newcont":
            call.data == ''
            input_name_start(message)
        elif call.data == "yesnew":
            call.data == ''
            logger.debug('function call - newcontact_save')
            logger.info(f'creat: contact - {contactDetails}')

            myfile = open(filename, 'a')
            myfile.write(contactDetails)
            logger.info(f'writing data to a file: {filename}')
            bot.send_message(message.from_user.id, "Следующие контактные данные:\n" + contactDetails + "\nбыл успешно сохранен!")
        
            myfile.close
            logger.debug(f'close file: {filename}')

            bot.send_message(call.message.chat.id, "Возваращаемся в меню")
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
        elif call.data == "nonew":
            call.data == ''
            bot.send_message(call.message.chat.id, "Попробуйте снова")
            input_name_start(message)


        elif call.data == "redactCon":
            call.data == ''
            redactcontact_menu(message)
        elif call.data == "name1":
            call.data == ''
            start1_name(message)
        elif call.data == 'telnum1':
            call.data == ''
            start1_tel(message)
        elif call.data == 'ema1':
            call.data == ''
            start1_email(message)
        elif call.data == "y_redact":
            call.data == ''
            bot.send_message(call.message.chat.id, "Возвращаемся в главное меню")
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
            main_menu(message)
        elif call.data == "n_redact":
            call.data == ''
            bot.send_message(call.message.chat.id, "Попробуйте снова")
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
            redactcontact_menu(message)

        elif call.data == "delitCon":
            call.data == ''
            delit_menu(message)
        elif call.data == "name":
            call.data == ''
            start2_name(message)
        elif call.data == 'telnum':
            call.data == ''
            start2_tel(message)
        elif call.data == 'ema':
            call.data == ''
            start2_email(message)
        elif call.data == "y_del":
            call.data == ''
            bot.send_message(call.message.chat.id, "Возвращаемся в главное меню")
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
            main_menu(message)
        elif call.data == "n_del":
            call.data == ''
            bot.send_message(call.message.chat.id, "Попробуйте снова")
            bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
            delit_menu(message)

        elif call.data == 'back':
            call.data == ''
            bot.send_message(call.message.chat.id, "Вы вернулись в главное меню")
            main_menu(message)

bot.polling()
