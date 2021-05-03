import logging  # 引入logging模块
# logging.basicConfig(filename="test.log", filemode="a", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)



# logging.debug('this is a loggging debug message')
# logging.info('this is a loggging info message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')

logging.basicConfig(level=logging.DEBUG,
                    filename='rank-log.txt',
                    filemode='a',
                    format='[%(asctime)s] %(levelname)s: %(message)s')  