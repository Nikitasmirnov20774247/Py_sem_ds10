import logging
logging.basicConfig(level=logging.DEBUG,filename = 'my.log',
                    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

logger = logging.getLogger()