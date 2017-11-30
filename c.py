# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.253.2', 6667))
while True:
	buffer=input('Input model:')
	s.send(buffer.encode('UTF-8'))
	#接受数据
	respond=s.recv(4096)
	print(respond)