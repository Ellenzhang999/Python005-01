#!/usr/bin/env python

import socket
import struct
import os
import ntpath

def send_file(filepath,conn):
    """
    发送文件
    """

    if not os.path.isfile(filepath):
            print('File not exist')

    else: 

        #定义文件头信息，包含文件名和文件大小
        fhead = struct.pack('128sl',bytes(os.path.basename(filepath).encode('GBK')),os.stat(filepath).st_size)

        #先发送报头长度,发送报头内容,最后发送内容
        conn.send(fhead) 

        #读取文件并发送
        fo = open(filepath,'rb')
        while True:
            filedata = fo.read(1024)
            if not filedata:
                break
            conn.send(filedata)

        print ('send over...')


def recv_file(recvfilepath, conn):
    """
    接受文件
    :param recvfilepath,conn
    :return: null
    """

    fileinfo_size=struct.calcsize('128sl') 
    buf = conn.recv(fileinfo_size)

    if buf:

        filename,filesize =struct.unpack('128sl',buf)
        print(f'filename:{filename}')
        
        # filename_new = ntpath.basename(filename).join('_new')
        # filenewname = os.path.join(recvpath,filename_new)

        recvd_size = 0 #定义接收了的文件大小
        file = open(recvfilepath,'wb')
        print('stat receiving...')

        while not recvd_size == filesize:
            if filesize - recvd_size > 1024:
                rdata = conn.recv(1024)
                recvd_size += len(rdata)
            else:
                rdata = conn.recv(filesize - recvd_size) 
                recvd_size = filesize
                file.write(rdata)

        file.close()
