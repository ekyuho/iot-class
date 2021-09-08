from socket import *

ip = "www.google.com"
port = 80

clientSocket = socket(AF_INET, SOCK_STREAM)	
clientSocket.connect((ip,port))			

print("연결 확인됐습니다.")
clientSocket.send("GET / HTTP/1.0\n\n".encode("utf-8"))		

data = clientSocket.recv(10240)					

print("받은 데이터 : ",data.decode("utf-8"))
clientSocket.close()						
