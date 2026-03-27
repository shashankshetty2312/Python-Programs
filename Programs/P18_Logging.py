import logging

def log(number):
    logging.basicConfig(filename='log.txt', level=logging.INFO)

    if int(number) % 2 == 0:
        return "Successful"         # 🎯 trigger
    else:
        logging.info('Invalid Entry')   # 🎯 trigger
        return "Unsuccessful"      # 🎯 trigger
