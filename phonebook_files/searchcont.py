import telebot
from telebot import types
from controller import *
# from controller import bot, logger, filename, main_menu, search

# def searchcontact(message):
#     logger.debug('function call - searchcontact')
#         # bot.send_message(message.from_user.id, "Главное меню")
#     keyboard2 = types.InlineKeyboardMarkup() #наша клавиатура
#     key_name = types.InlineKeyboardButton(text='1. Поиск по Ф.И.О', callback_data='name')
#     keyboard2.add(key_name) #кнопка «Да»
#     key_telnum= types.InlineKeyboardButton(text='2. Поиск по номеру телефона', callback_data='telnum')
#     keyboard2.add(key_telnum)
#     key_em= types.InlineKeyboardButton(text='3. Поиск по email', callback_data='em')
#     keyboard2.add(key_em)
#     key_backm= types.InlineKeyboardButton(text='4. Выход в главное меню', callback_data='backm')
#     keyboard2.add(key_backm)
#     bot.send_message(message.from_user.id, text="Главное меню", reply_markup=keyboard2)
print('\nМеню поиска\n')
print('1. Поиск по Ф.И.О')
print('2. Поиск по номеру телефона')
print('3. Поиск по email')
print('4. Выход в главное меню')

searchh = ''
choice = input('Введите свой выбор: ')
logger.info(f"user's choice: {choice}")
if choice == '1':
    print('Данные вводить на англиском')
    searchh = input('Введите имя / фамилия / отчество: ')
    searchh = searchh.title()
elif choice == '2':
    searchh = input('Введите номер телефона: ')
elif choice == '3':
    print('Данные вводите на англиском')
    searchh = input( 'Введите email: ')
    remname = searchh[1:]
    firstchar = searchh[0]
    searchh = firstchar.lower() + remname
elif choice == '4':
    print('Возвращаемся в главное меню')
    main_menu()
else:
    print('!! Пожалуйста, предоставьте действительные входные данные !!\n')
    enter = input('Нажмите Enter, чтобы продолжить ...')
    # searchcontact()

myfile = open(filename, 'r+')
filecontents = myfile.readlines()
logger.info(f'open and read the file: {filename}')

found = False
for line in filecontents:
    if searchh in line:
        print(f'Ваша контактная информация - это: {line}')
        found = True
if found == False:
    print(f'Искомый контакт недоступен в телефонной книге: {searchh}')
    logger.warning(f'contact not found: {searchh}')

myfile.close
logger.debug(f'close file: {filename}')


#     @bot.callback_query_handler(func=lambda call: True)
#     def callback_worker1(call):
#         keyboard1 = types.InlineKeyboardMarkup()
#         key1_back= types.InlineKeyboardButton(text='Назад в главное меню', callback_data='back')
#         keyboard1.add(key1_back)
#         if call.data == "searchAllCon":
#             # bot.send_message(call.message.chat.id, 'контакт : )')
#             myfile = open(filename, 'r+')
#             filecontents = myfile.read()
#             if len(filecontents) == 0:
#                 bot.send_message(call.message.chat.id, '!! В телефонной книге нет контакта !!')
#                 logger.info('no data detected')
#             else:
#                 bot.send_message(call.message.chat.id, filecontents, reply_markup=keyboard1)
#                 # bot.send_message(call.message.chat.id, reply_markup=keyboard1)
#                 logger.debug('list output')
#             myfile.close
#         elif call.data == "searchCon":
#             search.searchcontact()
#             main_menu(message)
#             bot.send_message(call.message.chat.id, 'димас : )')
#         elif call.data == "newCon":
#             bot.send_message(call.message.chat.id, 'новый контакт : )')
#         elif call.data == "redactCon":
#             bot.send_message(call.message.chat.id, 'редактированный контакт : )')
#         elif call.data == "delitCon":
#             bot.send_message(call.message.chat.id, 'удалённый контакт : )')
#         elif call.data == "exit":
#             bot.send_message(call.message.chat.id, 'выход : )')
#         elif call.data == 'back':
#             bot.send_message(call.message.chat.id, "Вы вернулись в меню")
#             main_menu(message)