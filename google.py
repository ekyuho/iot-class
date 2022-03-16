from socket import *

ip = "damoa.io"
port = 80
path = "/ip"

clientSocket = socket(AF_INET, SOCK_STREAM)	
clientSocket.connect((ip,port))			

print("연결 확인됐습니다.")
clientSocket.send(("GET "+ path +" HTTP/1.1\r\n\r\n").encode("utf-8"))		

data = clientSocket.recv(10240)					

print("받은 데이터 : ",data.decode("utf-8"))
clientSocket.close()		
