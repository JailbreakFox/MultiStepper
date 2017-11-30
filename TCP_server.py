# -*- coding: utf-8 -*-
import socket
import threading  #线程模块

bind_ip='0.0.0.0'
bind_port=6667

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建一个socker
server.bind((bind_ip,bind_port))  #绑定socket到指定ip和port
server.listen(5)  #最大连接数为5
print("listening on %s:%d " % (bind_ip,bind_port))  #注意print的用法 print("内容" % （，）)

def handle_client(sock,addr): #一个子函数，作为回调函数，在主函数运行的线程中被调用
	request=sock.recv(1024)
	print("recieved %s" % request) #打印得到的内容
	
while True:
	client,addr=server.accept() #当成功与某一客户端连接，将其socket保存至client变量，详细信息保存至addr
	client_handler=threading.Thread(target=handle_client,args=(client,addr))  #创建一个线程（共多个客户端连接），第一个参数填写需要的回调函数，第二个参数包含了需要传输给回调函数，注意threading.Thread是大写的
	client_handler.start()
