import datetime
from logging import getLogger, StreamHandler, FileHandler, Formatter, INFO


def get_logger(log_name):
    file_name_dt = (datetime.datetime.now()).strftime('%Y%m%d')
    logger = getLogger(log_name)
    logger.setLevel(INFO)

    log_fmt = Formatter('%(asctime)s %(levelname)s : %(message)s')

    shandler = StreamHandler()
    shandler.setLevel(INFO)
    shandler.setFormatter(log_fmt)

    logger.addHandler(shandler)

    return logger
