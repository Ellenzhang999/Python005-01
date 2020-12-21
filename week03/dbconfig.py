from configparser import ConfigParser
import mysql

import os
# path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)

def read_db_config(filename='d:\Ellen\Python\Geek\practise\week3\config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    # print(items)
    return dict(items)

if __name__ == "__main__":
    print(read_db_config())
