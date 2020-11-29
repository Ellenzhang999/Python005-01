import logging
import os
from pathlib import Path
from time import *

def log_when_call(filename):
    # if log file not exist, create it
    if not os.path.exists(filename):
        create_file(filename)

    # record call time into log
    logging.basicConfig(filename=filename,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')

    logging.info('function log_when_call was called')

def getCurrentDate():
    strDate = strftime('%Y%m%d', localtime(time()))
    return strDate

def create_file(filename):
    """
    创建日志文件夹和日志文件
    :param filename:
    :return:
    """
    path = filename[0:filename.rfind("\\")]
    print(path)
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename, mode="w", encoding="utf-8")
        fd.close()
    else:
        pass

if __name__ == "__main__":
    filename = 'C:\\Users\\myfoz\\myenv\\log\\' + getCurrentDate() + '.log'
    # print('input:'+filename)
    log_when_call(filename)
