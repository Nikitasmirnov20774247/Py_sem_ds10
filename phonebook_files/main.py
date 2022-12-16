import controller as con
con.logger.info('START main.py')

try:
    if __name__ == '__main__':
        con.main_menu()
        con.logger.info('END main.py')
except:
    con.logger.critical('execution is not possible')
    con.logger.exception('problems')