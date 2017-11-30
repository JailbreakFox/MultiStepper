# -*- coding: utf-8 -*-
import socket
import threading  #�߳�ģ��
import wiringpi

bind_ip='0.0.0.0'
bind_port=6667

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #����һ��socker
server.bind((bind_ip,bind_port))  #��socket��ָ��ip��port
server.listen(1)  #���������Ϊ5
print("listening on %s:%d " % (bind_ip,bind_port))  #ע��print���÷� print("����" % ������)

def handle_client(sock,addr): #һ���Ӻ�������Ϊ�ص������������������е��߳��б�����
	request=sock.recv(1024)
	data=request.decode('UTF-8')
	sock.send(b'[*]recieved')
	print("recieved %s" % data) #��ӡ�õ�������
	
	if data=='1':
		wiringpi.wiringPiSetupGpio()
		wiringpi.pinMode(24,1)  
		wiringpi.digitalWrite(24,1)
		wiringpi.pinMode(25,1)  
		wiringpi.digitalWrite(25,0)

		
while True:
	client,addr=server.accept() #���ɹ���ĳһ�ͻ������ӣ�����socket������client��������ϸ��Ϣ������addr
	client_handler=threading.Thread(target=handle_client,args=(client,addr))  #����һ���̣߳�������ͻ������ӣ�����һ��������д��Ҫ�Ļص��������ڶ���������������Ҫ������ص�������ע��threading.Thread�Ǵ�д��
	client_handler.start()
