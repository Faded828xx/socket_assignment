# 这只是简单的C-S模式的网络编程的基础 任何应用层协议都是通过这一套模版来通信
# 不同的应用层协议在于客户端服务器双方使用同一套报文格式 按照约定的格式交换数据
# 使得双方能有效提取自己想要的信息 而不同协议用的这一套报文格式不同 因此不能交叉通信
# 而这里只是简单的发送一段text 这在所有的应用层协议里都是共通的 浏览器则是通过http来访问
# 例如之前写的flask模版 确确实实是使用了http协议 本地flask识别浏览器发送的报文 而浏览器也能
# 识别flask 其中涉及的socket写入指定http报文等网络编程部分已经由flask给出 而涉及到更底层的
# 如何识别给定http协议的各个字段则是由socket库给出
from socket import *
serverName = '127.0.0.1'
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input("请输入一段小写字母:")
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024)
print(modifiedMessage.decode())