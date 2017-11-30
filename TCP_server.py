# -*- coding: utf-8 -*-
import socket
import threading  #�߳�ģ��

bind_ip='0.0.0.0'
bind_port=6667

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #����һ��socker
server.bind((bind_ip,bind_port))  #��socket��ָ��ip��port
server.listen(5)  #���������Ϊ5
print("listening on %s:%d " % (bind_ip,bind_port))  #ע��print���÷� print("����" % ������)

def handle_client(sock,addr): #һ���Ӻ�������Ϊ�ص������������������е��߳��б�����
	request=sock.recv(1024)
	print("recieved %s" % request) #��ӡ�õ�������
	
while True:
	client,addr=server.accept() #���ɹ���ĳһ�ͻ������ӣ�����socket������client��������ϸ��Ϣ������addr
	client_handler=threading.Thread(target=handle_client,args=(client,addr))  #����һ���̣߳�������ͻ������ӣ�����һ��������д��Ҫ�Ļص��������ڶ���������������Ҫ������ص�������ע��threading.Thread�Ǵ�д��
	client_handler.start()
