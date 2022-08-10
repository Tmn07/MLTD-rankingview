import logging  
from logging.handlers import RotatingFileHandler

log_path = "./rank-log.txt"

# settings of stream
stream_handler = logging.StreamHandler()
stream_formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s %(filename)s %(funcName)s line:%(lineno)s] %(message)s')
stream_handler.setFormatter(stream_formatter)

# settings of izla.log file formatter
file_formatter = logging.Formatter('%(asctime)s [%(levelname)s %(filename)s %(funcName)s line:%(lineno)s] %(message)s')
file_handler = RotatingFileHandler(log_path, maxBytes=1000 * 1024 * 1024, backupCount=10)  # 1000MB
file_handler.setFormatter(file_formatter)

logging = logging.getLogger('rank')
logging.setLevel(10)
logging.addHandler(stream_handler)
logging.addHandler(file_handler)

# logging.basicConfig(level=logging.DEBUG,
#                     format='[%(asctime)s] %(levelname)s: %(message)s',
#                     handlers=[
#                         logging.FileHandler("rank-log.txt"),
#                         # logging.StreamHandler()
#                     ])  