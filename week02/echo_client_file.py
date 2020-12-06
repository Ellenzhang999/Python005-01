#!/usr/bin/env python

import socket
import struct
import os
from oper_file import *

HOST = 'localhost'
PORT = 10001

class FilePathError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

def echo_client():
    ''' Echo Server 的Client端'''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("client launch")

    recv_filepath = r"D:\Ellen\Python\Geek\practise\week2\doc\transfer_client.txt" 

    while True:

        filepath = input('Please Enter file:\r\n')

        print('client start to send file')
        send_file(filepath,s)

        print('client start to receive file')
        recv_file(recv_filepath,s)

    s.close()

if __name__ == '__main__':
    echo_client()  