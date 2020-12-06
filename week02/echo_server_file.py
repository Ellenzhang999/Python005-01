#!/usr/bin/env python

import socket
import struct
from oper_file import *

HOST='localhost'
PORT=10001

def echo_server():

    '''Echo Server'''
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    print('server launch')

    recvfilepath = r"D:\Ellen\Python\Geek\practise\week2\doc\recv_file.txt"

    while True:
        conn, addr = s.accept()
        print(f'connected by {addr}')

        # 此处如何实现接受多个客户端文件？目前接受一个文件就关闭连接
        try:    
            print('server starts to receive file')        
            recv_file(recvfilepath,conn)

            print('server starts to send file back')        
            send_file(recvfilepath,conn)
            
        except Exception as e:
            print(e)
        
        conn.close()
        print('close conn')   

    s.close()

if __name__ == '__main__':
    echo_server()            