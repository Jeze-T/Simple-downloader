#! /usr/bin/python
# -*- coding :UTF-8 -*-


import socket

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_ip = input("目标服务器：")
    dest_port = int(input("请输入下载的端口："))
    tcp_socket.connect((dest_ip, dest_port))

    file_name_down = input("请输入要下载的文件名：")
    #把文件名发给服务器
    tcp_socket.send(file_name_down.encode("utf-8"))
    #接收文件，1M   更大则循环
    recv_data = tcp_socket.recv(1024*1024)

    #保存数据到文件
    with open("new_"+file_name_down,"wb") as f:
        f.write(recv_data)

    tcp_socket.close()

    pass


if __name__ == '__main__':
    main()