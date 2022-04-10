import logging  

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    handlers=[
                        logging.FileHandler("rank-log.txt"),
                        # logging.StreamHandler()
                    ])  